# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import re

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://play.google.com/store/apps/details?id=com.tripadvisor.tripadvisor")
time.sleep(1)

# 모달 화면 띄우기 : 리뷰 모두 보기 클릭
selector_element = "#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div:nth-child(1) > div > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > div > div.Jwxk6d > div:nth-child(5) > div > div > button"
browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()
time.sleep(1)

# - 정보 획득
# 댓글 모달 확인 : (css overflow:scroll or auto) div.fysCi
selector_element = "div.fysCi"
element_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)


# 댓글 div.fysCi > div > div:nth-child(2) > div
element_bundle_review = browser.find_elements(By.CSS_SELECTOR, value="div.fysCi > div > div:nth-child(2) > div")
for i in element_bundle_review:
    # 사용자 이름 div.YNR7H > div.gSGphe > div
    try:
        element_name = i.find_element(by=By.CSS_SELECTOR, value="div.YNR7H > div.gSGphe > div")
        user_name = element_name.text
    except:
        user_name = ""
    # 별점 div.Jx4nYe > div  ->  두번째 숫자만 
    try:
        element_score = i.find_element(by=By.CSS_SELECTOR, value="div.Jx4nYe > div")
        aria_label = element_score.get_attribute("aria-label")
        
        pattern = "별표 5개 만점에 ([0-9]+)개를 받았습니다."
        user_score = re.search(pattern, aria_label)
    except:
        user_score = ""

    # 날짜 div.Jx4nYe > span
    try:
        element_date = i.find_element(by=By.CSS_SELECTOR, value="div.Jx4nYe > span")
        user_date = element_date.text
    except:
        user_date = ""
    # 내용 div.h3YV2d
    try:
        element_comments = i.find_element(by=By.CSS_SELECTOR, value="div.h3YV2d")
        user_comments = element_comments.text
    except:
        user_comments = ""
    # 유용하다고 평가한 사람 div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div:nth-child(2) > div > div > div  -> 숫자만
    try:
        element_evaluation = i.find_element(by=By.CSS_SELECTOR, value="div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div:nth-child(2) > div > div > div")
        evaluation = element_evaluation.text

        pattern = "사용자 ([0-9]+)명이 이 리뷰가 유용하다고 평가함"
        evaluation = re.search(pattern, evaluation)

    except:
        evaluation = ""

    print("user_name:{}, user_score:{}, user_date:{}, user_comments:{}, evaluation:{}".format(user_name, user_score.group(1), user_date, user_comments, evaluation.group(1)))

pass

# 브라우저 종료
browser.quit()
