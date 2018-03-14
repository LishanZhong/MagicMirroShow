import sys
import datetime
import time
import Main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QtTestWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QtTestWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)     #设置上面菜单栏无边框
        desktop = QApplication.desktop()  # 获取显示器的大小
        self.resize(desktop.width(), desktop.height())  # 重设窗口大小，全屏显示
        self.setStyleSheet('QWidget{background-color:black}')
        self.setWindowTitle("Hello C1024")  # 设置窗口标题


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

    def update_item_data(data1,data2,data3,data4,data5):
        """更新内容"""
        label1.setText(data1)  # 设置label标签的文字内容

        label2.setText(data2)

        png = QtGui.QPixmap(data3)
        label3.setPixmap(png)

        label4.setText(data4)

        label5.setText(data5)




class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str,str,str,str,str)  # pyqt5 支持python3的str，没有Qstring
    def run(self):
        while True:
            # 网页的温度
            city = Main.weather['city']
            wendu = Main.weather['data']['wendu']
            shidu = Main.weather['data']['shidu']
            pm25 = Main.weather['data']['pm25']
            quality = Main.weather['data']['quality']
            ganmao = Main.weather['data']['ganmao']
            gaowen = Main.weather['data']['forecast'][0]['high'].split(' ')[1]
            diwen = Main.weather['data']['forecast'][0]['low'].split(' ')[1]
            type = Main.weather['data']['forecast'][0]['type']

            # 韦总的数据
            wendu_w = Main.sensor['T']
            shidu_w = Main.sensor['H']
            is_rain = Main.sensor['R']

            # 果果推送的message
            msg = Main.message

            L1 = str(datetime.datetime.now().strftime('%H:%M:%S'))
            L2 = city +'   ' + type +  '   ' + diwen + '—' + gaowen + ' \nPM2.5: ' + str(pm25) + '    ' + quality + '\n实时温度：' + str(wendu_w) + '℃    湿度：'+str(shidu_w) + '%\n' + ganmao
            L3 = './images/'+type+'.png'
            L4 = '主题:' + msg[0]['title'] + '\n时间：' + msg[0]['updated_at'] + '\n内容：' + msg[0]['content']
            L5 = '主题:' + msg[1]['title'] + '\n时间：' + msg[1]['updated_at'] + '\n内容：' + msg[1]['content']

            self.update_date.emit(L1, L2, L3, L4, L5)  # 发射信号

            time.sleep(1)

if __name__ == '__main__':
    Main.initClient()
    time.sleep(3)
    # pyqt窗口必须在QApplication方法中使用
    app = QtWidgets.QApplication(sys.argv)
    myWin = QtTestWindow()  # 创建自定义的窗体类对象

    now = str(datetime.datetime.now().strftime('%H:%M:%S'))
    label1 = QtTestWindow.addText(myWin, now, 0.6, 0.02, 0.4, 0.15, ['华文楷体', 60])

    label2 = QtTestWindow.addText(myWin, '--', 0.001, 0.17, 1, 0.1, ['华文楷体', 15])

    label3 = QtTestWindow.addImage(myWin, '', 0.1, 0.1, 100, 100)

    label4 = QtTestWindow.addText(myWin, '', 0.001, 0.7, 1, 0.1, ['华文楷体', 20])
    label5 = QtTestWindow.addText(myWin, '', 0.001, 0.85, 1, 0.1, ['华文楷体', 20])

    update_data_thread = UpdateData()   #界面更新线程
    update_data_thread.update_date.connect(QtTestWindow.update_item_data)  # 链接信号
    update_data_thread.start()

    myWin.show()  # 调用窗口显示

    sys.exit(app.exec_())  # 启动事件循环
    app.exit()
