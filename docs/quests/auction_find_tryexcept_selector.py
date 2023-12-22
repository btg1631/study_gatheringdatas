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
browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")

# - 가능 여부에 대한 OK 받음
pass

# - 정보 획득
from selenium.webdriver.common.by import By
selector_value = "div > div.info"
# 전체 상품 정보
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for element_item in element_bundle[0:30]:
    # 상품 제목
    selector_value_title = "em > a"
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_title)
    title = element_title.text

    # 상품 판매 원가
    try:
        selector_value_old_price = "strike > span"
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_old_price)
        old_price = element_old_price.text
    except: 
        old_price = "None"

    # 상품 가격
    try:
        selector_value_price = "span.sale > span"
        element_price = element_item.find_element(by=By.CSS_SELECTOR, value=selector_value_price)
        price = element_price.text
    except: 
        price = "None"

    # 배송 
    try:
        selector_value_delivery = "div.icon > div > div > span"
        element_delivery = element_item.find_elements(by=By.CSS_SELECTOR, value=selector_value_delivery)
        delivery = [list_element_delivery.text for list_element_delivery in element_delivery]
    except: 
        delivery = "None"

    print("title : {}, old price : {}, price : {}, delivery : {}".format(title, old_price, price, delivery))
    pass
pass

# 브라우저 종료
browser.quit()