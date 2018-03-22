import Client
import json
import Show
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def onMessage(msg):
	if msg['R'] == 'checkinok':
		print('Connected.')
	if msg['R'] == 'ping':
		Client.sendall(b'{\"M\":\"pong\"}\n')
	if msg['R'] == 'ok':
		print('操作成功完成.')

	if msg['R'] == 'weather':
		weather = json.loads(msg['V'])

		city = weather['city']
		wendu = weather['data']['wendu']
		shidu = weather['data']['shidu']
		pm25 = weather['data']['pm25']
		quality = weather['data']['quality']
		ganmao = weather['data']['ganmao']
		gaowen = weather['data']['forecast'][0]['high'].split(' ')[1]
		diwen = weather['data']['forecast'][0]['low'].split(' ')[1]
		type = weather['data']['forecast'][0]['type']
		notice = weather['data']['forecast'][0]['notice']

		weather_text = city + '   ' + type + '   ' + diwen + '—' + gaowen + ' \nPM2.5: ' + str(
			pm25) + '    ' + quality + '\n' + notice
		pic_url = './images/' + type + '.png'

		mirror.setWeather(weather_text )
		mirror.setWeatherPic(pic_url)
		print('1111'+weather_text)

	if msg['R'] == 'sensor':


		sensor = msg['V']

		wendu_w = msg['V']['T']
		shidu_w = msg['V']['H']
		is_rain_number = msg['V']['R']
		if (int(is_rain_number) > 66):
			is_rain = '无雨'
		else:
			is_rain = '有雨'

		sensor_text = '\n实时温度：' + str(wendu_w) + '℃    湿度：' + str(shidu_w) + '%' + '   ' + is_rain + '\n'
		mirror.setQiXiangZhan(sensor_text)
		print('2222'+ sensor_text)

	if msg['R'] == 'message':
		messages = msg['V']
		for msg in messages:
			mirror.addMessage(msg)
			#print(msg)



def onOffline():
	print("掉线了,尝试重新连接")
	initClient()


def initClient():
	c = Client.Client()

	c.setCallback(onMessage, onOffline)


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mirror = Show.Mirror()  # 创建自定义的窗体类对象
	mirror.show()  # 调用窗口显示
	initClient()
	sys.exit(app.exec_())  # 启动事件循环
	app.exit()

