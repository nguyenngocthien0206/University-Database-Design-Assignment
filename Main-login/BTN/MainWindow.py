
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox
import Background
from StudentWindow import *
from ClassWindow import *
from SubjectWindow import *
from StudentGradesWindow import *

class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.resize(1143, 722)
                Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                Form.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
                Form.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
                self.widget = QtWidgets.QWidget(Form)
                self.widget.setGeometry(QtCore.QRect(10, 20, 1121, 691))
                self.widget.setObjectName("widget")
                self.TitleLabel = QtWidgets.QLabel(self.widget)
                self.TitleLabel.setGeometry(QtCore.QRect(150, 100, 861, 111))
                font = QtGui.QFont()
                font.setPointSize(25)
                font.setBold(True)
                font.setWeight(75)
                self.TitleLabel.setFont(font)
                self.TitleLabel.setStyleSheet("color: rgba(255,255,255,210);")
                self.TitleLabel.setObjectName("TitleLabel")
                self.bg = QtWidgets.QLabel(self.widget)
                self.bg.setGeometry(QtCore.QRect(20, 20, 1081, 651))
                self.bg.setStyleSheet("\n"
        "border-image: url(:/bg/bg.jpg);\n"
        "border-radius: 20px;")
                self.bg.setText("")
                self.bg.setObjectName("bg")
                self.bg_2 = QtWidgets.QLabel(self.widget)
                self.bg_2.setGeometry(QtCore.QRect(20, 20, 1081, 651))
                self.bg_2.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "border-radius: 20px;")
                self.bg_2.setText("")
                self.bg_2.setObjectName("bg_2")
                self.StudentButton = QtWidgets.QPushButton(self.widget)
                self.StudentButton.setGeometry(QtCore.QRect(270, 270, 231, 61))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.StudentButton.setFont(font)
                self.StudentButton.setStyleSheet("QPushButton#StudentButton{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
        "color: rgba(255,255,255,210);\n"
        "border-radius:5px;\n"
        "}\n"
        "\n"
        "QPushButton#StudentButton:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
        "}\n"
        "\n"
        "QPushButton#StudentButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(105,118,132,200);\n"
        "}")
                self.StudentButton.setObjectName("StudentButton")
                self.ClassButton = QtWidgets.QPushButton(self.widget)
                self.ClassButton.setGeometry(QtCore.QRect(590, 270, 231, 61))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.ClassButton.setFont(font)
                self.ClassButton.setStyleSheet("QPushButton#ClassButton{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
        "color: rgba(255,255,255,210);\n"
        "border-radius:5px;\n"
        "}\n"
        "\n"
        "QPushButton#ClassButton:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
        "}\n"
        "\n"
        "QPushButton#ClassButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(105,118,132,200);\n"
        "}")
                self.ClassButton.setObjectName("ClassButton")
                self.SubjectButton = QtWidgets.QPushButton(self.widget)
                self.SubjectButton.setGeometry(QtCore.QRect(270, 380, 231, 61))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.SubjectButton.setFont(font)
                self.SubjectButton.setStyleSheet("QPushButton#SubjectButton{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
        "color: rgba(255,255,255,210);\n"
        "border-radius:5px;\n"
        "}\n"
        "\n"
        "QPushButton#SubjectButton:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
        "}\n"
        "\n"
        "QPushButton#SubjectButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(105,118,132,200);\n"
        "}")
                self.SubjectButton.setObjectName("SubjectButton")
                self.StudentGradesButton = QtWidgets.QPushButton(self.widget)
                self.StudentGradesButton.setGeometry(QtCore.QRect(590, 380, 231, 61))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.StudentGradesButton.setFont(font)
                self.StudentGradesButton.setStyleSheet("QPushButton#StudentGradesButton{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
        "color: rgba(255,255,255,210);\n"
        "border-radius:5px;\n"
        "}\n"
        "\n"
        "QPushButton#StudentGradesButton:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
        "}\n"
        "\n"
        "QPushButton#StudentGradesButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(105,118,132,200);\n"
        "}")
                self.StudentGradesButton.setObjectName("StudentGradesButton")
                self.QuitButton = QtWidgets.QPushButton(self.widget)
                self.QuitButton.setGeometry(QtCore.QRect(460, 530, 181, 61))
                font = QtGui.QFont()
                font.setPointSize(15)
                font.setBold(True)
                font.setWeight(75)
                self.QuitButton.setFont(font)
                self.QuitButton.setStyleSheet("QPushButton#QuitButton{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
        "color: rgba(255,255,255,210);\n"
        "border-radius:5px;\n"
        "}\n"
        "\n"
        "QPushButton#QuitButton:hover{\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
        "}\n"
        "\n"
        "QPushButton#QuitButton:pressed{\n"
        "padding-left:5px;\n"
        "padding-top:5px;\n"
        "background-color:rgba(105,118,132,200);\n"
        "}")
                self.QuitButton.setObjectName("QuitButton")
                self.bg_2.raise_()
                self.bg.raise_()
                self.TitleLabel.raise_()
                self.StudentButton.raise_()
                self.ClassButton.raise_()
                self.SubjectButton.raise_()
                self.StudentGradesButton.raise_()
                self.QuitButton.raise_()

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

                self.QuitButton.clicked.connect(lambda: self.close(Form))
                self.StudentButton.clicked.connect(self.studentWindow)
                self.ClassButton.clicked.connect(self.classWindow)
                self.SubjectButton.clicked.connect(self.subjectWindow)
                self.StudentGradesButton.clicked.connect(self.studentGradesWindow)
                

        def studentWindow(self):
                self.StudentWindow = QtWidgets.QMainWindow()
                self.ui = Ui_Student()
                self.ui.setupUi(self.StudentWindow)
                self.StudentWindow.show()
        
        def classWindow(self):
                self.ClassWindow = QtWidgets.QMainWindow()
                self.ui = Ui_Class()
                self.ui.setupUi(self.ClassWindow)
                self.ClassWindow.show()

        def subjectWindow(self):
                self.SubjectWindow = QtWidgets.QMainWindow()
                self.ui = Ui_Subject()
                self.ui.setupUi(self.SubjectWindow)
                self.SubjectWindow.show()

        def studentGradesWindow(self):
                self.StudentGradesWindow = QtWidgets.QMainWindow()
                self.ui = Ui_Grades()
                self.ui.setupUi(self.StudentGradesWindow)
                self.StudentGradesWindow.show()

        
        def close(self, Form):
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Warning)
                mess.setWindowTitle("Window Close")
                mess.setWindowIcon(QtGui.QIcon('warning.png'))
                mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
                mess.setText("Are you sure you want to close the windodw ?")
                mess.setStandardButtons(QMessageBox.Yes | QMessageBox.No )
                question = mess.exec_()
                if question == QMessageBox.Yes :
                        Form.close()

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Form"))
                self.TitleLabel.setText(_translate("Form", "Student Database Management System"))
                self.StudentButton.setText(_translate("Form", "Student"))
                self.ClassButton.setText(_translate("Form", "Class"))
                self.SubjectButton.setText(_translate("Form", "Subject"))
                self.StudentGradesButton.setText(_translate("Form", "StudentGrades"))
                self.QuitButton.setText(_translate("Form", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
