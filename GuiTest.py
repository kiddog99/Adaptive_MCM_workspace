from MainWindowTest import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np
import sys, random

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec_()