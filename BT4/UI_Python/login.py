# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import *


class Ui_LoginUi(object):
    def setupUi(self, LoginUi):
        LoginUi.setObjectName("LoginUi")
        LoginUi.resize(667, 506)
        self.widget = QtWidgets.QWidget(LoginUi)
        self.widget.setGeometry(QtCore.QRect(40, 40, 590, 420))
        self.widget.setStyleSheet("QPushButton#ButtonLogin{\n"
" background-color:rgba(85, 98, 112, 200);\n"
" color:rgba(255, 255, 255, 200);\n"
" border-radius:5px\n"
"}\n"
"QPushButton#ButtonLogin:pressed{\n"
" padding-left:5px;\n"
" padding-top:5px;\n"
" background-color:rgba(255, 107, 107, 255);\n"
" background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonLogin:hover{\n"
" background-color:rgba(255, 107, 107, 255);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.Access = QtWidgets.QLabel(self.widget)
        self.Access.setEnabled(True)
        self.Access.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.Access.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-radius:10px")
        self.Access.setText("")
        self.Access.setObjectName("Access")
        self.Background = QtWidgets.QLabel(self.widget)
        self.Background.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.Background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius:10px;")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setGeometry(QtCore.QRect(330, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.Title.setObjectName("Title")
        self.UserName = QtWidgets.QLineEdit(self.widget)
        self.UserName.setGeometry(QtCore.QRect(330, 140, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px\n"
"")
        self.UserName.setObjectName("UserName")
        self.Password = QtWidgets.QLineEdit(self.widget)
        self.Password.setGeometry(QtCore.QRect(330, 200, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Password.setFont(font)
        self.Password.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px\n"
"")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.ButtonLogin = QtWidgets.QPushButton(self.widget)
        self.ButtonLogin.setGeometry(QtCore.QRect(330, 280, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonLogin.setFont(font)
        self.ButtonLogin.setObjectName("ButtonLogin")
        self.ForgotPass = QtWidgets.QLabel(self.widget)
        self.ForgotPass.setGeometry(QtCore.QRect(330, 330, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.ForgotPass.setFont(font)
        self.ForgotPass.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.ForgotPass.setObjectName("ForgotPass")
        self.SMS = QtWidgets.QLabel(self.widget)
        self.SMS.setGeometry(QtCore.QRect(60, 50, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.SMS.setFont(font)
        self.SMS.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.SMS.setObjectName("SMS")
        self.SMS2 = QtWidgets.QLabel(self.widget)
        self.SMS2.setGeometry(QtCore.QRect(60, 70, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SMS2.setFont(font)
        self.SMS2.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.SMS2.setObjectName("SMS2")
        self.Hello = QtWidgets.QLabel(self.widget)
        self.Hello.setGeometry(QtCore.QRect(60, 130, 191, 41))
        self.Hello.setStyleSheet("color:rgba(255, 255, 255, 220);")
        self.Hello.setObjectName("Hello")
        self.Mountand = QtWidgets.QLabel(self.widget)
        self.Mountand.setGeometry(QtCore.QRect(50, 210, 251, 191))
        font = QtGui.QFont()
        font.setFamily("Mountain")
        font.setPointSize(150)
        self.Mountand.setFont(font)
        self.Mountand.setStyleSheet("color:rgba(255, 107, 107, 255);")
        self.Mountand.setObjectName("Mountand")
        self.ButtonQuit = QtWidgets.QPushButton(self.widget)
        self.ButtonQuit.setGeometry(QtCore.QRect(520, 50, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ButtonQuit.setFont(font)
        self.ButtonQuit.setStyleSheet("color:red;\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}")
        self.ButtonQuit.setObjectName("ButtonQuit")

        self.retranslateUi(LoginUi)
        QtCore.QMetaObject.connectSlotsByName(LoginUi)

        # ? semitransparent :
        LoginUi.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginUi.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        LoginUi.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        # ? connect button:
        self.ButtonQuit.clicked.connect(lambda : self.close(LoginUi))
        self.ButtonLogin.clicked.connect(self.login)

    def close(self,LoginUi):
            LoginUi.hide()

    def login(self):
        name = self.UserName.text()
        password = self.Password.text()
        if name == "admin" and password == "123456":
                self.MainWindow = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.MainWindow)
                self.MainWindow.show()
                LoginUi.hide()
        else:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 20px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(" Password or Username is incorrect ")
            mess.exec_()
        pass


    def retranslateUi(self, LoginUi):
        _translate = QtCore.QCoreApplication.translate
        LoginUi.setWindowTitle(_translate("LoginUi", "Form"))
        self.Title.setText(_translate("LoginUi", "Log In"))
        self.UserName.setPlaceholderText(_translate("LoginUi", "User Name"))
        self.Password.setPlaceholderText(_translate("LoginUi", "Password"))
        self.ButtonLogin.setText(_translate("LoginUi", "Log In"))
        self.ForgotPass.setText(_translate("LoginUi", "Forgot your User Name or Password"))
        self.SMS.setText(_translate("LoginUi", "Student "))
        self.SMS2.setText(_translate("LoginUi", "Management System"))
        self.Hello.setText(_translate("LoginUi", "Hi,\n"
"Welcome to Group 2!"))
        self.Mountand.setText(_translate("LoginUi", "-"))
        self.ButtonQuit.setText(_translate("LoginUi", "X"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginUi = QtWidgets.QWidget()
    ui = Ui_LoginUi()
    ui.setupUi(LoginUi)
    LoginUi.show()
    sys.exit(app.exec_())
