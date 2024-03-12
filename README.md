# ✏️ study_gatheringdatas

## ☑ 사용기술
<img alt="python" src ="https://img.shields.io/badge/PYTHON-3776AB.svg?&style=for-the-badge&logo=PYTHON&logoColor=white"/> <img alt="이미지명" src ="https://img.shields.io/badge/visual studio code-007ACC.svg?&style=for-the-badge&logo=visualstudiocode&logoColor=white"/> <img alt="이미지명" src ="https://img.shields.io/badge/selenium-43B02A.svg?&style=for-the-badge&logo=selenium&logoColor=white"/>


## 💻 셀레니움(Selenium)
- 웹 브라우저를 이용하는 자동화 프로그램인 'Selenium' 이용 데이터 스크래핑

|*|제목|code|설명|비고|
|--|--|--|--|--|
|0|format|[format](./docs/seleniums/formats.py)|selenium 실행 기본 포맷||
|1|find selector|[find selector](./docs/seleniums/emartmall_finds_selector.py)|하나의 element 정보 가져오기|emartmall|
|2|find bundles selector|[find bundles selector](./docs/seleniums/emartmall_find_bundles_selectors.py)|여러 element 정보 가져오기|emartmall|
|3|switch iframe|[switch_iframe](./docs/seleniums/navercafe_switch_iframe.py)|iframe 전환|navercafe|
|4|select selector|[select_selector](./docs/seleniums/ui_select_selector.py)|selectbox 선택||
|5|pagescrolls|[pagescrolls](./docs/seleniums/watcha_pagescrolls_selecctors.py)|페이지 스크롤|watcha|
|6|pagedown|[pagedown_selectors](./docs/seleniums/pagedown_selectors.py)|pagedown, pageup||
|7|login events|[login_events](./docs/seleniums/github_login_events_selector.py)|아이디, 패스워드 입력|github|
|8|modal pagedown|[modal_pagedown](./docs/seleniums/googlestore_NHhealthcare_modal_pagedown_selector.py)|모달창 pagedown|googlestore|


## 💻 API


## 💻 scheduler



## 📚 QUEST
|*|구분|code|설명|비고|
|--|--|--|--|--|
|1|seleniums|[finds](./docs/quests/selenium_coupangmall_finds.py)|특정 카테고리 상품명 출력|coupang mall|
|2|seleniums|[tryexcept](./docs/quests/auction_find_tryexcept_selector.py)|상품제목, 판매원가,변경가격, 배송방법(list), 대처 코드 사용(try~except)|auction|
|3|seleniums|[login](./docs/quests/jobplanet_login_selector.py)|사이트 로그인|jobplanet|
|4|seleniums|[pagination](./docs/quests/coupang_paginations_selectors.py)|변화하는 pagination 개수만큼 넘기기|coupang|
|5|seleniums|[pagescroll](./docs/quests/watcha_comments_pagescrolls_selecctors.py)|각 댓글 mongodb 저장|watcha|
|6|seleniums|[switch_iframe](./docs/quests/11st_switch_iframe.py)|상품 리뷰 전체 스크래핑|11st|
|7|seleniums|[iframe_back](./docs/quests/11st_item_comments_iframe_back.py)|상품상세정보와 댓글 스크래핑(frame 회피)|11st|
|8|seleniums|[ui_select](./docs/quests/courtaction_ui_select.py)|물건상세검색 및 스크래핑-법원소재지 최소 3개, frame 회피|courtaction|



