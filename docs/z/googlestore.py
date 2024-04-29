def get_data(database_name,url):
    # * 웹 크롤링 동작
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    import time
    import re

    webdriver_manager_directory = ChromeDriverManager().install()
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities


    # mongodb 연결
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://192.168.10.240:27017")
    database = mongoClient["AI_LKJ"]
    collection = database['TRAVEL_APPLICATION']

    # - 주소 입력
    browser.get(url)
    time.sleep(2)

    # 모달 화면 띄우기 : 리뷰 모두 보기 클릭
    selector_element = "#yDmH0d > c-wiz.SSPGKf.Czez9d > div > div > div:nth-child(1) > div > div.wkMJlb.YWi3ub > div > div.qZmL0 > div:nth-child(1) > c-wiz:nth-child(4) > section > div > div.Jwxk6d > div:nth-child(5) > div > div > button"
    browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()
    time.sleep(2)

    # 선택 #formFactor_2 > div.kW9Bj > i   //// div.JPdR6b.e5Emjc.CblTmf.ah7Sve.qjTEB > div > div > span:nth-child(2)
    selector_element = "#formFactor_2 > div.kW9Bj > i"
    browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()
    time.sleep(2)

    selector_element = "div.JPdR6b.e5Emjc.CblTmf.ah7Sve.qjTEB > div > div > span:nth-child(2)"
    browser.find_element(by=By.CSS_SELECTOR, value=selector_element).click()
    time.sleep(2)
    
    # - 정보 획득
    # 댓글 모달 확인 : (css overflow:scroll or auto) div.fysCi
    selector_element = "div.fysCi"
    element_scrollableDiv = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)

    previous_scrollHeight = 0
    while True:
    #for i in range(10):
        # python 방식 변수 매칭
        # print("{0}.scrollTo({1}, {0}.scrollHeight);".format(element_scrollableDiv, previous_scrollHeight))
        
        # javascript와 python을 결합한 방식 변수 매칭
        browser.execute_script("arguments[0].scrollTo(arguments[1], arguments[0].scrollHeight);", element_scrollableDiv, previous_scrollHeight)

        current_scrollHeight = browser.execute_script("return arguments[0].scrollHeight", element_scrollableDiv)
        if previous_scrollHeight >= current_scrollHeight:
            break
        else:
            previous_scrollHeight = current_scrollHeight
        time.sleep(1)
        pass

    # 댓글 개수 확인 : div.RHo1pe
    selector_element = "div.RHo1pe"
    elements_comment = browser.find_elements(by=By.CSS_SELECTOR, value=selector_element)
    print("count comment after done scroll : {}".format(len(elements_comment)))

    # ---------------------------------------------------------------------------

    # 댓글 div.fysCi > div > div:nth-child(2) > div
    element_bundle_review = browser.find_elements(By.CSS_SELECTOR, value="div.fysCi > div > div:nth-child(2) > div")
    for i in element_bundle_review:
        # 사용자 이름 div.YNR7H > div.gSGphe > div
        try:
            element_name = i.find_element(by=By.CSS_SELECTOR, value="div.YNR7H > div.gSGphe > div")
            user_name = element_name.text
        except:
            user_name = ""
        # 별점 div.Jx4nYe > div  ->  두번째 숫자만 
        try:
            element_score = i.find_element(by=By.CSS_SELECTOR, value="div.Jx4nYe > div")
            aria_label = element_score.get_attribute("aria-label")
            
            pattern = "별표 5개 만점에 ([0-9]+)개를 받았습니다."
            user_score = re.search(pattern, aria_label)
            user_score = user_score.group(1)
        except:
            user_score = ""

        # 날짜 div.Jx4nYe > span
        try:
            element_date = i.find_element(by=By.CSS_SELECTOR, value="div.Jx4nYe > span")
            user_date = element_date.text
        except:
            user_date = ""
        # 내용 div.h3YV2d
        try:
            element_comments = i.find_element(by=By.CSS_SELECTOR, value="div.h3YV2d")
            user_comments = element_comments.text
        except:
            user_comments = ""
        # 유용하다고 평가한 사람 div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div:nth-child(2) > div > div > div  -> 숫자만
        try:
            element_evaluation = i.find_element(by=By.CSS_SELECTOR, value="div.VfPpkd-wzTsW > div > div > div > div > div.fysCi > div > div:nth-child(2) > div > div > div")
            evaluation = element_evaluation.text

            pattern = "사용자 ([0-9]+)명이 이 리뷰가 유용하다고 평가함"
            evaluation = re.search(pattern, evaluation)
            evaluation = evaluation.group(1)

        except:
            evaluation = ""

        # MongoDB에 저장
        collection.insert_one({"app_name": database_name, "user_score": user_score, "user_date": user_date, "user_comments": user_comments, "evaluation": evaluation})
        #print("app_name:{}, user_score:{}, user_date:{}, user_comments:{}, evaluation:{}".format(database_name, user_score, user_date, user_comments, evaluation))

    pass

    # 브라우저 종료
    browser.quit()
