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
browser.get("http://192.168.10.245:8000/")


# - 정보 획득
from selenium.webdriver.common.by import By
time.sleep(2)
login_button = browser.find_element(by=By.CSS_SELECTOR, value="div.col-md-3.text-end > form > button")
login_button.click()

# element_login_field = browser.find_element(by=By.CSS_SELECTOR, value="#user_email")
# element_login_field.send_keys("btg1631@naver.com")

# element_password_field = browser.find_element(by=By.CSS_SELECTOR, value="#user_password")
# element_password_field.send_keys("******")

# element_login_button = browser.find_element(by=By.CSS_SELECTOR, value="div > section.section_email.er_r > fieldset > button")
# element_login_button.click()


# 브라우저 종료
browser.quit()