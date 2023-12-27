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
url = "https://play.google.com/store/search?q=%ED%97%AC%EC%8A%A4%EC%BC%80%EC%96%B4%EC%95%B1&c=apps&hl=ko-KR&pli=1"
browser.get(url)

# - 정보 획득
from selenium.webdriver.common.by import By
# 앱 제조회사 리스트 : div > a.Si6A0c.Gy4nib
elements_companies = browser.find_elements(by=By.CSS_SELECTOR, value="div > a.Si6A0c.Gy4nib")
for company in elements_companies:
    company.click()
    time.sleep(1)       # 화면 완성 term
    # 앱 상세 제목 : div > h1
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div > h1")
    print("App company Name : {}".format(element_title.text))
    browser.back()      # 제품 리스트로 이동
    time.sleep(1)       # 화면 완성 term
    pass
pass


# 브라우저 종료
browser.quit()
