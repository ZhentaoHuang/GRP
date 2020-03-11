'''
Created on 2020年3月11日
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple PyQt5-tools
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python
@author: Administrator
'''
from PyQt5.QtCore import *
from PyQt5.QtWidgets import * 
from Ui_MainWindow import Ui_MainWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()

    sys.exit(app.exec_())