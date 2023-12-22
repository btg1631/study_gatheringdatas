from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
capabilities = browser.capabilities

# 주소 입력
browser.get("https://www.coupang.com/np/categories/194282")

# 정보 획득
from selenium.webdriver.common.by import By

selector_value = "div.name"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for webelement in elements_path:  
    title = webelement.text
    print("{}".format(title))

# 브라우저 종료
browser.quit()

