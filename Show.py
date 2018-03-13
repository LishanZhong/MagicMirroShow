import sys
import datetime
import time
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

    def addText(self, text, p_x, p_y, l_width, l_height, font):
        desktop = QApplication.desktop()  # 获取显示器的大小
        label = QtWidgets.QLabel(self)  # 绑定label到窗口
        label.setText(text)  # 设置label标签的文字内容
        label.setStyleSheet('QWidget{color:white}')
        # label.resize(300, 100)
        label.setGeometry(desktop.width() * p_x, desktop.height() * p_y, l_width, l_height)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
        label.setFont(QFont(font[0], font[1]))
        return label


    def addImage(self, path, p_x, p_y, l_width, l_height):
        desktop = QApplication.desktop()  # 获取显示器的大小
        label = QtWidgets.QLabel(self)
        png = QtGui.QPixmap('./photos/晴.png')
        label.setPixmap(png)
        label.setGeometry(desktop.width() * 0.1, desktop.height() * 0.1, 100, 100)
        return label

    def update_item_data(data):
        """更新内容"""
        label1.setText(data)  # 设置label标签的文字内容




class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring
    def run(self):
        while True:
            now = datetime.datetime.now().strftime('%H:%M:%S')
            self.update_date.emit(str(now))  # 发射信号
            time.sleep(1)

if __name__ == '__main__':
    # pyqt窗口必须在QApplication方法中使用
    app = QtWidgets.QApplication(sys.argv)
    myWin = QtTestWindow()  # 创建自定义的窗体类对象

    now = str(datetime.datetime.now().strftime('%H:%M:%S'))
    label1 = QtTestWindow.addText(myWin, now, 0.6, 0.02, 300, 100, ['华文楷体', 60])

    label2 = QtTestWindow.addText(myWin, '21℃', 0.1, 0.17, 100, 100, ['华文楷体', 40])

    label3 = QtTestWindow.addImage(myWin, './photos/晴.png', 0.1, 0.1, 100, 100)

    update_data_thread = UpdateData()   #界面更新线程
    update_data_thread.update_date.connect(QtTestWindow.update_item_data)  # 链接信号
    update_data_thread.start()


    myWin.show()  # 调用窗口显示
    sys.exit(app.exec_())  # 启动事件循环
    app.exit()
