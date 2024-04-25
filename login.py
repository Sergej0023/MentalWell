# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1000, 800))
        Form.setMaximumSize(QtCore.QSize(1000, 800))
        Form.setWindowTitle("MentalWell")
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(47, 163, 209);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(370, 60, 231, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.signUp = QtWidgets.QPushButton(Form)
        self.signUp.setGeometry(QtCore.QRect(330, 550, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.signUp.setFont(font)
        self.signUp.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.signUp.setAutoDefault(False)
        self.signUp.setDefault(False)
        self.signUp.setFlat(False)
        self.signUp.setObjectName("signUp")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(340, 520, 311, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(340, 590, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.guest = QtWidgets.QPushButton(Form)
        self.guest.setGeometry(QtCore.QRect(330, 620, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.guest.setFont(font)
        self.guest.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.guest.setObjectName("guest")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(290, 279, 391, 201))
        self.frame.setStyleSheet("background-color: rgb(61, 220, 255);\n"
"    border-radius: 10px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.userName = QtWidgets.QLineEdit(self.frame)
        self.userName.setGeometry(QtCore.QRect(40, 20, 311, 31))
        self.userName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"QLineEdit{\n"
"   padding:5px;\n"
"}")
        self.userName.setObjectName("userName")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(40, 70, 311, 31))
        self.password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"QLineEdit{\n"
"   padding:5px;\n"
"}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.frame)
        self.login.setGeometry(QtCore.QRect(40, 120, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setStyleSheet("QPushButton {\n"
"    background-color: #fdfcfa;\n"
"    border: 1px solid #0c253b;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Add styling for when the button is pressed */\n"
"    background-color: #c0c0c0; /* For example, change the background color when pressed */\n"
"}")
        self.login.setObjectName("login")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 371, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.signUp.setText(_translate("Form", "Sign up"))
        self.label_4.setText(_translate("Form", "Don\'t have an account?"))
        self.label_2.setText(_translate("Form", "Or"))
        self.guest.setText(_translate("Form", "Continue as a Guest"))
        self.userName.setPlaceholderText(_translate("Form", "Enter username"))
        self.password.setPlaceholderText(_translate("Form", "Enter password"))
        self.login.setText(_translate("Form", "Login"))
        self.label_3.setText(_translate("Form", "User Agreement"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
