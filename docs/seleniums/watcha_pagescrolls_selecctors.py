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

# - 주소 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/m5ZlbBL/comments")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

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


# browser.save_screenshot('./formats.png')

# 브라우저 종료
browser.quit()

# document.body.scrollHeight
# browser.execute_script("return document.body.scrollHeight")
# ul > div.css-13j4ly.egj9y8a4