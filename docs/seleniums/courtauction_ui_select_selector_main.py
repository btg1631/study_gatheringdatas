import courtaction_ui_select_selector_subfunction as subfunction
# 기본 function 형식 - 기다림. 불리울 때 기능한다.
def main() :
    try:
        uri="https://www.courtauction.go.kr/"
        browser = subfunction.getBrowserFromURI(uri)    # 업무 코드
        browser = subfunction.clickThingsCourt(browser)
        court_count = subfunction.selectCourts(browser=browser)
        print("court count : {}".format(court_count))
    except:
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        subfunction.quitBrowser(browser=browser)    # try나 except이 끝난 후 무조건 실행 코드
    return 0

if __name__ == "__main__":
    try:
        main()    # 업무 코드
    except:
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass    # try나 except이 끝난 후 무조건 실행 코드