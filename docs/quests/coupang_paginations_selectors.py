# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Chrome 브라우저 옵션 생성
chrome_options = Options()
# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# WebDriver 생성
webdriver_manager_directory = ChromeDriverManager().install()
# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
for page_number in range(1, 7):        # page number
    url = "https://www.coupang.com/np/campaigns/348?page={}".format(page_number)
    browser.get(url)
    time.sleep(3)

    # - html 파일 받음(and 확인)
    html = browser.page_source
    pass

# 브라우저 종료
browser.quit()
