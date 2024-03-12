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

def Connect_Mongo():
    mongoClient = MongoClient("mongodb://192.168.10.10:27017")
    database = mongoClient["project_coliving"]
    collection = database["news"]
    return collection

# - 주소 입력
browser.get("https://search.naver.com/search.naver?where=news&query=%EC%BD%94%EB%A6%AC%EB%B9%99%ED%95%98%EC%9A%B0%EC%8A%A4&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds=2019.03.06&de=2024.03.06&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Afrom20190306to20240306&is_sug_officeid=0&office_category=0&service_area=0")

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def ScrollHeight():
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
        time.sleep(2)
        pass


def insert_db(collection): 
    # div.group_news > ul > li
    selector_value = "div.group_news > ul > li"
    element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
    for element_item in element_bundle:
        time.sleep(2)

        # 언론사  div.info_group > a
        try:
            selector_value_press = "div.info_group > a"
            element_press = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_press)
            press = element_press.text
        except: 
            press = "None"
        # 제목  div.news_contents > a.news_tit
        try:
            selector_value_title = "div.news_contents > a.news_tit"
            element_title = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_title)
            title = element_title.text
        except: 
            title = "None"
        # 내용  div.news_contents > div > div > a
        try:
            selector_value_content = "div.news_contents > div > div > a"
            element_content = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_content)
            content = element_content.text
        except: 
            content = "None"


        print("press : {}, title : {}, content : {}".format(press, title, content))
        # db에 저장
        collection.insert_one({"press" : press, "title" : title, "content" : content})


collection = Connect_Mongo()
ScrollHeight()
insert_db(collection)

# 브라우저 종료
browser.quit()


