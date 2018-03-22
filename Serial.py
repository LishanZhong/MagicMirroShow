import serial
import time
import threading
class Serial(object):

    # 收到命令时的回调函数
    onCommandCallback = None

    def __init__(self):
        self.port = None
        self.t1 = threading.Thread(target=self.connect)
        self.t1.start()

    def connect(self):
        while True:
            try:
                print('Waiting for connect to serial...')
                self.ser = serial.Serial("/dev/ttyUSB0", 9600)
                print('Cerial Connected.')
                # 心跳维护线程
                self.receive()
                break
            except Exception as e:
                print(e)
                time.sleep(2)


    def setCallback(self, _onCommandCallback):
        self.onCommandCallback = _onCommandCallback

    def receive(self):
        while True:
            # 获得接收缓冲区字符
            count = ser.inWaiting()
            if count != 0:
                # 读取内容并回显
                recv = ser.read(count)
                self.onReceive(recv)
            # 清空接收缓冲区
            ser.flushInput()
            # 必要的软件延时
            time.sleep(0.1)

    def onReceive(self, data):
        print("串口收到:" + msg)
        if self.onCommandCallback:
            self.onCommandCallback(data)

    def close(self):
        if ser != None:
            ser.close()