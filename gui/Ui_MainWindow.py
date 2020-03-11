# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DriverStyle.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout_2.addWidget(self.graphicsView_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(80, 6, 80, 6)
        self.horizontalLayout_2.setSpacing(200)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.init()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_4.setText(_translate("MainWindow", "开始"))
        self.pushButton_5.setText(_translate("MainWindow", "暂停"))
        self.pushButton_6.setText(_translate("MainWindow", "帮助"))
        
    def init(self):
        img=cv2.imread("drive.jpg")                              #读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)              #转换图像通道
        x = img.shape[1]                                        #获取图像大小
        y = img.shape[0]
        self.zoomscale=1                                        #图片放缩尺度
        frame = QImage(img, x, y, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        self.item=QGraphicsPixmapItem(pix)                      #创建像素图元
        #self.item.setScale(self.zoomscale)
        self.scene=QGraphicsScene()                             #创建场景
        self.scene.addItem(self.item)
        self.graphicsView_2.setScene(self.scene)                        #将场景添加至视图

