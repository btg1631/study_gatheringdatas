# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# mongodb 연결
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://192.168.10.245:27017")
database = mongoClient["local"]
collection = database["Egg"]

# - 주소 입력
browser.get("https://www.coupang.com/vp/products/6417848924?itemId=19225484848&vendorItemId=81042389208&sourceType=CATEGORY&categoryId=492681&isAddedCart=")
time.sleep(2)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# 브랜드  div.prod-buy.new-oos-style.not-loyalty-member.eligible-address.dawn-only-product.without-subscribe-buy-type.DISPLAY_0.only-one-delivery.fix-verdor-section-display > a
try:  # 브랜드 
    element_brand = browser.find_element(by=By.CSS_SELECTOR, value="div.prod-buy.new-oos-style.not-loyalty-member.eligible-address.dawn-only-product.without-subscribe-buy-type.DISPLAY_0.only-one-delivery.fix-verdor-section-display > a")
    brand = element_brand.text
except:
    brand = "None"
# 상품명  div.prod-buy-header > h2
try:   # 상품명
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div.prod-buy-header > h2")
    title = element_title.text
except:
    title = "None"
# 원가  span.origin-price
try:   # 원가
    element_price = browser.find_element(by=By.CSS_SELECTOR, value="span.origin-price")
    price = element_price.text
except:
    price = "None"

print("brand:{}, title:{}, price:{}".format(brand, title, price))

# 상품평 클릭  #prod-review-nav-link > span.count
button = browser.find_element(by=By.CSS_SELECTOR, value="#prod-review-nav-link > span.count")
button.click()
time.sleep(2)

pagination_container = browser.find_element(By.CSS_SELECTOR, 'div.sdp-review__article__page.js_reviewArticlePagingContainer')
buttons = pagination_container.find_elements(By.TAG_NAME, 'button')

while True:
    try:
        for j in range(2, 12): 
            # 상품평 전체 section.js_reviewArticleListContainer > article
            element_bundle_review = browser.find_elements(By.CSS_SELECTOR, value="section.js_reviewArticleListContainer > article")
            for i in element_bundle_review:
                # 닉네임  div.sdp-review__article__list__info__user > span
                try:  # 닉네임 
                    element_name = i.find_element(by=By.CSS_SELECTOR, value="div.sdp-review__article__list__info__user > span")
                    name = element_name.text
                except:
                    name = ""
                # 별점  div.sdp-review__article__list__info__product-info__star-gray > div
                try:   # 별점
                    element_rating = i.find_element(by=By.CSS_SELECTOR, value="div.sdp-review__article__list__info__product-info__star-gray > div")
                    rating = element_rating.get_attribute('data-rating')
                except:
                    rating = ""
                # 제목  article > div.sdp-review__article__list__headline
                try:   # 제목
                    element_reviewtitle = i.find_element(by=By.CSS_SELECTOR, value="article > div.sdp-review__article__list__headline")
                    reviewtitle = element_reviewtitle.text
                except:
                    reviewtitle = ""
                # 내용  div.sdp-review__article__list__review.js_reviewArticleContentContainer > div
                try:   # 내용
                    element_comments = i.find_element(by=By.CSS_SELECTOR, value="div.sdp-review__article__list__review.js_reviewArticleContentContainer > div")
                    comments = element_comments.text
                except:
                    comments = ""
                # 만족도  article > div.sdp-review__article__list__survey
                try:   # 만족도
                    element_satisfaction = i.find_element(by=By.CSS_SELECTOR, value="article > div.sdp-review__article__list__survey")
                    satisfaction = element_satisfaction.text
                except:
                    satisfaction = ""

                # MongoDB에 저장
                collection.insert_one({"brand": brand, "title": title, "price": price, "name": name, "rating": rating, "comments": reviewtitle+comments, "satisfaction": satisfaction})
                # print("name:{}, rating:{}, comments:{}".format(name, rating, reviewtitle+comments))

            buttons = browser.find_elements(By.CSS_SELECTOR, 'div.sdp-review__article__page.js_reviewArticlePagingContainer > button')
            buttons[j].click()
            time.sleep(2)
    except:
        break
# 브라우저 종료
browser.quit()
