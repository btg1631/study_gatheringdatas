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

# def Connect_Mongo():
#     mongoClient = MongoClient("mongodb://192.168.10.10:27017")
#     database = mongoClient["project_coliving"]
#     collection = database["news"]
#     return collection

# - 주소 입력
browser.get("https://news.naver.com/section/102")
time.sleep(2)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# def insert_db(collection): 

# 기사 더보기 클릭  div.section_latest > div > div.section_more > a
for i in range(2):
    button = browser.find_element(by=By.CSS_SELECTOR, value="div.section_latest > div > div.section_more > a")
    button.click()

# 스크롤을 페이지 상단으로 이동
browser.execute_script("window.scrollTo(0, 0);")


# 뉴스    div.section_latest > div > div.section_latest_article._CONTENT_LIST._PERSIST_META > div > ul > li
selector_value = "div.section_latest_article._CONTENT_LIST._PERSIST_META > div > ul > li > div > div > div.sa_text > a"

# 기사의 총 개수를 먼저 파악합니다.
element_bundle_initial = browser.find_elements(By.CSS_SELECTOR, value=selector_value)
total_articles = len(element_bundle_initial)

for i in range(total_articles):
    # 매번 새로운 요소 리스트를 가져옵니다.
    element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
    if len(element_bundle) > i:
        # 기사 클릭
        element_bundle[i].click()
        time.sleep(2)  # 페이지 로드를 기다립니다.

        # 언론사   #img.media_end_head_top_logo_img.light_type._LAZY_LOADING._LAZY_LOADING_INIT_HIDE
        try:
            selector_value_press = "img.media_end_head_top_logo_img.light_type._LAZY_LOADING._LAZY_LOADING_INIT_HIDE"
            element_press = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_press)
            press = element_press.get_attribute('alt')
        except: 
            press = "None"

        # 제목   
        try:
            selector_value_title = "#title_area > span"
            element_title = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_title)
            title = element_title.text
        except: 
            title = "None"

        # 내용
        try:
            selector_value_content = "#dic_area"
            element_content = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_content)
            content = element_content.text
        except: 
            content = "None"

        print("press : {}, title : {}, content : {}".format(press, title, content))
        # db에 저장
        # collection.insert_one({"press" : press, "title" : title, "content" : content})

        browser.back()

    else:
        print("No more articles to click.")
        break

# collection = Connect_Mongo()
# ScrollHeight()
# insert_db(collection)

# 브라우저 종료
browser.quit()


