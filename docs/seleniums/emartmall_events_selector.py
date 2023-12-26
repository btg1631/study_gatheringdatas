# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=1
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=2
# ...
# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033&page=10


# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
driver = webdriver.Chrome()

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory), options=chrome_options)

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
for page_number in range(1, 7):        # page number
    url = "https://emart.ssg.com/disp/category.ssg?dispCtgId=6000213247&page={}".format(page_number)
    browser.get(url)
    time.sleep(3)
    # - html 파일 받음(and 확인)
    html = browser.page_source
    pass

# - 가능 여부에 대한 OK 받음

# - html 파일 받음(and 확인)
pass
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

pass
# browser.save_screenshot('./formats.png')

# 브라우저 종료
browser.quit()
