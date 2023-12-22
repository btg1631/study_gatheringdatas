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
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

# -----------------------------------------------------------------------------------------------------------
## 하나의 element 정보 가져오기
selector_value = "#ty_thmb_view > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit"
element_path = browser.find_element(by=By.CSS_SELECTOR, value=selector_value)
# browser.find_element(By.CSS_SELECTOR, "#ty_thmb_view > ul > li:nth-child(1) > div > a > div.mnemitem_tit > span.mnemitem_goods_tit")

type(element_path)
# <class 'selenium.webdriver.remote.webelement.WebElement'>

# get text in tag
element_path.text
# '반려견패드(중)40*50cm*100매'
element_path.get_attribute('class')
# 'mnemitem_goods_tit'

# -----------------------------------------------------------------------------------------------------------
## 여러개 elements 정보 가져오기
selector_value = "span.mnemitem_goods_tit"
elements_path = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)

type(elements_path)
# <class 'list'>
type(elements_path[0])
# <class 'selenium.webdriver.remote.webelement.WebElement'>
elements_path[0].text
# '시리우스 펫퓸 반려견 러블리플라워 샴푸 500ML'
elements_path[1].text
# '시리우스 펫퓸 반려견 드라이풋샴푸 270ML'
for webelement in elements_path:  
    title = webelement.text
    print("{}".format(title))
    pass

pass

# 브라우저 종료
browser.quit()

#\37 047313102 > a > dl > dd > div.name