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
from pymongo import MongoClient


mongoClient = MongoClient("mongodb://localhost:27017")
database = mongoClient["gatheringdatas"]
collection = database["11st_comments"]

# - 주소 입력
browser.get("https://www.11st.co.kr/products/2733986352?trTypeCd=34")

# - 정보 획득
from selenium.webdriver.common.by import By

browser.find_element(by=By.CSS_SELECTOR, value="#tabDetail > ul > li:nth-child(2)").click()

# iframe 으로 전환
browser.switch_to.frame("ifrmReview")

# while True:
for i in range(5):
    try:
        browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
    except:
        break
    time.sleep(2)

selector_value = "li.review_list_element"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for element_item in element_bundle:
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
        selector_value_review = "div.cont_text_wrap > p"
        element_review = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_review)
        review = element_review.text
    except:
        review = "None"

    # db에 저장
    collection.insert_one({"user_name" : username, "option" : option, "score" : score, "review" : review})

# 브라우저 종료
browser.quit()
