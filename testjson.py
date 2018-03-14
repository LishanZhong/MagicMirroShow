import Main
import time


Main.initClient()
time.sleep(5)

#网页的温度
city = Main.weather['city']
wendu = Main.weather['data']['wendu']
shidu = Main.weather['data']['shidu']
pm25 = Main.weather['data']['pm25']
quality = Main.weather['data']['quality']
ganmao = Main.weather['data']['ganmao']
gaowen = Main.weather['data']['forecast'][0]['high'].split(' ')[1]
diwen = Main.weather['data']['forecast'][0]['low'].split(' ')[1]
type = Main.weather['data']['forecast'][0]['type']

#韦总的数据
wendu_w = Main.sensor['T']
shidu_w = Main.sensor['H']
is_rain = Main.sensor['R']

#果果推送的message
print(Main.message)

for msg in Main.message:
    print(msg['title'])