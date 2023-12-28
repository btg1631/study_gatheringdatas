# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# mongodb 연결
def Connectdb(collection_name):
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["gatheringdatas"]
    collection = database[collection_name]
    return collection

# 상품 정보
def Element(index, collection1):
    element_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a > span.best")
    element_companies[index].click()    # 상품 클릭
    time.sleep(1)
    
    try:        # 상품 이름
        element_title = browser.find_element(by=By.CSS_SELECTOR, value="h1.title")
        title = element_title.text
    except:
        title = "None"
    try:        # 상품 이미지
        element_image = browser.find_element(by=By.CSS_SELECTOR, value="#productImg > div > img")
        image = element_image.get_attribute('src')
    except:
        element_image = browser.find_element(by=By.CSS_SELECTOR, value="div.img_full.img_full_height > img")
        image = element_image.get_attribute('src')
    try:        # 상품 원가
        element_oldprice = browser.find_element(by=By.CSS_SELECTOR, value="dd.price_regular")
        oldprice = element_oldprice.text
    except:
        oldprice = "None"    
    try:        # 상품 판매가
        element_price = browser.find_element(by=By.CSS_SELECTOR, value="dd.price > strong > span.value")
        price = element_price.text
    except:
        price = "None"

    rows = browser.find_elements(by=By.CSS_SELECTOR, value="#tabpanelDetail1 > table > tbody > tr")
    data = []
    for row in rows:        # 상품 정보
        cols = row.find_elements(By.TAG_NAME, 'td')        # 각 행의 모든 열 가져오기
        cols_text = [col.text for col in cols]        # 각 열의 텍스트 정보 가져오기
        data.append(cols_text)

    try:        # db에 저장
        element_result = collection1.insert_one({"element_number": data[0][1], "title" : title, "image" : image, "oldprice" : oldprice, "price" : price})
        element_id = element_result.inserted_id
        # "state" : data[0][0], "delivery" : data[1][1], "origin" : data[2][1]
    except:
        element_result = collection1.insert_one({"element_number": "None", "title" : title, "image" : image, "oldprice" : oldprice, "price" : price, "Expiration_date" : data[0][0]})
        element_id = element_result.inserted_id
    return element_id

# 리뷰
def Review(element_id, collection2):
        # while True:        # 리뷰 더보기 클릭
        #     try:
        #         browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
        #     except:
        #         break
        #     time.sleep(1)

        browser.switch_to.frame("ifrmReview")        # iframe 으로 전환
        time.sleep(2)

        selector_value = "li.review_list_element"
        element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
        time.sleep(1)
        for element_item in element_bundle[0:3]:
            try:            # 작성자
                selector_value_username = "dt.name"
                element_username = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_username)
                username = element_username.text
            except:
                username = "None"
            try:            # 선택 옵션
                selector_value_option = "div.option > dd"
                element_option = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_option)
                option = element_option.text
            except:
                try:
                    selector_value_option = "p.option"
                    element_option = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_option)
                    option = element_option.text
                except:
                    option = "None"
            try:            # 별점
                selector_value_score = "div > p.grade > span > em"
                element_score = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_score)
                score = element_score.text
            except:
                score = "None"
            try:            # 내용
                button = element_item.find_element(by=By.CSS_SELECTOR, value="button.c_product_btn.c_product_btn_more6.review-expand-open-text")
                button.click()  # 더보기 버튼 클릭
                time.sleep(1)

                selector_value_review = "div.cont_text_wrap.active > p"
                element_review = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_review)
                review = element_review.text
            except:             # 버튼이 없는 경우
                selector_value_review = "div.cont_text_wrap > p"
                element_review = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_review)
                review = element_review.text

            # db에 저장
            collection2.insert_one({"element_id" : element_id, "user_name" : username, "option" : option, "score" : score, "review" : review})
        pass

# 주소 입력
url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
browser.get(url)

collection1 = Connectdb("11st_item")
collection2 = Connectdb("11st_item_comments")

for index in range(4) :
    element_id = Element(index, collection1)
    Review(element_id, collection2)
    browser.back()    # 뒤로가기
    time.sleep(2)

# 브라우저 종료
browser.quit()