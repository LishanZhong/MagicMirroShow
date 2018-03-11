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

class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring
    def run(self):
        while True:
            now = datetime.datetime.now().strftime('%H:%M:%S')
            self.update_date.emit(str(now))  # 发射信号
            # print(now)
            time.sleep(1)


if __name__ == '__main__':
    # pyqt窗口必须在QApplication方法中使用
    app = QtWidgets.QApplication(sys.argv)
    myWin = QtTestWindow()  # 创建自定义的窗体类对象

    desktop = QApplication.desktop()  # 获取显示器的大小
    myWin.resize(desktop.width(), desktop.height())  # 重设窗口大小，全屏显示
    myWin.setStyleSheet('QWidget{background-color:black}')
    myWin.setWindowTitle("Hello QT")  # 设置窗口标题

    now = str(datetime.datetime.now().strftime('%H:%M:%S'))

    label1 = QtWidgets.QLabel(myWin)  # 绑定label到窗口
    label1.setText(now)  # 设置label标签的文字内容
    label1.setStyleSheet('QWidget{color:white}')
    label1.resize(100, 100)
    label1.setGeometry(10, 10, 300, 300)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
    label1.setFont(QFont('华文楷体', 60))
    # 添加第二个label
    label2 = QtWidgets.QLabel(myWin)
    label2.setText('21℃')
    label2.setStyleSheet('QWidget{color:white}')
    label2.setGeometry(desktop.width()*0.9, desktop.height()*0.1, 60, 20)
    myWin.show()  # 调用窗口显示

    def update_item_data(data):
        """更新内容"""
        label1.setText(data)  # 设置label标签的文字内容

    # 启动更新线程
    update_data_thread = UpdateData()
    update_data_thread.update_date.connect(update_item_data)  # 链接信号
    update_data_thread.start()
    '''
    # 显示在屏幕中央
    desktop = QApplication.desktop()  # 获取坐标
    x = (desktop.width() - myWin.width()) // 2
    y = (desktop.height() - myWin.height()) // 2
    myWin.move(x, y)  # 移动
    '''
    # 显示

    sys.exit(app.exec_())  # 启动事件循环
    app.exit()