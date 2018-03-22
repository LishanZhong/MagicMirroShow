#!/usr/bin/python3
import socket
import time
import json
import threading


class Client(object):
	DEVICEID = 'M83HUF843H'
	host = "cos18.cn"
	# host = "127.0.0.1"
	port = 20223
	# 收到消息时的回调函数
	onMessageCallback = None
	# 连接断开时的回调函数
	onOfflineCallback = None

	def __init__(self):
		self.s = None
		self.data = b''
		self.flag = 1
		self.offlined = False
		self.t1 = threading.Thread(target=self.connect)
		self.t2 = threading.Thread(target=self.heartbeat)
		# 开启线程
		self.t1.start()
		

	def connect(self):
		while True:
			try:
				print('Waiting for connect to server...')
				self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.s.connect((Client.host, Client.port))
				# check in
				checkinBytes = bytes('{"ID":"' + Client.DEVICEID + '","M":"checkin"}', encoding='utf8')
				self.s.sendall(checkinBytes)
				print('Connected to server.')
				# 心跳维护线程
				self.t2.start()
				print(333333)
				self.receive()
				break
			except Exception as e:
				print(e)
				time.sleep(2)

	def send(self, content):
		if self.offlined:
			exit(-1)
		try:
			sayBytes = bytes(content + '\n', encoding='utf8')
			self.s.sendall(sayBytes)
		except Exception as e:
			print(e)
			self.offline()

	# deal with message coming in

	def process(self, msg):
		print("Received:" + msg)
		msg = json.loads(msg)
		if self.onMessageCallback:
			self.onMessageCallback(msg)

	# main while

	def receive(self):
		while not self.offlined:
			try:
				d = self.s.recv(1)
				self.flag = True
			except socket.error as e:
				print("Error receiving data: %s" % e)
				self.flag = False
				# 连接断开了
				self.offline()
				return
			if self.flag:
				if d != b'\n':
					self.data += d
				else:
					msg = str(self.data, encoding='utf-8')
					self.process(msg)
					self.data = b''

	def heartbeat(self):
		while not self.offlined:
			time.sleep(20)
			self.send('{\"M\":\"pong\"}')

	def offline(self):
		if self.offlined:
			exit(-1)
		self.offlined = True
		if self.onOfflineCallback:
			self.onOfflineCallback()
		exit(-1)

	def setCallback(self, _onMessageCallback, _onOfflineCallback):
		self.onMessageCallback = _onMessageCallback
		self.onOfflineCallback = _onOfflineCallback
