# from : https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md#%EC%B0%B8%EA%B3%A0-%EC%82%AC%ED%95%AD

import requests     # postman app 역할

#  request API 요청
url = "https://openapi.naver.com/v1/datalab/shopping/categories"
headers = {'X-Naver-Client-Id':'FgRcI134o3JcUtBEYT8v'
           , 'X-Naver-Client-Secret':"kdq7Y9wHFh"}
bodys = {
  "startDate": "2023-08-01",
  "endDate": "2023-09-30",
  "timeUnit": "month",
  "category": [
      {"name": "패션의류", "param": [ "50000000"]},
      {"name": "화장품/미용", "param": [ "50000002"]}
  ],
  "device": "pc",
  "gender": "f",
  "ages": [ "20",  "30"]
}
response = requests.post(url, headers=headers, json=bodys)

# response API 응답
response.content

# json을 변수로 변환
import json
contents = json.loads(response.content)
pass