# from : https://developers.naver.com/docs/serviceapi/search/news/news.md#%EB%89%B4%EC%8A%A4

import requests     # postman app 역할

#  request API 요청
url = "https://openapi.naver.com/v1/search/news"
params = {'query':'인공지능'}
headers = {'X-Naver-Client-Id':'qQBxcjo68I_u39QS_koP'
           , 'X-Naver-Client-Secret':"ISq_J8IyEt"}

response = requests.get(url, params=params, headers=headers)

# response API 응답
response.content

# json을 변수로 변환
import json
contents = json.loads(response.content)
pass