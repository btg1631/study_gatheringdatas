# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
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

# - 주소 입력
browser.get("https://deal.11st.co.kr/browsing/DealAction.tmall?method=getShockingDealMain")

# - 정보 획득
from selenium.webdriver.common.by import By

selector_value = "div.c-card-item.c-card-item--collection.c-card-item--box > a"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for element_item in element_bundle[0:4]:
    element_item.click()    # 상품 클릭
    time.sleep(1)

    # 상품 이름
    try:
        element_title = browser.find_element(by=By.CSS_SELECTOR, value="h1.title")
        title = element_title.text
    except:
        title = "None"
    # 상품 이미지
    try:
        element_image = browser.find_element(by=By.CSS_SELECTOR, value="div.img_full.img_full_height > img")
        image = element_image.get_attribute('src')
    except:
        element_image = browser.find_element(by=By.CSS_SELECTOR, value="div.img_full.img_full_width > img")
        image = element_image.get_attribute('src')
    # 상품 원가
    try:
        element_oldprice = browser.find_element(by=By.CSS_SELECTOR, value="dd.price_regular")
        oldprice = element_oldprice.text
    except:
        oldprice = "None"    
    # 상품 판매가
    try:
        element_price = browser.find_element(by=By.CSS_SELECTOR, value="dd.price > strong > span.value")
        price = element_price.text
    except:
        price = "None"

    rows = browser.find_elements(by=By.CSS_SELECTOR, value="#tabpanelDetail1 > table > tbody > tr")

    data = []
    for row in rows:
        # 각 행의 모든 열 가져오기
        cols = row.find_elements(By.TAG_NAME, 'td')
        # 각 열의 텍스트 정보 가져오기
        cols_text = [col.text for col in cols]
        data.append(cols_text)

    collection = Connectdb("11st_item")
    # db에 저장
    collection.insert_one({"element_number": data[0][1], "title" : title, "image" : image, "oldprice" : oldprice, "price" : price})


    # 리뷰 더보기 클릭
    # while True:
    #     try:
    #         browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
    #     except:
    #         break
    #     time.sleep(1)

    # iframe 으로 전환
    browser.switch_to.frame("ifrmReview")

    # 댓글
    collection = Connectdb("11st_item_comments")
    selector_value = "li.review_list_element"
    element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
    for element_item in element_bundle[0:3]:
        # 작성자
        try:
            selector_value_username = "dt.name"
            element_username = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_username)
            username = element_username.text
        except:
            username = "None"
        # 선택 옵션
        try:
            selector_value_option = "div.option > dd"
            element_option = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_option)
            option = element_option.text
        except:
            selector_value_option = "p.option"
            element_option = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_option)
            option = element_option.text
        # 별점
        try:
            selector_value_score = "div > p.grade > span > em"
            element_score = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_score)
            score = element_score.text
        except:
            score = "None"
        # 내용
        try:
            button = element_item.find_element(by=By.CSS_SELECTOR, value="button.c_product_btn.c_product_btn_more6.review-expand-open-text")
            button.click()  # 더보기 버튼 클릭
            time.sleep(1)

            selector_value_review = "div.cont_text_wrap.active > p"
            element_review = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_review)
            review = element_review.text
        except:
            # 버튼이 없는 경우
            selector_value_review = "div.cont_text_wrap > p"
            element_review = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_review)
            review = element_review.text

        # db에 저장
        collection.insert_one({"element_number" : data[0][1], "user_name" : username, "option" : option, "score" : score, "review" : review})

    browser.back()    # 뒤로가기
    time.sleep(2)
    pass
pass


# 브라우저 종료
browser.quit()
