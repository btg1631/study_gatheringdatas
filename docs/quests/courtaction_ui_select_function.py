# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# mongodb 연결
def Connectdb(collection_name):
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["gatheringdatas"]
    collection = database[collection_name]
    return collection

def Court(coll):
    # iframe 으로 전환
    browser.switch_to.frame("indexFrame")
    # 경매물건 클릭
    menu = browser.find_element(by=By.CSS_SELECTOR, value="#menu > h1:nth-child(5)")
    menu.click()

    element_courts = browser.find_elements(by=By.CSS_SELECTOR, value="#idJiwonNm > option")
    for index in range(len(element_courts)):
        element_courts = browser.find_elements(by=By.CSS_SELECTOR, value="#idJiwonNm > option")
        # 법원 선택
        select_court = Select(browser.find_element(by=By.CSS_SELECTOR, value="#idJiwonNm"))
        option_value = element_courts[index].get_attribute("value")
        select_court.select_by_value(option_value)

        # select_court = browser.find_element(by=By.CSS_SELECTOR, value="#idJiwonNm")
        # Select(select_court).select_by_index(index)
        # 법원 이름 저장
        court_num = browser.find_element(by=By.CSS_SELECTOR, value="#idJiwonNm > option:nth-child({})".format(index+1))
        court = court_num.text
        # 검색 클릭
        search = browser.find_element(by=By.CSS_SELECTOR, value="#contents > form > div.tbl_btn > a:nth-child(1)")
        search.click()
        time.sleep(1)

        Court_nextpage(court, coll)
    # 브라우저 종료
    browser.quit()

def Court_nextpage(court, coll):
    for k in range(2, 12):
        element_table = browser.find_elements(by=By.CSS_SELECTOR, value="form:nth-child(1) > table > tbody > tr")   # table 길이 찾기
        Court_insertdata(court, element_table, coll)
        
        try:            # 다음 페이지
            page = browser.find_element(by=By.CSS_SELECTOR, value="div.page2 > a:nth-child({})".format(k))
            page.click()
            time.sleep(1)
            element_table = browser.find_elements(by=By.CSS_SELECTOR, value="form:nth-child(1) > table > tbody > tr")
        except:         
            try:             # 다음 페이지
                page = browser.find_element(by=By.CSS_SELECTOR, value="div.page2 > a:nth-child({})".format(k+1))
                page.click()
                time.sleep(1)
            except:         # 다음 페이지가 없을 경우 이전 클릭
                back = browser.find_element(by=By.CSS_SELECTOR, value="form:nth-child(1) > div > div > a:nth-child(5)")
                back.click()
                break

def Court_insertdata(court, element_table, coll):
    for j in range(1, len(element_table)+1):   # table 길이만큼만 반복
        try:            # 사건번호  
            selector_value_case_number = "form:nth-child(1) > table > tbody > tr:nth-child({}) > td:nth-child(2)".format(j)
            case_number = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_case_number)
            casenumber = case_number.text
        except:
            casenumber = "None"
        try:            # 소재지 및 내역  
            selector_value_case_location = "tr:nth-child({}) > td:nth-child(4) > div".format(j)
            case_location = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_case_location)
            caselocation = case_location.text
        except:
            caselocation = "None"

        # db 저장
        # coll.insert_one({"court" : court, "case_number" : casenumber, "case_location" : caselocation})
        print({"court" : court, "case_number" : casenumber, "case_location" : caselocation})

def create_browser():
    webdriver_manager_directory = ChromeDriverManager().install()
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities
    browser.get("https://www.courtauction.go.kr/")

    return browser, capabilities


if __name__ == "__main__":
    browser, capabilities = create_browser()
    collection = Connectdb("courtaction")
    Court(collection)

