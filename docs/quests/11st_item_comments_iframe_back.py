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
url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb'
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By

def Element(collection1, collection2):
    for index in range(4) :
        element_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a > span.best")
        element_companies[index].click()    # 상품 클릭
        time.sleep(1)

        # 상품 이름
        try:
            element_title = browser.find_element(by=By.CSS_SELECTOR, value="h1.title")
            title = element_title.text
        except:
            title = "None"
        # 상품 이미지
        try:
            element_image = browser.find_element(by=By.CSS_SELECTOR, value="#productImg > div > img")
            image = element_image.get_attribute('src')
        except:
            element_image = browser.find_element(by=By.CSS_SELECTOR, value="div.img_full.img_full_height > img")
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
        # 상품 정보
        data = []
        for row in rows:
            # 각 행의 모든 열 가져오기
            cols = row.find_elements(By.TAG_NAME, 'td')
            # 각 열의 텍스트 정보 가져오기
            cols_text = [col.text for col in cols]
            data.append(cols_text)

        # db에 저장
        try:
            element_result = collection1.insert_one({"element_number": data[0][1], "title" : title, "image" : image, "oldprice" : oldprice, "price" : price})
            element_id = element_result.inserted_id
            # "state" : data[0][0], "delivery" : data[1][1], "origin" : data[2][1]
        except:
            element_result = collection1.insert_one({"element_number": "None", "title" : title, "image" : image, "oldprice" : oldprice, "price" : price, "Expiration_date" : data[0][0]})
            element_id = element_result.inserted_id

        # 리뷰 더보기 클릭
        # while True:
        #     try:
        #         browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
        #     except:
        #         break
        #     time.sleep(1)

        # iframe 으로 전환
        browser.switch_to.frame("ifrmReview")
        time.sleep(2)
        # 댓글
        selector_value = "li.review_list_element"
        element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
        time.sleep(1)
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
                try:
                    selector_value_option = "p.option"
                    element_option = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_option)
                    option = element_option.text
                except:
                    option = "None"
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
            collection2.insert_one({"element_id" : element_id, "user_name" : username, "option" : option, "score" : score, "review" : review})

        browser.back()    # 뒤로가기
        time.sleep(2)
        pass

collection1 = Connectdb("11st_item")
collection2 = Connectdb("11st_item_comments")
Element(collection1, collection2)

# 브라우저 종료
browser.quit()