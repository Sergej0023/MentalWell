# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'support.ui'
#
# Created by: PyQt5 ui code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Support(QtWidgets.QDialog):

    def __init__(self, parent_page) -> None:
        super().__init__()
        self.parent_page = parent_page

    def setupUi(self, inspiring):
        inspiring.setObjectName("inspiring")
        inspiring.resize(1000, 800)
        inspiring.setMinimumSize(QtCore.QSize(1000, 800))
        inspiring.setMaximumSize(QtCore.QSize(1000, 800))
        inspiring.setStyleSheet("background-color: rgb(47, 163, 209);")
        self.label = QtWidgets.QLabel(inspiring)
        self.label.setGeometry(QtCore.QRect(370, 70, 221, 191))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(inspiring)
        self.frame.setGeometry(QtCore.QRect(170, 320, 611, 331))
        self.frame.setStyleSheet("background-color: rgb(61, 220, 255);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 451, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.back = QtWidgets.QPushButton(self.frame)
        self.back.setGeometry(QtCore.QRect(140, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
#        self.back.setStyleSheet("QPushButton {\n"
#"    background-color: #fdfcfa;\n"
#"    border: 1px solid #0c253b;\n"
#"    border-radius: 10px;\n"
#"}\n"
#"\n"
#"QPushButton:pressed {\n"
#"    /* Add styling for when the button is pressed */\n"
#"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
#"}")
        #self.back.setObjectName("back")
        self.MainMenu = QtWidgets.QPushButton(self.frame)
        def on_main_menu_clicked():
            if self.parent_page is not None:
                window = QtWidgets.QMainWindow()
                self.parent_page.setupUi(window)
                window.show()
                inspiring.close()
        self.MainMenu.clicked.connect(on_main_menu_clicked)
        self.MainMenu.setGeometry(QtCore.QRect(320, 280, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MainMenu.setFont(font)
        self.MainMenu.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.MainMenu.setObjectName("MainMenu")
        self.support = QtWidgets.QLabel(self.frame)
        self.support.setGeometry(QtCore.QRect(70, 70, 471, 191))
        self.support.setStyleSheet("background-color: rgb(242, 217, 170);")
        self.support.setText("")
        self.support.setObjectName("support")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 90, 401, 151))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(inspiring)
        QtCore.QMetaObject.connectSlotsByName(inspiring)

    def retranslateUi(self, inspiring):
        _translate = QtCore.QCoreApplication.translate
        inspiring.setWindowTitle(_translate("inspiring", "Form"))
        self.label_2.setText(_translate("inspiring", "Support"))
        #self.back.setText(_translate("inspiring", "Back"))
        self.MainMenu.setText(_translate("inspiring", "Main Menu"))
        self.plainTextEdit.setPlainText(_translate("inspiring", "       \n"
"       mustafa.al-bayati0036@stud.hkr.se\n"
"       ryad.hazin0002@stud.hkr.se\n"
"       ali.daoud0056@stud.hkr.se\n"
"       ian.onamu0001@stud.hkr.se\n"
"       sergej.macut0023@stud.hkr.se"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inspiring = QtWidgets.QWidget()
    ui = Ui_Support(None)
    ui.setupUi(inspiring)
    inspiring.show()
    sys.exit(app.exec_())
