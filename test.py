#https://www.jianshu.com/p/b857771aef80
import sys
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time



class QtTestWindow(QtWidgets.QWidget):
    # QtTestWindow类继承QtWidgets.QWidget类
    def __init__(self):
        # 重载类初始化函数
        super(QtTestWindow, self).__init__()  # super关键字自行百度

    def update_item_data(self, data):
        """更新内容"""
        self.setItem(0, 0, QTableWidgetItem(data))  # 设置表格内容(行， 列) 文字

class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            self.update_date.emit(str(cnt))  # 发射信号
            time.sleep(1)


# pyqt窗口必须在QApplication方法中使用
app = QtWidgets.QApplication(sys.argv)
myWin = QtTestWindow()  # 创建自定义的窗体类对象

update_data_thread = UpdateData()
update_data_thread.update_date.connect(QtTestWindow.update_item_data)  # 链接信号
update_data_thread.start()

myWin.resize(360, 640)  # 重设窗口大小
myWin.setStyleSheet('QWidget{background-color:black}')
myWin.setWindowTitle("Hello QT")  # 设置窗口标题
# 添加第一个label
now = datetime.datetime.now()

label1 = QtWidgets.QLabel(myWin)  # 绑定label到窗口
label1.setText(now.strftime('%H:%M:%S'))  # 设置label标签的文字内容
label1.setStyleSheet('QWidget{color:white}')
label1.resize(100, 100)
label1.setGeometry(10, 10, 300, 300)  # 设置控件相对父窗口位置宽高 参数(x,y,w,h)
label1.setFont(QFont('华文楷体', 60))
# 添加第二个label
label2 = QtWidgets.QLabel(myWin)
label2.setText('21℃')
label2.setStyleSheet('QWidget{color:white}')
label2.setGeometry(300, 10, 60, 20)


myWin.show()  # 调用窗口显示
sys.exit(app.exec_())  # 启动事件循环