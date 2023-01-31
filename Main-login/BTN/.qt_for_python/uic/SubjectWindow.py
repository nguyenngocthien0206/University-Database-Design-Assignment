# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SubjectWindow.ui'
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
        Form.resize(1143, 882)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 1121, 841))
        self.TitleLabel = QLabel(self.widget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(400, 50, 321, 111))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet(u"color: rgba(255,255,255,210);")
        self.bg = QLabel(self.widget)
        self.bg.setObjectName(u"bg")
        self.bg.setGeometry(QRect(20, 20, 1081, 811))
        self.bg.setStyleSheet(u"\n"
"border-image: url(:/bg/bg.jpg);\n"
"border-radius: 20px;")
        self.bg_2 = QLabel(self.widget)
        self.bg_2.setObjectName(u"bg_2")
        self.bg_2.setGeometry(QRect(20, 20, 1081, 651))
        self.bg_2.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(76, 76, 76, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 20px;")
        self.QuitButton = QPushButton(self.widget)
        self.QuitButton.setObjectName(u"QuitButton")
        self.QuitButton.setGeometry(QRect(700, 740, 181, 61))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
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
        self.TableData = QTableWidget(self.widget)
        if (self.TableData.columnCount() < 3):
            self.TableData.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.TableData.setObjectName(u"TableData")
        self.TableData.setGeometry(QRect(160, 170, 811, 341))
        self.DeleteButton = QPushButton(self.widget)
        self.DeleteButton.setObjectName(u"DeleteButton")
        self.DeleteButton.setGeometry(QRect(280, 740, 181, 61))
        self.DeleteButton.setFont(font1)
        self.DeleteButton.setStyleSheet(u"QPushButton#DeleteButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
"color: rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#DeleteButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
"}\n"
"\n"
"QPushButton#DeleteButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(105,118,132,200);\n"
"}")
        self.InsertLabel = QLabel(self.widget)
        self.InsertLabel.setObjectName(u"InsertLabel")
        self.InsertLabel.setGeometry(QRect(170, 580, 81, 41))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        self.InsertLabel.setFont(font2)
        self.InsertLabel.setStyleSheet(u"color: rgba(255,255,255,210);")
        self.UpdateLabel = QLabel(self.widget)
        self.UpdateLabel.setObjectName(u"UpdateLabel")
        self.UpdateLabel.setGeometry(QRect(170, 650, 101, 41))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.UpdateLabel.setFont(font3)
        self.UpdateLabel.setStyleSheet(u"color: rgba(255,255,255,210);")
        self.TextSbjID_Insert = QLineEdit(self.widget)
        self.TextSbjID_Insert.setObjectName(u"TextSbjID_Insert")
        self.TextSbjID_Insert.setGeometry(QRect(280, 580, 171, 41))
        self.TextSbjID_Insert.setFont(font1)
        self.TextSbjID_Insert.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.TextSbjName_Insert = QLineEdit(self.widget)
        self.TextSbjName_Insert.setObjectName(u"TextSbjName_Insert")
        self.TextSbjName_Insert.setGeometry(QRect(470, 580, 171, 41))
        self.TextSbjName_Insert.setFont(font1)
        self.TextSbjName_Insert.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.TextSbjUnit_Insert = QLineEdit(self.widget)
        self.TextSbjUnit_Insert.setObjectName(u"TextSbjUnit_Insert")
        self.TextSbjUnit_Insert.setGeometry(QRect(660, 580, 171, 41))
        self.TextSbjUnit_Insert.setFont(font1)
        self.TextSbjUnit_Insert.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.TextSbjName_Update = QLineEdit(self.widget)
        self.TextSbjName_Update.setObjectName(u"TextSbjName_Update")
        self.TextSbjName_Update.setGeometry(QRect(470, 650, 171, 41))
        self.TextSbjName_Update.setFont(font1)
        self.TextSbjName_Update.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.TextSbjID_Update = QLineEdit(self.widget)
        self.TextSbjID_Update.setObjectName(u"TextSbjID_Update")
        self.TextSbjID_Update.setGeometry(QRect(280, 650, 171, 41))
        self.TextSbjID_Update.setFont(font1)
        self.TextSbjID_Update.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.TextSbjUnit_Update = QLineEdit(self.widget)
        self.TextSbjUnit_Update.setObjectName(u"TextSbjUnit_Update")
        self.TextSbjUnit_Update.setGeometry(QRect(660, 650, 171, 41))
        self.TextSbjUnit_Update.setFont(font1)
        self.TextSbjUnit_Update.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.bg_2.raise_()
        self.bg.raise_()
        self.TitleLabel.raise_()
        self.QuitButton.raise_()
        self.TableData.raise_()
        self.DeleteButton.raise_()
        self.InsertLabel.raise_()
        self.UpdateLabel.raise_()
        self.TextSbjID_Insert.raise_()
        self.TextSbjName_Insert.raise_()
        self.TextSbjUnit_Insert.raise_()
        self.TextSbjName_Update.raise_()
        self.TextSbjID_Update.raise_()
        self.TextSbjUnit_Update.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.TitleLabel.setText(QCoreApplication.translate("Form", u"Subject Table", None))
        self.bg.setText("")
        self.bg_2.setText("")
        self.QuitButton.setText(QCoreApplication.translate("Form", u"Quit", None))
        ___qtablewidgetitem = self.TableData.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"SubjectID", None));
        ___qtablewidgetitem1 = self.TableData.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"SubjectName", None));
        ___qtablewidgetitem2 = self.TableData.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Units", None));
        self.DeleteButton.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.InsertLabel.setText(QCoreApplication.translate("Form", u"Insert", None))
        self.UpdateLabel.setText(QCoreApplication.translate("Form", u"Update", None))
        self.TextSbjID_Insert.setPlaceholderText(QCoreApplication.translate("Form", u"SbjID", None))
        self.TextSbjName_Insert.setPlaceholderText(QCoreApplication.translate("Form", u"SbjName", None))
        self.TextSbjUnit_Insert.setPlaceholderText(QCoreApplication.translate("Form", u"Unit", None))
        self.TextSbjName_Update.setPlaceholderText(QCoreApplication.translate("Form", u"SbjName", None))
        self.TextSbjID_Update.setPlaceholderText(QCoreApplication.translate("Form", u"SbjID", None))
        self.TextSbjUnit_Update.setPlaceholderText(QCoreApplication.translate("Form", u"Unit", None))
    # retranslateUi

