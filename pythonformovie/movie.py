##################################################################################
import requests
import pandas as pd
# movie 상세정보는 이 주소로@@ http://www.kobis.or.kr/kobisopenapi/webservice/soap/movie
keytemp = 'b150e934e2569d580b00692fc4bf0b22'
import datetime
import urllib.request as ul
import json
from pprint import pprint

ReferenceDate = datetime.datetime(2020,5,31)
fifty=range(0,349,7) #<- 7,14,21,....
parsingDate=[] #<- targetdate에 넣을 list

for i in fifty:
    parsingDate.append(ReferenceDate - datetime.timedelta(days=int(i)))

#확인용 url=f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={keytemp}&targetDt={datetemp}&weekGb=0'

df_temp = pd.read_csv("boxoffice.csv")
code_name = df_temp['2']

# pprint(movie_data.get('movieInfo').get('actors'))
movie_info = [] #<- 영화 정보들을 넣을 빈 list    
for codename in code_name:
    url=f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={keytemp}&movieCd={codename}'
    temp_request = requests.get(url)
    temp_text = temp_request.text
    info_json = json.loads(temp_text)
    temp_allinfo = info_json['movieInfoResult']['movieInfo']
    movie_info.append([temp_allinfo['movieCd'],temp_allinfo['movieNm'],
    temp_allinfo['movieNmOg'],temp_allinfo['movieNmEn'],
    temp_allinfo['audits'],temp_allinfo['openDt'],
    temp_allinfo['prdtYear'],temp_allinfo['showTm'],
    temp_allinfo['genres'],temp_allinfo['directors']])
info_df = pd.DataFrame(movie_info)
print(info_df[:7])
info_df.to_csv("movie.csv",mode = 'w',encoding = 'utf-8',index=False)

# print(movie_info[:3])
# info_df = pd.DataFrame(movie_info)
# #boxoffice = movie_df.columns['rank','old&new','movieCode','movieName','salesAmount','audience']
# info_df.to_csv("movie.csv",mode = 'w',encoding = 'utf-8',index=False)
