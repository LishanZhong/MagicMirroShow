import sys
import datetime
import time
import Main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Mirror(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Mirror, self).__init__()
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 设置上面菜单栏无边框
		desktop = QApplication.desktop()  # 获取显示器的大小
		self.resize(desktop.width(), desktop.height())  # 重设窗口大小，全屏显示
		self.setStyleSheet('QWidget{background-color:black}')
		self.setWindowTitle("Hello C1024")  # 设置窗口标题
		self.labelTime = self.addText('Hello', 0.6, 0.02, 0.4, 0.15, ['华文楷体', 60])

		self.labelWeather = self.addText('Loading...', 0.001, 0.17, 1, 0.1, ['华文楷体', 15])

		self.labelWeatherPic = self.addImage('', 0.1, 0.1, 100, 100)
		
		self.QiXiangZhan = self.addText('', 0.001, 0.25, 1, 0.04, ['华文楷体', 15])

		self.label4 = self.addText('', 0.001, 0.7, 1, 0.1, ['华文楷体', 20])
		self.label5 = self.addText('', 0.001, 0.85, 1, 0.1, ['华文楷体', 20])

		
		self.update_data_thread = UpdateData()  # 界面更新线程(仅时间)
		self.update_data_thread.update_date.connect(self.update_item_data)  # 链接信号
		self.update_data_thread.start()
		
		self.msgList = [['', ''], ['李果果', '第二帅']]


	def addText(self, text, p_x, p_y, s_x, s_y, font):
		desktop = QApplication.desktop()  # 获取显示器的大小
		label = QtWidgets.QLabel(self)  # 绑定label到窗口
		label.setText(text)  # 设置label标签的文字内容
		label.setStyleSheet('QWidget{color:white}')
		label.setGeometry(desktop.width() * p_x, desktop.height() * p_y, \
						  desktop.width() * s_x, desktop.height() * s_y)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
		label.setFont(QFont(font[0], font[1]))
		return label


	def addImage(self, path, p_x, p_y, l_width, l_height):
		desktop = QApplication.desktop()  # 获取显示器的大小
		label = QtWidgets.QLabel(self)
		png = QtGui.QPixmap('./photos/晴.png')
		label.setPixmap(png)
		label.setGeometry(desktop.width() * p_x, desktop.height() * p_x, 100, 100)
		return label


	def setWeatherPic(self, pic_url):
		png = QtGui.QPixmap(pic_url)  # 设置天气图标
		self.labelWeatherPic.setPixmap(png)


	def setWeather(self, text):
		self.labelWeather.setText(text)  # 设置天气标签的文字内容
		
	def setQiXiangZhan(self, text):
		self.QiXiangZhan.setText(text)  # 设置气象站标签的文字内容


	def addMessage(self, message):
		print('Add ' + str(message) + '\n')
		self.msgList.append([message['title'], message['content']])
		self.label4.setText('主题:' + self.msgList[-1][0] + '\n内容：' + self.msgList[-1][1])
		self.label5.setText('主题:' + self.msgList[-2][0] + '\n内容：' + self.msgList[-2][1])

	def update_item_data(self, time):
		"""更新内容"""
		self.labelTime.setText(time)  # 设置label标签的文字内容


class UpdateData(QThread):
	"""更新数据类"""
	update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring

	def run(self):
		while True:
			timeStr = str(datetime.datetime.now().strftime('%H:%M:%S'))
			self.update_date.emit(timeStr)  # 发射信号
			time.sleep(1)


