# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - Copy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1143, 722)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 1121, 691))
        self.TitleLabel = QLabel(self.widget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(150, 100, 861, 111))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet(u"color: rgba(255,255,255,210);")
        self.bg = QLabel(self.widget)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(20, 20, 1081, 651))
        self.bg.setStyleSheet(u"\n"
"border-image: url(:/bg/bg.jpg);\n"
"border-radius: 20px;")
        self.bg_2 = QLabel(self.widget)
        self.bg_2.setObjectName(u"bg_2")
        self.bg_2.setGeometry(QRect(20, 20, 1081, 651))
        self.bg_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;")
        self.StudentButton = QPushButton(self.widget)
        self.StudentButton.setObjectName(u"StudentButton")
        self.StudentButton.setGeometry(QRect(270, 270, 231, 61))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.StudentButton.setFont(font1)
        self.StudentButton.setStyleSheet(u"QPushButton#StudentButton{\n"
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
        self.ClassButton = QPushButton(self.widget)
        self.ClassButton.setObjectName(u"ClassButton")
        self.ClassButton.setGeometry(QRect(590, 270, 231, 61))
        self.ClassButton.setFont(font1)
        self.ClassButton.setStyleSheet(u"QPushButton#ClassButton{\n"
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
        self.SubjectButton = QPushButton(self.widget)
        self.SubjectButton.setObjectName(u"SubjectButton")
        self.SubjectButton.setGeometry(QRect(270, 380, 231, 61))
        self.SubjectButton.setFont(font1)
        self.SubjectButton.setStyleSheet(u"QPushButton#SubjectButton{\n"
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
        self.StudentGradesButton = QPushButton(self.widget)
        self.StudentGradesButton.setObjectName(u"StudentGradesButton")
        self.StudentGradesButton.setGeometry(QRect(590, 380, 231, 61))
        self.StudentGradesButton.setFont(font1)
        self.StudentGradesButton.setStyleSheet(u"QPushButton#StudentGradesButton{\n"
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
        self.QuitButton = QPushButton(self.widget)
        self.QuitButton.setObjectName(u"QuitButton")
        self.QuitButton.setGeometry(QRect(460, 530, 181, 61))
        self.QuitButton.setFont(font1)
        self.QuitButton.setStyleSheet(u"QPushButton#QuitButton{\n"
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
        self.bg_2.raise_()
        self.bg.raise_()
        self.TitleLabel.raise_()
        self.StudentButton.raise_()
        self.ClassButton.raise_()
        self.SubjectButton.raise_()
        self.StudentGradesButton.raise_()
        self.QuitButton.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"Student Database Management System", None))
        self.bg.setText("")
        self.bg_2.setText("")
        self.StudentButton.setText(QCoreApplication.translate("Form", u"Student", None))
        self.ClassButton.setText(QCoreApplication.translate("Form", u"Class", None))
        self.SubjectButton.setText(QCoreApplication.translate("Form", u"Subject", None))
        self.StudentGradesButton.setText(QCoreApplication.translate("Form", u"StudentGrades", None))
        self.QuitButton.setText(QCoreApplication.translate("Form", u"Quit", None))
    # retranslateUi

