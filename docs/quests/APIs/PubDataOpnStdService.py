import requests

url = "http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo"

params = {'servieKey' : 'Gc7paAk%2Bpu9XSVXtB0YmE6%2FxA9zA4D8Q%2BfrMBjne9OMNaQdfGSppOtS54DkAhAfYt6Lvx8NUr8ct46cuTNMwtg%3D%3D'
          , 'pageNo' : 1 
          , 'numOfRows' : 10
          , 'type' : 'json'
          , 'bidNtceBgnDt' : '201712010000'
          , 'bidNtceEndDt' : '201712312359'}

response = requests.get(url, params =params)

import json
contents = json.loads(response.content)

# 몽고디비에 넣기
from pymongo import MongoClient
mongoclient = MongoClient("mongodb://localhost:27017")
database = mongoclient['data_go_kr']
collection = database['PubDataOpnStdService']

collection.insert_many(contents['response']['body']['items'])