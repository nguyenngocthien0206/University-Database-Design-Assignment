# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import bg
from MainWindow import *
from Signup import *
from sqlite3 import *


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(590, 416)
        # ? semitransparent :
        Login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Login.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        Login.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(0, 0, 590, 420))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
" background-color:rgba(85, 98, 112, 200);\n"
" color:rgba(255, 255, 255, 200);\n"
" border-radius:5px\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
" padding-left:5px;\n"
" padding-top:5px;\n"
" background-color:rgba(255, 107, 107, 255);\n"
" background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
" background-color:rgba(255, 107, 107, 255);\n"
"}\n"
"\n"
"QPushButton#Register{\n"
" background-color:rgba(85, 98, 112, 200);\n"
" color:rgba(255, 255, 255, 200);\n"
" border-radius:5px\n"
"}\n"
"QPushButton#Register:pressed{\n"
" padding-left:5px;\n"
" padding-top:5px;\n"
" background-color:rgba(255, 107, 107, 255);\n"
" background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#Register:hover{\n"
" background-color:rgba(255, 107, 107, 255);\n"
"}\n"
"QPushButton#ButtonLogin{\n"
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
""

"QPushButton#ButtonSignUp{\n"
" background-color:rgba(85, 98, 112, 200);\n"
" color:rgba(255, 255, 255, 200);\n"
" border-radius:5px\n"
"}\n"
"QPushButton#ButtonSignUp:pressed{\n"
" padding-left:5px;\n"
" padding-top:5px;\n"
" background-color:rgba(255, 107, 107, 255);\n"
" background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#ButtonSignUp:hover{\n"
" background-color:rgba(255, 107, 107, 255);\n"
"}\n"
""
)
        self.widget.setObjectName("widget")
        self.LabelLogin = QtWidgets.QLabel(self.widget)
        self.LabelLogin.setEnabled(True)
        self.LabelLogin.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.LabelLogin.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-radius:10px")
        self.LabelLogin.setText("")
        self.LabelLogin.setObjectName("LabelLogin")
        self.LabelBg = QtWidgets.QLabel(self.widget)
        self.LabelBg.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.LabelBg.setStyleSheet("border-image: url(:/BackgroundSignUp/backgroundLogIn.png);\n"
"border-radius:10px;")
        self.LabelBg.setText("")
        self.LabelBg.setObjectName("LabelBg")
        self.LabelTitle = QtWidgets.QLabel(self.widget)
        self.LabelTitle.setGeometry(QtCore.QRect(330, 70, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.LabelTitle.setFont(font)
        self.LabelTitle.setStyleSheet("color: rgba(0, 0, 0, 200);")
        self.LabelTitle.setObjectName("LabelTitle")
        self.TextUserName = QtWidgets.QLineEdit(self.widget)
        self.TextUserName.setGeometry(QtCore.QRect(330, 140, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TextUserName.setFont(font)
        self.TextUserName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px\n"
"")
        self.TextUserName.setMaxLength(16)
        self.TextUserName.setObjectName("TextUserName")
        self.TextPassword = QtWidgets.QLineEdit(self.widget)
        self.TextPassword.setGeometry(QtCore.QRect(330, 200, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.TextPassword.setFont(font)
        self.TextPassword.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 200);\n"
"color:rgb(0, 0, 0);\n"
"padding-bottom:7px\n"
"")
        self.TextPassword.setMaxLength(32)
        self.TextPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.TextPassword.setObjectName("TextPassword")
        self.ButtonLogin = QtWidgets.QPushButton(self.widget)
        self.ButtonLogin.setGeometry(QtCore.QRect(330, 260, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonLogin.setFont(font)
        self.ButtonLogin.setObjectName("ButtonLogin")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(60, 50, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(60, 70, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(60, 120, 191, 41))
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 220);")
        self.label_7.setObjectName("label_7")
        self.ButtonExit = QtWidgets.QPushButton(self.widget)
        self.ButtonExit.setGeometry(QtCore.QRect(520, 50, 21, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ButtonExit.setFont(font)
        self.ButtonExit.setStyleSheet("color:red;\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}")
        self.ButtonExit.setObjectName("ButtonExit")
        self.ButtonSignUp = QtWidgets.QPushButton(self.widget)
        self.ButtonSignUp.setGeometry(QtCore.QRect(330, 310, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonSignUp.setFont(font)
        self.ButtonSignUp.setStyleSheet("")
        self.ButtonSignUp.setObjectName("ButtonSignUp")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

        self.ButtonLogin.clicked.connect(self.login)
        self.ButtonSignUp.clicked.connect(self.signUpWindow)
        self.ButtonExit.clicked.connect(lambda: self.close(Login))

    def login(self):
        connection = connect('acc.db')
        cur = connection.cursor()
        query = """select Password from Account WHERE UserName = '{}'""".format(
            self.TextUserName.text())
        result = cur.execute(query).fetchall()
        if len(result) > 0:
            password = result[0][0]
            if self.TextPassword.text() == password:
                self.mainWindow()
                self.close(Login)
            else : 
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Critical)
                mess.setWindowIcon(QtGui.QIcon('cancel.png'))
                mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
                mess.setWindowIcon(QtGui.QIcon('cancel.png'))
                mess.setWindowTitle("Error")
                mess.setText(" Sorry, your password is not correct ")
                mess.exec_()

        else :
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(" The user name is not a valid ")
            mess.exec_()
        connection.close()

        
    
    def mainWindow(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def signUpWindow(self):
        self.SignUp = QtWidgets.QMainWindow()
        self.ui = Ui_SignUp()
        self.ui.setupUi(self.SignUp)
        self.SignUp.show()

    def close(self,Form):
        Form.close()
        
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Log In"))
        self.LabelTitle.setText(_translate("Login", "Log In"))
        self.TextUserName.setPlaceholderText(_translate("Login", "User Name"))
        self.TextPassword.setPlaceholderText(_translate("Login", "Password"))
        self.ButtonLogin.setText(_translate("Login", "Log In"))
        self.label_5.setText(_translate("Login", "Student "))
        self.label_6.setText(_translate("Login", "Management System"))
        self.label_7.setText(_translate("Login", "Hi,\n"
"Welcome to Group 2!"))
        self.ButtonExit.setText(_translate("Login", "X"))
        self.ButtonSignUp.setText(_translate("Login", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())