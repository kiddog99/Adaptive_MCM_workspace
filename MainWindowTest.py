# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Var import Var, MidVar
import random
import numpy as np

class Ui_MainWindow(object):

    MidVarList = {}
    IndpVarList = {}
    FinalVar = MidVar()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 626)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(50, 12))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.FinalVarInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.FinalVarInput.setMaximumSize(QtCore.QSize(70, 20))
        self.FinalVarInput.setObjectName("FinalVarInput")
        self.horizontalLayout.addWidget(self.FinalVarInput)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.FinalVarFormulaInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.FinalVarFormulaInput.setMinimumSize(QtCore.QSize(20, 20))
        self.FinalVarFormulaInput.setMaximumSize(QtCore.QSize(1000, 20))
        self.FinalVarFormulaInput.setObjectName("FinalVarFormulaInput")
        self.horizontalLayout.addWidget(self.FinalVarFormulaInput)
        self.FinalVarButton = QtWidgets.QPushButton(self.layoutWidget)
        self.FinalVarButton.setObjectName("FinalVarButton")
        self.horizontalLayout.addWidget(self.FinalVarButton)
        self.FinalVarDel = QtWidgets.QPushButton(self.layoutWidget)
        self.FinalVarDel.setObjectName("FinalVarDel")
        self.horizontalLayout.addWidget(self.FinalVarDel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setMaximumSize(QtCore.QSize(50, 12))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.MidVarInput = QtWidgets.QLineEdit(self.layoutWidget1)
        self.MidVarInput.setMaximumSize(QtCore.QSize(70, 20))
        self.MidVarInput.setObjectName("MidVarInput")
        self.horizontalLayout_4.addWidget(self.MidVarInput)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.MidVarFormulaImput = QtWidgets.QLineEdit(self.layoutWidget1)
        self.MidVarFormulaImput.setMinimumSize(QtCore.QSize(20, 20))
        self.MidVarFormulaImput.setMaximumSize(QtCore.QSize(1000, 20))
        self.MidVarFormulaImput.setObjectName("MidVarFormulaImput")
        self.horizontalLayout_4.addWidget(self.MidVarFormulaImput)
        self.MidVarButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.MidVarButton.setObjectName("MidVarButton")
        self.horizontalLayout_4.addWidget(self.MidVarButton)
        self.MidVarDel = QtWidgets.QPushButton(self.layoutWidget1)
        self.MidVarDel.setObjectName("MidVarDel")
        self.horizontalLayout_4.addWidget(self.MidVarDel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_4.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addWidget(self.splitter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.IndpVarInput = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IndpVarInput.sizePolicy().hasHeightForWidth())
        self.IndpVarInput.setSizePolicy(sizePolicy)
        self.IndpVarInput.setMinimumSize(QtCore.QSize(10, 10))
        self.IndpVarInput.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarInput.setObjectName("IndpVarInput")
        self.verticalLayout_5.addWidget(self.IndpVarInput)
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.IndpVarRelatianship = QtWidgets.QLineEdit(self.widget)
        self.IndpVarRelatianship.setMinimumSize(QtCore.QSize(20, 20))
        self.IndpVarRelatianship.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarRelatianship.setObjectName("IndpVarRelatianship")
        self.verticalLayout_5.addWidget(self.IndpVarRelatianship)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
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
        self.IndpVarType = QtWidgets.QComboBox(self.widget)
        self.IndpVarType.setObjectName("IndpVarType")
        self.IndpVarType.addItem("")
        self.IndpVarType.addItem("")
        self.IndpVarType.addItem("")
        self.IndpVarType.addItem("")
        self.IndpVarType.addItem("")
        self.IndpVarType.addItem("")
        self.IndpVarType.addItem("")
        self.IndpVarType.addItem("")
        self.verticalLayout_2.addWidget(self.IndpVarType)
        self.IndpVarLow = QtWidgets.QLineEdit(self.widget)
        self.IndpVarLow.setMinimumSize(QtCore.QSize(20, 20))
        self.IndpVarLow.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarLow.setObjectName("IndpVarLow")
        self.verticalLayout_2.addWidget(self.IndpVarLow)
        self.IndpVarHigh = QtWidgets.QLineEdit(self.widget)
        self.IndpVarHigh.setMinimumSize(QtCore.QSize(20, 20))
        self.IndpVarHigh.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarHigh.setObjectName("IndpVarHigh")
        self.verticalLayout_2.addWidget(self.IndpVarHigh)
        self.IndpVarMu = QtWidgets.QLineEdit(self.widget)
        self.IndpVarMu.setMinimumSize(QtCore.QSize(20, 20))
        self.IndpVarMu.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarMu.setObjectName("IndpVarMu")
        self.verticalLayout_2.addWidget(self.IndpVarMu)
        self.IndpVarSigma = QtWidgets.QLineEdit(self.widget)
        self.IndpVarSigma.setMinimumSize(QtCore.QSize(20, 20))
        self.IndpVarSigma.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarSigma.setObjectName("IndpVarSigma")
        self.verticalLayout_2.addWidget(self.IndpVarSigma)
        self.IndpVarAlpha = QtWidgets.QLineEdit(self.widget)
        self.IndpVarAlpha.setMinimumSize(QtCore.QSize(20, 20))
        self.IndpVarAlpha.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarAlpha.setText("")
        self.IndpVarAlpha.setObjectName("IndpVarAlpha")
        self.verticalLayout_2.addWidget(self.IndpVarAlpha)
        self.IndpVarBeta = QtWidgets.QLineEdit(self.widget)
        self.IndpVarBeta.setMinimumSize(QtCore.QSize(20, 20))
        self.IndpVarBeta.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarBeta.setText("")
        self.IndpVarBeta.setObjectName("IndpVarBeta")
        self.verticalLayout_2.addWidget(self.IndpVarBeta)
        self.IndpVarLambd = QtWidgets.QLineEdit(self.widget)
        self.IndpVarLambd.setMinimumSize(QtCore.QSize(20, 20))
        self.IndpVarLambd.setMaximumSize(QtCore.QSize(1000, 20))
        self.IndpVarLambd.setText("")
        self.IndpVarLambd.setObjectName("IndpVarLambd")
        self.verticalLayout_2.addWidget(self.IndpVarLambd)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.IndpVarButton = QtWidgets.QPushButton(self.widget)
        self.IndpVarButton.setObjectName("IndpVarButton")
        self.verticalLayout_6.addWidget(self.IndpVarButton)
        self.IndpVarDel = QtWidgets.QPushButton(self.widget)
        self.IndpVarDel.setObjectName("IndpVarDel")
        self.verticalLayout_6.addWidget(self.IndpVarDel)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.RunCal = QtWidgets.QPushButton(self.widget)
        self.RunCal.setObjectName("RunCal")
        self.verticalLayout_6.addWidget(self.RunCal)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.TextInputFinal = QtWidgets.QTextBrowser(self.widget)
        self.TextInputFinal.setMinimumSize(QtCore.QSize(0, 20))
        self.TextInputFinal.setMaximumSize(QtCore.QSize(16777215, 80))
        self.TextInputFinal.setObjectName("TextInputFinal")
        self.verticalLayout_8.addWidget(self.TextInputFinal)
        self.TextInputMid = QtWidgets.QTextBrowser(self.widget)
        self.TextInputMid.setMaximumSize(QtCore.QSize(16777215, 120))
        self.TextInputMid.setObjectName("TextInputMid")
        self.verticalLayout_8.addWidget(self.TextInputMid)
        self.TextInputIndp = QtWidgets.QTextBrowser(self.widget)
        self.TextInputIndp.setObjectName("TextInputIndp")
        self.verticalLayout_8.addWidget(self.TextInputIndp)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_8)
        self.TextOutput = QtWidgets.QTextBrowser(self.widget)
        self.TextOutput.setObjectName("TextOutput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.TextOutput)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.moreinfo = QtWidgets.QMenuBar(MainWindow)
        self.moreinfo.setGeometry(QtCore.QRect(0, 0, 898, 23))
        self.moreinfo.setObjectName("moreinfo")
        MainWindow.setMenuBar(self.moreinfo)

        self.retranslateUi(MainWindow)
        self.FinalVarButton.clicked.connect(self.FinalVarCreate)
        self.FinalVarDel.clicked.connect(self.FinalVarClean)
        self.MidVarButton.clicked.connect(self.MidVarCreate)
        self.MidVarDel.clicked.connect(self.MidVarClean)
        self.IndpVarButton.clicked.connect(self.IndpVarCreate)
        self.IndpVarDel.clicked.connect(self.IndpVarClean)
        self.RunCal.clicked.connect(self.RunCalculat)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def InputShow(self, pos, msg):
        if pos == "final":
            self.TextInputFinal.setText(msg)
            self.cursor = self.TextInputFinal.textCursor()
            self.TextInputFinal.moveCursor(self.cursor.End)
        elif pos == "mid":
            self.TextInputMid.setText(msg)
            self.cursor = self.TextInputMid.textCursor()
            self.TextInputMid.moveCursor(self.cursor.End)
        elif pos == "indp":
            self.TextInputIndp.setText(msg)
            self.cursor = self.TextInputIndp.textCursor()
            self.TextInputIndp.moveCursor(self.cursor.End)
    def FinalVarCreate(self):
        self.FinalVar.name = self.FinalVarInput.text()
        self.FinalVar.formula = self.FinalVarFormulaInput.text()
        print(self.FinalVar.name, "****", self.FinalVar.formula)
        TempMsg = "终点数学模型：\n" \
               "{0}\n{1}\n" \
               .format(self.FinalVar.name, self.FinalVar.formula)
        self.InputShow("final", TempMsg)
    def FinalVarClean(self):
        self.FinalVar.__init__()
        TempMsg = "终点数学模型：\n" \
                  "{0}\n{1}\n" \
                .format(self.FinalVar.name, self.FinalVar.formula)
        self.InputShow("final", TempMsg)
    def MidVarCreate(self):
        temp = MidVar()
        temp.name = self.MidVarInput.text()
        temp.formula = self.MidVarFormulaImput.text()
        self.MidVarList[str(temp.name)] = temp
        temp = None
        print(self.MidVarList)
        self.InputShow("mid", "过程参数模型：")
        for v in self.MidVarList:
            tempname = v
            tempsample = self.MidVarList[v]
            tempformula = tempsample.formula
            templist = tempsample.VarLi
            msg = "{0} , {1}\n{2}".format(tempname, tempformula, templist)
            print(msg)
            self.TextInputMid.append(msg)
            self.cursor = self.TextInputMid.textCursor()
            self.TextInputMid.moveCursor(self.cursor.End)
    def MidVarClean(self):
        temp = self.MidVarInput.text()
        if temp in self.MidVarList:
            self.MidVarList.pop(temp)
        print(self.MidVarList)
        self.InputShow("mid", "过程参数模型：")
        for v in self.MidVarList:
            tempname = v
            tempsample = self.MidVarList[v]
            tempformula = tempsample.formula
            templist = tempsample.VarLi
            msg = "{0} , {1}\n{2}".format(tempname, tempformula, templist)
            print(msg)
            self.TextInputMid.append(msg)
            self.cursor = self.TextInputMid.textCursor()
            self.TextInputMid.moveCursor(self.cursor.End)
    def IndpVarCreate(self):
        temp = Var()
        temp.name = self.IndpVarInput.text()
        if self.IndpVarRelatianship.text():
            temp.father = self.IndpVarRelatianship.text()
            self.MidVarList[temp.father].VarLi.append(temp.name)
            self.InputShow("mid", "过程参数模型：")
            for v in self.MidVarList:
                tempname = v
                tempsample = self.MidVarList[v]
                tempformula = tempsample.formula
                templist = tempsample.VarLi
                msg = "{0} , {1}\n{2}".format(tempname, tempformula, templist)
                print(msg)
                self.TextInputMid.append(msg)
                self.cursor = self.TextInputMid.textCursor()
                self.TextInputMid.moveCursor(self.cursor.End)
        temp.typ = self.IndpVarType.currentText()
        temp.low = self.IndpVarLow.text()
        temp.high = self.IndpVarHigh.text()
        temp.mu = self.IndpVarMu.text()
        temp.sigma = self.IndpVarSigma.text()
        temp.alpha =self.IndpVarAlpha.text()
        temp.beta = self.IndpVarBeta.text()
        temp.lambd = self.IndpVarLambd.text()
        self.IndpVarList[temp.name] = temp
        temp = None
        print(self.IndpVarList, )
        self.InputShow("indp", "独立变量：")
        for v in self.IndpVarList:
            tempname = v
            tempsample = self.IndpVarList[v]
            temptyp = tempsample.typ
            tempfather = tempsample.father
            msg = "{0} , {1}\n关联过程参数：{2}".format(tempname, temptyp, tempfather)
            print(msg)
            self.TextInputIndp.append(msg)
            self.cursor = self.TextInputIndp.textCursor()
            self.TextInputIndp.moveCursor(self.cursor.End)
    def IndpVarClean(self):
        temp = self.IndpVarInput.text()
        if temp in self.IndpVarList:
            self.IndpVarList.pop(temp)
        print(self.MidVarList)
        self.InputShow("indp", "独立变量：")
        for v in self.IndpVarList:
            tempname = v
            tempsample = self.IndpVarList[v]
            temptyp = tempsample.typ
            tempfather = tempsample.father
            msg = "{0} , {1}\n关联过程参数：{2}".format(tempname, temptyp, tempfather)
            print(msg)
            self.TextInputIndp.append(msg)
            self.cursor = self.TextInputIndp.textCursor()
            self.TextInputIndp.moveCursor(self.cursor.End)
    def checkVar(self, Var):
        if Var.low != None:
            try:
                Var.low = eval(Var.low)
            except:
                pass
        if Var.high != None:
            try:
                Var.high = eval(Var.high)
            except:
                pass
        if Var.mu != None:
            try:
                Var.mu = eval(Var.mu)
            except:
                pass
        if Var.sigma != None:
            try:
                Var.sigma = eval(Var.sigma)
            except:
                pass
        if Var.alpha != None:
            try:
                Var.alpha = eval(Var.alpha)
            except:
                pass
        if Var.beta != None:
            try:
                Var.beta = eval(Var.beta)
            except:
                pass
        if Var.lambd != None:
            try:
                Var.lambd = eval(Var.lambd)
            except:
                pass
    def FinalVarGenerator(self):
        self.FinalVar.tempfor = self.FinalVar.formula
        for indpv in self.IndpVarList:
            self.checkVar(self.IndpVarList[indpv])
            self.IndpVarList[indpv].generator()
            '''self.TextOutput.append("独立变量：{0},{1}".format(indpv,
                                                         self.IndpVarList[indpv].value))
            self.cursor = self.TextOutput.textCursor()
            self.TextOutput.moveCursor(self.cursor.End)'''
            if indpv in self.FinalVar.tempfor:
                self.FinalVar.tempfor = self.FinalVar.tempfor.replace(
                    indpv, str(self.IndpVarList[indpv].value))
        for midVar in self.MidVarList:
            temp = self.MidVarList[midVar]
            temp.generator(self.IndpVarList)
            self.TextOutput.append("过程参数：{0},{1}".format(midVar,
                                                         self.MidVarList[midVar].value))
            self.cursor = self.TextOutput.textCursor()
            self.TextOutput.moveCursor(self.cursor.End)
            if midVar in self.FinalVar.tempfor:
                self.FinalVar.tempfor = self.FinalVar.tempfor.replace(
                    midVar, str(self.MidVarList[midVar].value))
        #print(self.FinalVar.tempfor)
        self.FinalVar.value = eval(self.FinalVar.tempfor)
    def RunCalculat(self):
        self.TextOutput.clear()
        tempResult = []
        mark = 1
        count = 0
        u_y = 0
        y_mean, y_std, y_low, y_high = [], [], [], []
        s_y_mean, s_y_std, s_y_low, s_y_high = 0, 0, 0, 0
        try:
            while mark and count < 1000:
                print("第%s次循环"%count)
                temparr = []
                for i in range(10000):
                    self.FinalVarGenerator()
                    tempResult.append(self.FinalVar.value)
                    temparr.append(self.FinalVar.value)
                    '''if not i+1 % 100:
                        temparr = np.array(tempResult)
                        self.TextOutput.append("前{0}次取样的平均值为{1:.4f}，标准偏差为{2:.4f}".
                            format(i, np.mean(temparr), np.std(temparr)))'''
                print(temparr)
                temparr.sort()
                temparr_np = np.array(temparr)
                y_mean.append(np.mean(temparr_np))
                y_std.append(np.std(temparr_np))
                y_low.append(temparr[499])
                y_high.append(temparr[-500])
                if not count:
                    pass
                else:
                    s_y_mean = 2 * np.std(np.array(y_mean))
                    s_y_std = 2 * np.std(np.array(y_std))
                    s_y_low = 2 * np.std(np.array(y_low))
                    s_y_high = 2 * np.std(np.array(y_high))
                    print("自适应指标：")
                    print(s_y_mean, s_y_std, s_y_low, s_y_high)
                    u_y = np.std(np.array(tempResult))
                    print("处理前的标准差：")
                    print(u_y)
                    u_y = str(np.float(u_y))
                    if "e" in u_y:
                        u_y = u_y.split("e")
                        u_y = 0.5 * 10 ** int(u_y[1])
                    else:
                        if float(u_y) < 1:
                            u_y = 0.005
                        else:
                            u_y = 0.05
                    print(u_y)
                    if s_y_mean < u_y and s_y_std < u_y and s_y_low < u_y and s_y_high < u_y:
                        mark = 0
                count += 1
            temparr = tempResult
            temparr.sort()
            location = int(len(temparr)*0.05)
            tempResult = np.array(tempResult)
            if count == 1000:
                self.TextOutput.append("到达最大迭代次数（10^7）;")
            self.TextOutput.append("最终计算结果：")
            self.TextOutput.append("采样结果平均值为：{0:.4f}\n"
                                   "采样结果标准偏差为：{1:.4f}\n"
                                   "采样结果95%区间为：{2:.4f}~{3:.4f}".format(
                np.mean(tempResult), np.std(tempResult), temparr[location-1], temparr[location*-1]))
            self.cursor = self.TextOutput.textCursor()
            self.TextOutput.moveCursor(self.cursor.End)
        except:
            self.TextOutput.setText("计算过程错误，请检查！")
        print(tempResult)

    def Adapt(self):
        pass





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "终点数学模型"))
        self.label_2.setText(_translate("MainWindow", "目标参数"))
        self.label_3.setText(_translate("MainWindow", "数学模型"))
        self.FinalVarButton.setText(_translate("MainWindow", "添加"))
        self.FinalVarDel.setText(_translate("MainWindow", "清除"))
        self.label_4.setText(_translate("MainWindow", "过程参数模型"))
        self.label_5.setText(_translate("MainWindow", "过程参数"))
        self.label_15.setText(_translate("MainWindow", "过程计算"))
        self.MidVarButton.setText(_translate("MainWindow", "添加"))
        self.MidVarDel.setText(_translate("MainWindow", "清除"))
        self.label_16.setText(_translate("MainWindow", "独立变量"))
        self.label_18.setText(_translate("MainWindow", "变量名称"))
        self.label_19.setText(_translate("MainWindow", "关联过程参数"))
        self.label_7.setText(_translate("MainWindow", "分布类型"))
        self.label_8.setText(_translate("MainWindow", "变量下限"))
        self.label_9.setText(_translate("MainWindow", "变量上限"))
        self.label_10.setText(_translate("MainWindow", "平均值"))
        self.label_11.setText(_translate("MainWindow", "方差"))
        self.label_12.setText(_translate("MainWindow", "Alpha"))
        self.label_13.setText(_translate("MainWindow", "Beta"))
        self.label_14.setText(_translate("MainWindow", "Lambda"))
        self.IndpVarType.setItemText(0, _translate("MainWindow", "均匀分布"))
        self.IndpVarType.setItemText(1, _translate("MainWindow", "三角分布"))
        self.IndpVarType.setItemText(2, _translate("MainWindow", "正态分布"))
        self.IndpVarType.setItemText(3, _translate("MainWindow", "高斯分布"))
        self.IndpVarType.setItemText(4, _translate("MainWindow", "Beta分布"))
        self.IndpVarType.setItemText(5, _translate("MainWindow", "指数分布"))
        self.IndpVarType.setItemText(6, _translate("MainWindow", "伽马分布"))
        self.IndpVarType.setItemText(7, _translate("MainWindow", "对数正态分布"))
        self.IndpVarButton.setText(_translate("MainWindow", "添加"))
        self.IndpVarDel.setText(_translate("MainWindow", "清除"))
        self.RunCal.setText(_translate("MainWindow", "开始采样"))