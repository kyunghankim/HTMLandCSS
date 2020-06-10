
import requests
import pandas as pd
#http://www.kobis.or.kr/kobisopenapi/webservice/soap/boxoffice
keytemp = 'b150e934e2569d580b00692fc4bf0b22'
import datetime
import urllib.request as ul
import json

ReferenceDate = datetime.datetime(2020,5,31)
fifty=range(0,349,7) #<- 7,14,21,....
parsingDate=[] #<- targetdate에 넣을 list

for i in fifty:
    parsingDate.append(ReferenceDate - datetime.timedelta(days=int(i)))

movie_lists = [] #<- 영화 정보들을 넣을 빈 list

for time in parsingDate:
    targetdate_temp = time.strftime('%Y%m%d')
    datetemp = int(targetdate_temp)
    url=f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={keytemp}&targetDt={datetemp}&weekGb=0'
    request = requests.get(url)
    results = request.text
    data_json = json.loads(results)
    for movie in data_json['boxOfficeResult']['dailyBoxOfficeList']:
        movie_lists.append([movie['rank'], movie['rankOldAndNew'],
        movie['movieCd'], movie['movieNm'],
        movie['salesAmt'], movie['audiCnt']])

print(movie_lists[:3])
movie_df = pd.DataFrame(movie_lists)
movie_df.to_csv("boxoffice2.csv",mode = 'w',encoding = 'euc-kr',index=False)

