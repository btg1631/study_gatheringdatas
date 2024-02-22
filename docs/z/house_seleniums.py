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
browser.get("https://dgdr.co.kr/branch/index.html")

# - 정보 획득
from selenium.webdriver.common.by import By

# 각 아이템 클릭
selector_value = "div.scrollbar-outer.scroll-content.scroll-scrolly_visible > div > ul > li"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)
for element_item in element_bundle:
    element_item.click()
    time.sleep(2)

    # 제목(title)   #contents > h1
    try:
        selector_value_title = "#contents > h1"
        element_title = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_title)
        title = element_title.text
    except: 
        title = "None"



    # 지역은 역 이름으로 뽑아!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # 지역(region)   div.map-desc > div:nth-child(1) > div
    try:
        selector_value_region = "div.map-desc > div:nth-child(1) > div"
        element_region = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_region)
        region = element_region.text
    except: 
        region = "None"

    # 회사(회사가 아니면 일반사업자 - brandType)   #contents > h1
    try:
        brandType = "None"
    except: 
        brandType = "None"

    # url


    # 옵션(roomOption)   div:nth-child(1) > div > div.desc
    try:
        selector_value_roomOption = "div:nth-child(1) > div > div.desc"
        element_roomOption = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_roomOption)
        roomOption = element_roomOption.text
    except: 
        roomOption = "None"
    
    # imgUrl 1개만   div.container-wrap.on > div.swiper-container.swiper-container-initialized.swiper-container-horizontal > div > div.swiper-slide.swiper-slide-active > div > img
    try:
        selector_value_imgUrl = "div.container-wrap.on > div.swiper-container.swiper-container-initialized.swiper-container-horizontal > div > div.swiper-slide.swiper-slide-active > div > img"
        element_imgUrl = browser.find_element(by=By.CSS_SELECTOR, value=selector_value_imgUrl)
        imgUrl = element_imgUrl.get_attribute('src')
    except: 
        imgUrl = "None"
        
    # 입주현황전체정보 n번 반복해애ㅑ함   tbody > tr 
    selector_value_room = "tbody > tr"
    element_bundle_room = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value_room)
    for element_item_room in element_bundle_room:
        # 방 이름(roomName)   td:nth-child(2)
        try:
            selector_value_roomName = "td:nth-child(2)"
            element_roomName = element_item_room.find_element(by=By.CSS_SELECTOR, value=selector_value_roomName)
            roomName = element_roomName.text
        except: 
            roomName = "None"

        # 성별(남,여, 공용-gender)   td:nth-child(3)
        try:
            selector_value_gender = "td:nth-child(3)"
            element_gender = element_item_room.find_element(by=By.CSS_SELECTOR, value=selector_value_gender)
            gender = element_gender.text
        except: 
            gender = "None"

        # 1인실 or 그 외(roomType)   td:nth-child(4)
        try:
            selector_value_roomType = "td:nth-child(4)"
            element_roomType = element_item_room.find_element(by=By.CSS_SELECTOR, value=selector_value_roomType)
            roomType = element_roomType.text
            if roomType == '1인실':
                roomType = element_roomType.text
            else:
                roomType = "그 외"
        except: 
            roomType = "None"

        # 평수(추후 범주형 변환-py)   td:nth-child(5)
        try:
            selector_value_py = "td:nth-child(5)"
            element_py = element_item_room.find_element(by=By.CSS_SELECTOR, value=selector_value_py)
            py = element_py.text
        except: 
            py = "None"

        # 보증금(deposit)   td:nth-child(6)
        try:
            selector_value_deposit = "td:nth-child(6)"
            element_deposit = element_item_room.find_element(by=By.CSS_SELECTOR, value=selector_value_deposit)
            deposit = element_deposit.text
        except: 
            deposit = "None"

        # 월세가격(rentFee)   td:nth-child(7)
        try:
            selector_value_rentFee = "td:nth-child(7)"
            element_rentFee = element_item_room.find_element(by=By.CSS_SELECTOR, value=selector_value_rentFee)
            rentFee = element_rentFee.text
        except: 
            rentFee = "None"

        print("title : {}, roomName : {}, gender : {}, roomType : {}, py : {}, deposit : {}, rentFee : {}, region : {}, brandType : {}, roomOption : {}, url : {}, imgUrl : {}".format(title, roomName, gender, roomType, py, deposit, rentFee, region, brandType, roomOption, imgUrl, imgUrl))


    browser.back()
    time.sleep(2)


# 브라우저 종료
browser.quit()
