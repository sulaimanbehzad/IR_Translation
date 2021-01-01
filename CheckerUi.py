import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd

afterTranslation = ['ID','POS','Gloss','Gloss_persian','Checked']
fileds = pd.read_csv('translatedCSV.csv',header=None,names=afterTranslation)
fileds = fileds.iloc[1:]
list = fileds.values.tolist()
length = len(list)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.resize(600,300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        f = open("index.txt", "r")
        self.start = int(f.read())
        f.close()
        self.index = self.start

        self.textLabel = QLabel(self.centralwidget)
        self.textLabel.setText("English Text:")
        self.textLabel.move(20, 20)
        self.textLabel2 = QLabel(self.centralwidget)
        self.textLabel2.setText("Translated Text:")
        self.textLabel2.move(20, 50)

        self.textLabel2 = QLabel(self.centralwidget)
        self.textLabel2.setText("items left: " + str((length-1)-self.index))
        self.textLabel2.move(20, 80)

        self.lineEntry = QLineEdit(self.centralwidget)
        self.lineEntry.move(90, 20)
        self.lineEntry.resize(500, 20)
        self.lineEntry.setText(list[self.index][2])

        self.lineEntry2 = QLineEdit(self.centralwidget)
        self.lineEntry2.move(105, 48)
        self.lineEntry2.resize(485, 20)
        self.lineEntry2.setText(list[self.index][3])

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270,100,50,30))
        self.pushButton.clicked.connect(self.changelabeltext)
        self.pushButton.setStyleSheet("background-color: #07ba38")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(265, 150,60, 30))
        self.pushButton2.clicked.connect(self.saveIndex)
        self.pushButton2.setStyleSheet("background-color: #e33529")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(270, 200,50, 30))
        self.pushButton3.clicked.connect(self.changelabeltext2)
        self.pushButton3.setStyleSheet("background-color: #307efc")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translation Checker"))
        self.pushButton.setText(_translate("MainWindow", "Confirm"))
        self.pushButton2.setText(_translate("MainWindow", "save index"))
        self.pushButton3.setText(_translate("MainWindow", "skip"))
    def saveIndex(self):
        f = open("index.txt", "w")
        f.write(str(self.index))
        f.close()
        df = pd.DataFrame(list[self.start:self.index], columns=afterTranslation)
        df.to_csv('checked.csv', mode='a', index=False, encoding='utf-8-sig',header=False)
        sys.exit(app.exec_())
    def changelabeltext(self):
        if self.index < length-1:
            list[self.index][4] = 1
            list[self.index][3] = self.lineEntry2.text()
            self.index = self.index +1
            self.lineEntry.setText(list[self.index][2])
            self.lineEntry2.setText(list[self.index][3])
            self.textLabel2.setText("items left: " + str((length-1) - self.index))
        elif self.index == length-1:
            list[self.index][4] = 1
            list[self.index][3] = self.lineEntry2.text()
            self.index = self.index + 1
            df = pd.DataFrame(list[self.start:self.index-1], columns=afterTranslation)
            df.to_csv('checked.csv',mode='a', index=False, encoding='utf-8-sig')
            sys.exit(app.exec_())
    def changelabeltext2(self):
        if self.index < length-1:
            list[self.index][4] = 0
            list[self.index][3] = self.lineEntry2.text()
            self.index = self.index +1
            self.lineEntry.setText(list[self.index][2])
            self.lineEntry2.setText(list[self.index][3])
            self.textLabel2.setText("items left: " + str((length-1) - self.index))
        elif self.index == length-1:
            list[self.index][4] = 0
            list[self.index][3] = self.lineEntry2.text()
            self.index = self.index + 1
            df = pd.DataFrame(list[self.start:self.index-1], columns=afterTranslation)
            df.to_csv('checked.csv',mode='a', index=False, encoding='utf-8-sig')
            sys.exit(app.exec_())
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())