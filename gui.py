# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1154, 783)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 1091, 691))
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget1 = QtWidgets.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setMaximumSize(QtCore.QSize(50, 12))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.final_Var = QtWidgets.QLineEdit(self.widget1)
        self.final_Var.setMaximumSize(QtCore.QSize(70, 20))
        self.final_Var.setObjectName("final_Var")
        self.horizontalLayout.addWidget(self.final_Var)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.final_model = QtWidgets.QLineEdit(self.widget1)
        self.final_model.setMinimumSize(QtCore.QSize(20, 20))
        self.final_model.setMaximumSize(QtCore.QSize(1000, 20))
        self.final_model.setObjectName("final_model")
        self.horizontalLayout.addWidget(self.final_model)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(50, 12))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(70, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_4.addWidget(self.lineEdit_12)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_4.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addWidget(self.splitter)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18, 0, QtCore.Qt.AlignTop)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(70, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_5.addWidget(self.label_17, 0, QtCore.Qt.AlignTop)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setMaximumSize(QtCore.QSize(70, 20))
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_5.addWidget(self.lineEdit_13, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_2.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_2.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(20, 20))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(1000, 20))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout_2.addWidget(self.lineEdit_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.Model = QtWidgets.QTreeView(self.widget)
        self.Model.setObjectName("Model")
        self.gridLayout.addWidget(self.Model, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.moreinfo = QtWidgets.QMenuBar(MainWindow)
        self.moreinfo.setGeometry(QtCore.QRect(0, 0, 1154, 23))
        self.moreinfo.setObjectName("moreinfo")
        MainWindow.setMenuBar(self.moreinfo)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "终点数学模型"))
        self.label_2.setText(_translate("MainWindow", "目标参数"))
        self.label_3.setText(_translate("MainWindow", "数学模型"))
        self.pushButton.setText(_translate("MainWindow", "添加"))
        self.label_4.setText(_translate("MainWindow", "过程参数模型"))
        self.label_5.setText(_translate("MainWindow", "过程参数"))
        self.label_15.setText(_translate("MainWindow", "过程计算"))
        self.pushButton_2.setText(_translate("MainWindow", "添加"))
        self.label_16.setText(_translate("MainWindow", "独立变量"))
        self.label_18.setText(_translate("MainWindow", "变量名称"))
        self.label_17.setText(_translate("MainWindow", "关联参数"))
        self.label_7.setText(_translate("MainWindow", "分布类型"))
        self.label_8.setText(_translate("MainWindow", "变量下限"))
        self.label_9.setText(_translate("MainWindow", "变量上限"))
        self.label_10.setText(_translate("MainWindow", "平均值"))
        self.label_11.setText(_translate("MainWindow", "方差"))
        self.label_12.setText(_translate("MainWindow", "Alpha"))
        self.label_13.setText(_translate("MainWindow", "Beta"))
        self.label_14.setText(_translate("MainWindow", "Lambda"))
        self.comboBox.setItemText(0, _translate("MainWindow", "均匀分布"))
        self.comboBox.setItemText(1, _translate("MainWindow", "三角分布"))
        self.comboBox.setItemText(2, _translate("MainWindow", "正态分布"))
        self.comboBox.setItemText(3, _translate("MainWindow", "高斯分布"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Beta分布"))
        self.comboBox.setItemText(5, _translate("MainWindow", "指数分布"))
        self.comboBox.setItemText(6, _translate("MainWindow", "伽马分布"))
        self.comboBox.setItemText(7, _translate("MainWindow", "对数正态分布"))
        self.pushButton_3.setText(_translate("MainWindow", "添加"))

