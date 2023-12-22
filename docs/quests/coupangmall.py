# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://www.coupang.com/np/categories/194282")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

selector_value = "div.name"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

for webelement in elements_path:  
    title = webelement.text
    print("{}".format(title))
    pass

pass

# 브라우저 종료
browser.quit()

