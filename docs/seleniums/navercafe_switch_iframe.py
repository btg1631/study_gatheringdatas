# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://cafe.naver.com/peopledisc")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
#menuLink84 : 병원진료후기 메뉴
element_click = browser.find_element(by=By.CSS_SELECTOR, value="#menuLink84")
element_click.click()

# iframe 으로 전환
browser.switch_to.frame("cafe_main")

#main-area > div:nth-child(4) > table > tbody > tr : 해당 리스트
cafe_list = browser.find_elements(by=By.CSS_SELECTOR, value="#main-area > div:nth-child(4) > table > tbody > tr")
pass

# 브라우저 종료
browser.quit()
