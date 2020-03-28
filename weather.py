#coding:'utf-8'
import requests,threading

def get_weather(city):
    weather = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    dic_city = weather.json()

    city_data = dic_city.get('data')
    city_weather = []

    if city_data:
        city_forecast = city_data['forecast'][0]
        date = city_forecast.get('date')
        high = city_forecast.get('high')
        low = city_forecast.get('low')
        typec = city_forecast.get('type')
        city_weather.append(city)
        city_weather.append(date)
        city_weather.append(high)
        city_weather.append(low)
        city_weather.append(typec)
        print(city_weather,'\n')
    else:
        print('未获得')
    print()

threads = []
cities = ['北京', '南京', '上海', '深圳', '广州', '杭州', '苏州', '天津', '西安', '成都']
files = range(len(cities))
for i in files:
    t = threading.Thread(target = get_weather,args = (cities[i],))
    threads.append(t)
for i in files:
    threads[i].start()
for i in files:
    threads[i].join()
print('结束获取')

