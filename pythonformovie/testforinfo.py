import requests
import pandas as pd
# movie 상세정보는 이 주소로@@ http://www.kobis.or.kr/kobisopenapi/webservice/soap/movie
keytemp = 'b150e934e2569d580b00692fc4bf0b22'
import datetime
import urllib.request as ul
import json
from pprint import pprint

df_temp = pd.read_csv("boxoffice.csv")
code_name = df_temp['2']
movie_info = [] #<- 영화 정보들을 넣을 빈 list

tempcdnm=20179462 #<- 확인용
url=f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={keytemp}&movieCd={tempcdnm}'
temp_request = requests.get(url)
temp_text = temp_request.text
info_json = json.loads(temp_text)
pprint(info_json)
print('-----------------')
# info = info_json['movieInfoResult']
# print(type(info_json['movieInfoResult']['movieInfo']),type(info_json['movieInfoResult']) )
# pprint(info['movieInfo'])
# for i in info:
#     print(info[i])
# print([info['movieCd'],info['movieNm'],
#         info['movieNmOg'],info['movieNmEn'],
#         info['audits'][0]['watchGradeNm'],info['openDt'],info['prdtYear'],
#         info['showTm'],info['genres'],
#         info['actors'][0]['peopleNm']])