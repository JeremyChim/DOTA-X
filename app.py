"""
-*- coding: utf-8 -*-
Time: 2023/10/30 17:09
Auth: Jeremy.Chim
File: app.py
IDE: PyCharm
GitHub: https://github.com/JeremyChim/DOTA-X
"""


import sys
import os

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from InterFace import Ui_Form

from InitConf import InitConf


def openQss(qssFile) -> str:
    """Open Qss File."""
    with open(qssFile) as file:
        qssStyleSheet = file.read()
    return qssStyleSheet


def defaultDataFunc(DataFile: str) -> str:
    """
    Default Data File.
    """
    with open(DataFile) as file:
        defaultData = file.read()
    return defaultData


class Window(QWidget, Ui_Form):
    """
    init MainWindow.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initWindow()
        self.initButton()
        self.initScrollbar()

    def initWindow(self):
        """
        init MainWindow.
        """
        self.setWindowTitle('DOTA-X')
        self.setWindowIcon(QIcon('app.ico'))
        self.ChangeStyle('qss/Ubuntu.qss')

    def initButton(self):
        """
        init Button.
        """
        self.pushButton_Config.clicked.connect(lambda: os.startfile(r'config.xlsx'))
        self.pushButton_Hero.clicked.connect(lambda: self.funcScript(1))
        self.pushButton_Ability.clicked.connect(lambda: self.funcScript(2))
        self.pushButton_Unit.clicked.connect(lambda: self.funcScript(3))
        self.checkBox.clicked.connect(lambda: self.windowTop())
        self.comboBox.addItems(['AMOLED', 'Aqua',
                                'ConsoleStyle', 'ElegantDark',
                                'MacOS', 'ManjaroMix',
                                'ManjaroMix', 'MaterialDark',
                                'NeonButtons', 'Ubuntu',
                                'Window'])
        self.comboBox.setCurrentText('Ubuntu')
        self.comboBox.activated.connect(lambda: self.ChangeStyleCB())

    def initScrollbar(self):
        """
        init Scrollbar.
        """
        old = self.plainTextEdit_OldData
        new = self.plainTextEdit_NewData
        new.setVerticalScrollBar(old.verticalScrollBar())
        new.setHorizontalScrollBar(old.horizontalScrollBar())

    def windowTop(self):
        """
        Window Stays On TopHint.
        """
        if self.checkBox.isChecked() is True:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
            self.setVisible(True)
        else:
            self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, False)
            self.setVisible(True)

    def funcScript(self, script):
        """
        Function Script.
        """
        oldData = self.plainTextEdit_OldData.toPlainText()
        match script:
            case 1:
                if not oldData:
                    oldData = defaultDataFunc('DefaultDataHero.txt')
                    self.plainTextEdit_OldData.setPlainText(oldData)
                newData = InitConf().scriptHero(oldData)
            case 2:
                if not oldData:
                    oldData = defaultDataFunc('DefaultDataAbility.txt')
                    self.plainTextEdit_OldData.setPlainText(oldData)
                newData = InitConf().scriptAbility(oldData)
            case 3:
                if not oldData:
                    oldData = defaultDataFunc('DefaultDataUnit.txt')
                    self.plainTextEdit_OldData.setPlainText(oldData)
                newData = InitConf().scriptUnit(oldData)
            case _:
                newData = oldData
        self.plainTextEdit_NewData.setPlainText(newData)

    def ChangeStyleCB(self):
        """Change Style of comboBox."""
        style = self.comboBox.currentText()
        qssFile = f'qss/{style}.qss'
        self.ChangeStyle(qssFile)

    def ChangeStyle(self, qssFile):
        """Change Style."""
        Style = openQss(qssFile)
        self.setStyleSheet(Style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec()
