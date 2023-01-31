# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Background
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox
from sqlite3 import *


class Ui_Student(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1143, 882)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 1121, 841))
        self.widget.setObjectName("widget")
        self.TitleLabel = QtWidgets.QLabel(self.widget)
        self.TitleLabel.setGeometry(QtCore.QRect(400, 50, 321, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("color: rgba(255,255,255,210);")
        self.TitleLabel.setObjectName("TitleLabel")
        self.bg = QtWidgets.QLabel(self.widget)
        self.bg.setGeometry(QtCore.QRect(20, 20, 1081, 811))
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
        self.QuitButton = QtWidgets.QPushButton(self.widget)
        self.QuitButton.setGeometry(QtCore.QRect(700, 740, 181, 61))
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
        self.TableData = QtWidgets.QTableWidget(self.widget)
        self.TableData.setGeometry(QtCore.QRect(160, 170, 811, 341))
        self.TableData.setObjectName("TableData")
        self.TableData.setColumnCount(4)
        self.TableData.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(3, item)
        self.DeleteButton = QtWidgets.QPushButton(self.widget)
        self.DeleteButton.setGeometry(QtCore.QRect(280, 740, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet("QPushButton#DeleteButton{\n"
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
        self.DeleteButton.setObjectName("DeleteButton")
        self.InsertLabel = QtWidgets.QLabel(self.widget)
        self.InsertLabel.setGeometry(QtCore.QRect(80, 580, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.InsertLabel.setFont(font)
        self.InsertLabel.setStyleSheet("color: rgba(255,255,255,210);")
        self.InsertLabel.setObjectName("InsertLabel")
        self.UpdateLabel = QtWidgets.QLabel(self.widget)
        self.UpdateLabel.setGeometry(QtCore.QRect(80, 640, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.UpdateLabel.setFont(font)
        self.UpdateLabel.setStyleSheet("color: rgba(255,255,255,210);")
        self.UpdateLabel.setObjectName("UpdateLabel")
        self.TextStdID_Insert = QtWidgets.QLineEdit(self.widget)
        self.TextStdID_Insert.setGeometry(QtCore.QRect(190, 580, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextStdID_Insert.setFont(font)
        self.TextStdID_Insert.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(105,118,132,255);\n"
                                            "color:rgba(255,255,255,230);\n"
                                            "padding-bottom:7px;")
        self.TextStdID_Insert.setObjectName("TextStdID_Insert")
        self.TextStdName_Insert = QtWidgets.QLineEdit(self.widget)
        self.TextStdName_Insert.setGeometry(QtCore.QRect(380, 580, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextStdName_Insert.setFont(font)
        self.TextStdName_Insert.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                              "border:none;\n"
                                              "border-bottom:2px solid rgba(105,118,132,255);\n"
                                              "color:rgba(255,255,255,230);\n"
                                              "padding-bottom:7px;")
        self.TextStdName_Insert.setObjectName("TextStdName_Insert")
        self.TextStdAddress_Insert = QtWidgets.QLineEdit(self.widget)
        self.TextStdAddress_Insert.setGeometry(QtCore.QRect(570, 580, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextStdAddress_Insert.setFont(font)
        self.TextStdAddress_Insert.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                                 "border:none;\n"
                                                 "border-bottom:2px solid rgba(105,118,132,255);\n"
                                                 "color:rgba(255,255,255,230);\n"
                                                 "padding-bottom:7px;")
        self.TextStdAddress_Insert.setObjectName("TextStdAddress_Insert")
        self.TextClsID_Insert = QtWidgets.QLineEdit(self.widget)
        self.TextClsID_Insert.setGeometry(QtCore.QRect(760, 580, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextClsID_Insert.setFont(font)
        self.TextClsID_Insert.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(105,118,132,255);\n"
                                            "color:rgba(255,255,255,230);\n"
                                            "padding-bottom:7px;")
        self.TextClsID_Insert.setObjectName("TextClsID_Insert")
        self.TextClsID_Update = QtWidgets.QLineEdit(self.widget)
        self.TextClsID_Update.setGeometry(QtCore.QRect(760, 650, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextClsID_Update.setFont(font)
        self.TextClsID_Update.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(105,118,132,255);\n"
                                            "color:rgba(255,255,255,230);\n"
                                            "padding-bottom:7px;")
        self.TextClsID_Update.setObjectName("TextClsID_Update")
        self.TextStdName_Update = QtWidgets.QLineEdit(self.widget)
        self.TextStdName_Update.setGeometry(QtCore.QRect(380, 650, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextStdName_Update.setFont(font)
        self.TextStdName_Update.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                              "border:none;\n"
                                              "border-bottom:2px solid rgba(105,118,132,255);\n"
                                              "color:rgba(255,255,255,230);\n"
                                              "padding-bottom:7px;")
        self.TextStdName_Update.setObjectName("TextStdName_Update")
        self.TextStdID_Update = QtWidgets.QLineEdit(self.widget)
        self.TextStdID_Update.setGeometry(QtCore.QRect(190, 650, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextStdID_Update.setFont(font)
        self.TextStdID_Update.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(105,118,132,255);\n"
                                            "color:rgba(255,255,255,230);\n"
                                            "padding-bottom:7px;")
        self.TextStdID_Update.setObjectName("TextStdID_Update")
        self.TextStdAddress_Update = QtWidgets.QLineEdit(self.widget)
        self.TextStdAddress_Update.setGeometry(QtCore.QRect(570, 650, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.TextStdAddress_Update.setFont(font)
        self.TextStdAddress_Update.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                                 "border:none;\n"
                                                 "border-bottom:2px solid rgba(105,118,132,255);\n"
                                                 "color:rgba(255,255,255,230);\n"
                                                 "padding-bottom:7px;")
        self.TextStdAddress_Update.setObjectName("TextStdAddress_Update")
        self.InsertButton = QtWidgets.QPushButton(self.widget)
        self.InsertButton.setGeometry(QtCore.QRect(950, 570, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.InsertButton.setFont(font)
        self.InsertButton.setStyleSheet("QPushButton#InsertButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
                                        "color: rgba(255,255,255,210);\n"
                                        "border-radius:5px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#InsertButton:hover{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#InsertButton:pressed{\n"
                                        "padding-left:5px;\n"
                                        "padding-top:5px;\n"
                                        "background-color:rgba(105,118,132,200);\n"
                                        "}")
        self.InsertButton.setObjectName("InsertButton")
        self.UpdateButton = QtWidgets.QPushButton(self.widget)
        self.UpdateButton.setGeometry(QtCore.QRect(950, 650, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.UpdateButton.setFont(font)
        self.UpdateButton.setStyleSheet("QPushButton#UpdateButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20,47,78,219), stop:1 rgba(85,98,112,226));\n"
                                        "color: rgba(255,255,255,210);\n"
                                        "border-radius:5px;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#UpdateButton:hover{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40,67,98,219), stop:1 rgba(105,118,132,226));\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton#UpdateButton:pressed{\n"
                                        "padding-left:5px;\n"
                                        "padding-top:5px;\n"
                                        "background-color:rgba(105,118,132,200);\n"
                                        "}")
        self.UpdateButton.setObjectName("UpdateButton")
        self.bg_2.raise_()
        self.bg.raise_()
        self.TitleLabel.raise_()
        self.QuitButton.raise_()
        self.TableData.raise_()
        self.DeleteButton.raise_()
        self.InsertLabel.raise_()
        self.UpdateLabel.raise_()
        self.TextStdID_Insert.raise_()
        self.TextStdName_Insert.raise_()
        self.TextStdAddress_Insert.raise_()
        self.TextClsID_Insert.raise_()
        self.TextClsID_Update.raise_()
        self.TextStdName_Update.raise_()
        self.TextStdID_Update.raise_()
        self.TextStdAddress_Update.raise_()
        self.InsertButton.raise_()
        self.UpdateButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
# ? Connect
        self.QuitButton.clicked.connect(lambda: self.close(Form))
        self.InsertButton.clicked.connect(self.insert)
        self.UpdateButton.clicked.connect(self.update)
        self.DeleteButton.clicked.connect(lambda: self.delete(self.TableData))
        self.loadData()

    def loadData(self):
        connection = connect('StudentManagement.db')
        cur = connection.cursor()
        res = cur.execute("SELECT * FROM Student")

        self.TableData.horizontalHeader().setStretchLastSection(True)
        self.TableData.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

        for row_number, row_data in enumerate(res):
            self.TableData.setRowCount(row_number)
            self.TableData.setColumnCount(len(row_data))
            self.TableData.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.TableData.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.TableData.sortItems(0, QtCore.Qt.AscendingOrder)
        connection.close()

    def insert(self):
        connection = connect('StudentManagement.db')
        cur = connection.cursor()
        query = """select * from Class WHERE ClassID = '{}'""".format(
            self.TextClsID_Insert.text())
        cur.execute(query)
        if len(cur.fetchall()) <= 0:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setStyleSheet(
                "QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(" FOREIGN KEY constraint failed ")
            mess.exec_()
            connection.close()
            self.TextClsID_Insert.clear()
            self.TextStdID_Insert.clear()
            self.TextStdName_Insert.clear()
            self.TextStdAddress_Insert.clear()
            connection.close()
            return
        try:
            connection = connect('StudentManagement.db')
            cur = connection.cursor()
            query = f"""INSERT INTO Student VALUES('{self.TextStdID_Insert.text().upper()}','{self.TextStdName_Insert.text()}',
            '{self.TextStdAddress_Insert.text()}','{self.TextClsID_Insert.text()}')"""
            cur.execute(query)
            connection.commit()
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            mess.setWindowIcon(QtGui.QIcon('information.png'))
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowTitle("Congratulations")
            mess.setText(" Insert Successful ")
            mess.exec_()
            self.loadData()
            connection.close()
        except Error as e:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(str(e))
            mess.exec_()
        self.TextClsID_Insert.clear()
        self.TextStdID_Insert.clear()
        self.TextStdName_Insert.clear()
        self.TextStdAddress_Insert.clear()

    def update(self):
        connection = connect('StudentManagement.db')
        cur = connection.cursor()
        query = """select * from Student WHERE StudentID = '{}'""".format(
            self.TextStdID_Update.text())
        cur.execute(query)
        if len(cur.fetchall()) <= 0:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setStyleSheet(
                "QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(" Student is not exist! ")
            mess.exec_()
            connection.close()
            self.TextClsID_Update.clear()
            self.TextStdID_Update.clear()
            self.TextStdName_Update.clear()
            self.TextStdAddress_Update.clear()
            connection.close()
            return

        try:
            connection = connect('StudentManagement.db')
            cur = connection.cursor()
            query = """select * from Class WHERE ClassID = '{}'""".format(
            self.TextClsID_Update.text())
            cur.execute(query)
            if len(cur.fetchall())<=0:
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Critical)
                mess.setStyleSheet(
                    "QLabel{min-height:30 px; font-size: 24px;}")
                mess.setWindowIcon(QtGui.QIcon('cancel.png'))
                mess.setWindowTitle("Error")
                mess.setText(" FOREIGN KEY constraint failed ")
                mess.exec_()
                self.TextClsID_Update.clear()
                self.TextStdID_Update.clear()
                self.TextStdName_Update.clear()
                self.TextStdAddress_Update.clear()
                return
            query = """UPDATE Student SET StudentName = '{}',StudentAddress = '{}' ,ClassID = '{}' WHERE StudentID = '{}'""".format(
                self.TextStdName_Update.text(), self.TextStdAddress_Update.text(), self.TextClsID_Update.text(), self.TextStdID_Update.text())
            cur.execute(query)
            connection.commit()
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            mess.setWindowIcon(QtGui.QIcon('information.png'))
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowTitle("Congratulations")
            mess.setText(" Update Successful ")
            mess.exec_()
            connection.close()
            self.loadData()
        except Error as e:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(str(e))
            mess.exec_()
        self.TextClsID_Update.clear()
        self.TextStdID_Update.clear()
        self.TextStdName_Update.clear()
        self.TextStdAddress_Update.clear()

    def delete(self, TableData):
        mess = QMessageBox()
        mess.setIcon(QMessageBox.Warning)
        mess.setWindowIcon(QtGui.QIcon('warning.png'))
        mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
        mess.setWindowTitle("Delete Student")
        mess.setText("Are you sure you want to delete this student ?")
        mess.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        question = mess.exec_()

        try:
            if question == QMessageBox.Yes:
                index = TableData.currentRow()
                data = TableData.item(index, 0).text()
                connection = connect('StudentManagement.db')
                cur = connection.cursor()
                cur.execute(
                    "DELETE FROM StudentGrades WHERE StudentID = '{}'".format(data))
                connection.commit()
                cur.execute(
                    "DELETE FROM Student WHERE StudentID = '{}'".format(data))
                connection.commit()
                TableData.removeRow(index)

        except Error as e:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(e)
            mess.exec_()
        pass

    def close(self, Form):
        mess = QMessageBox()
        mess.setIcon(QMessageBox.Warning)
        mess.setWindowTitle("Window Close")
        mess.setWindowIcon(QtGui.QIcon('warning.png'))
        mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
        mess.setText("Are you sure you want to close the windodw ?")
        mess.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        question = mess.exec_()
        if question == QMessageBox.Yes:
            Form.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TitleLabel.setText(_translate("Form", "Student Table"))
        self.QuitButton.setText(_translate("Form", "Quit"))
        item = self.TableData.horizontalHeaderItem(0)
        item.setText(_translate("Form", "StudentID"))
        item = self.TableData.horizontalHeaderItem(1)
        item.setText(_translate("Form", "StudentName"))
        item = self.TableData.horizontalHeaderItem(2)
        item.setText(_translate("Form", "StudentAddress"))
        item = self.TableData.horizontalHeaderItem(3)
        item.setText(_translate("Form", "ClassID"))
        self.DeleteButton.setText(_translate("Form", "Delete"))
        self.InsertLabel.setText(_translate("Form", "Insert"))
        self.UpdateLabel.setText(_translate("Form", "Update"))
        self.TextStdID_Insert.setPlaceholderText(_translate("Form", "StdID"))
        self.TextStdName_Insert.setPlaceholderText(
            _translate("Form", "StdName"))
        self.TextStdAddress_Insert.setPlaceholderText(
            _translate("Form", "StdAddress"))
        self.TextClsID_Insert.setPlaceholderText(_translate("Form", "ClsID"))
        self.TextClsID_Update.setPlaceholderText(_translate("Form", "ClsID"))
        self.TextStdName_Update.setPlaceholderText(
            _translate("Form", "StdName"))
        self.TextStdID_Update.setPlaceholderText(_translate("Form", "StdID"))
        self.TextStdAddress_Update.setPlaceholderText(
            _translate("Form", "StdAddress"))
        self.InsertButton.setText(_translate("Form", "Insert"))
        self.UpdateButton.setText(_translate("Form", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Student()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
