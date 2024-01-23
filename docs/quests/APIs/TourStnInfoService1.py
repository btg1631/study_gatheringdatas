# from : https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15082033

import requests

url = 'http://apis.data.go.kr/1360000/TourStnInfoService1/getCityTourClmIdx1'
params = { 'serviceKey' : 'n8q0vxEC5P2BMwv1kLcYxS7kTyu6EUP6HDeneaUs4TXvp%2Fm6Xfg5ljzg7A%2FQssE2VA%2BuOdmlkYItOj7tngykpA==',
          'pageNo' : 1,
          'numOfRows' : 10,
          'dataType' : 'json',
          'CURRENT_DATE' : 2018123110,
          'DAY' : 3

}

response =  requests.get(url, params=params)

response.content

import json
contents = json.loads(response.content)

from pymongo import MongoClient
def dbconnect(collection_name) :
    # MongoDB 클라이언트 설정
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["data_go_kr"]
    collection = database[collection_name]
    return collection

collection = dbconnect('TourStnInfoService1')
collection.insert_many(contents['response']['body']['items']['item'])