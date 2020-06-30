import json
from datetime import datetime
import urllib.request as ul
from whereRU import get_local

now = datetime.now()
now_hour = int(now.strftime('%H'))
now_min = int(now.strftime('%M'))

def get_sky_info(data):
    pass

def get_base_time(hour, minute):
    hour = int(hour)
    if minute< 40:
        hour = hour - 1
        if hour < 0:
            hour = 23
    if hour < 10:
        temp_hour = '0'+str(hour)
    else:
        temp_hour = str(hour)
           

    return temp_hour + '00'


service_key = '8WBQFbvaR1oBFwQ5sQ%2FrvuVzYrWGcjYYiTMl69cFmxTqZf587y8gUI0z71gOoqxHDyiiDVv4u%2B5Kct%2F24m27Pg%3D%3D'
num_of_rows = '8'
page_no = '1'
base_date = now.strftime('%Y%m%d')

if now_hour == 0 and now_min < 40:
    base_date = str(int(base_date-1))
base_time = get_base_time(now_hour, now_min)
nx, ny = get_local()
#print(now_hour)
#print(now_min)
print("basedate = "+base_date)
print("basetime = "+base_time)

api_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst?serviceKey={}&numOfRows={}&pageNo={}&dataType=JSON&base_date={}&base_time={}&nx={}&ny={}'.format(service_key, num_of_rows, page_no, base_date, base_time, nx, ny)
#print(api_url)
request = ul.Request(api_url)
response = ul.urlopen(request)
responseData = response.read()
rD = json.loads(responseData)
weather_info = rD['response']['body']['items']['item']

time_weather=[]
category = {'T1H':'기온','RN1':'1시간 강수량','UUU':'동서바람성분','VVV':'남북바람성분','REH':'습도','PTY':'강수형태','VEC':'풍향','WSD':'풍속'}
cate_decode = {'기온':'','1시간 강수량':'','동서바람성분':'','남북바람성분':'','습도':'','강수형태':'','풍향':'','풍속':''}
#PTY_info = {'0':'none','1':'rain','2':'rain/snow','3':'snow','4':'shower'}

def get_category(a):
    category = weather_info[a]['category']
    return category

def get_value(a):
    value = weather_info[a]['obsrValue']
    return value

for i in range(8):
    weather_category = get_category(i)
    weather_value = get_value(i)
    cate_decode[category[weather_category]] = weather_value

if cate_decode['강수형태'] == '0':
    cate_decode['강수형태'] = 'None'
elif cate_decode['강수형태'] == '1':
    cate_decode['강수형태'] = '비'
elif cate_decode['강수형태'] == '2':
    cate_decode['강수형태'] = '비/눈'
elif cate_decode['강수형태'] == '3':
    cate_decode['강수형태'] = '눈'
elif cate_decode['강수형태'] == '4':
    cate_decode['강수형태'] = '소나기'

rescode = response.getcode()


#print(rescode)  #요청/응답 상태코드 : 200이면 정상
#print(weather_info)
print(" ")
for key, value in cate_decode.items():
    print(key, value)

