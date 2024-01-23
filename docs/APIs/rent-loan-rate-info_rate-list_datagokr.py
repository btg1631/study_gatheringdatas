# 데이터명	한국주택금융공사_전세자금대출 금리 정보
# from : https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests

# url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?serviceKey=BoygPZjC27pxm92hSposjnSob2u36vziS1rzIzxkrL9QxmlhB0SMARwLfNlBE3wrE7nnw34zLmmv0a6amvW4xg%3D%3D&pageNo=1&numOfRows=30&dataType=JSON'
url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

# serviceKey=BoygPZjC27pxm92hSposjnSob2u36vziS1rzIzxkrL9QxmlhB0SMARwLfNlBE3wrE7nnw34zLmmv0a6amvW4xg%3D%3D
# &pageNo=1
# &numOfRows=10
# &dataType=JSON
params = {'serviceKey':'BoygPZjC27pxm92hSposjnSob2u36vziS1rzIzxkrL9QxmlhB0SMARwLfNlBE3wrE7nnw34zLmmv0a6amvW4xg=='
          , 'pageNo' : 1
          , 'numOfRows' : 10
          , 'dataType' : 'JSON'}

# response = requests.get(url)
response = requests.get(url, params=params)

print(response.content)

import json
contents = json.loads(response.content)

type(contents)
# <class 'dict'>
contents['header']
# {'resultCode': '00', 'resultMsg': '정상'}
contents['header']['resultCode']
# '00'
contents['body']['totalCount']
# 18
type(contents['body']['items'])     # 리스트 정보
# <class 'list'>

# mongodb 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["data_go_kr"]

# collection 작업
collection = database['rent-loan-rate-info_rate-list']

# insert 작업 진행
result = collection.insert_many(contents['body']['items'])
pass