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

# mongodb
from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost:27017")
database = mongoClient["gatheringdatas"]
collection = database["watcha_comments"]

# - 주소 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/mWLjlkd/comments")
html = browser.page_source

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
## 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")

previous_scrollHeight = 0
while True:
    element_body.send_keys(Keys.END)

    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
    if previous_scrollHeight >= current_scrollHeight:
        break
    else:
        previous_scrollHeight = current_scrollHeight
    time.sleep(1)
    pass

selector_value = "ul > div.css-13j4ly.egj9y8a4"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for element_item in element_bundle:
    # 작성자
    try:
        selector_value_username = "a > div.css-eldyae.e10cf2lr1"
        element_username = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_username)
        username = element_username.text
    except: 
        username = "None"
    # 별점 점수
    try:
        selector_value_score = "div.css-31ods0.egj9y8a0 > span"
        element_score = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_score)
        score = element_score.text
    except: 
        score = "None"
    # 내용
    try:
        selector_value_review = "div.css-2occzs.egj9y8a1 > a > div > span"
        element_review = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_review)
        review = element_review.text
    except: 
        review = "None"

    # db에 저장
    collection.insert_one({"user_name" : username, "score" : score, "review" : review})

# 브라우저 종료
browser.quit()

# document.body.scrollHeight
# browser.execute_script("return document.body.scrollHeight")
# ul > div.css-13j4ly.egj9y8a4
