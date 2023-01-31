
from os import curdir
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import BackGround
from InsertWindow import *
from QueryWindow import Ui_QueryWindow
from UpdateWindow import *
from FindWindow import *
from sqlite3 import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1283, 868)
        self.Window = QtWidgets.QWidget(MainWindow)
        self.Window.setObjectName("Window")
        self.BackGroundLabel = QtWidgets.QLabel(self.Window)
        self.BackGroundLabel.setEnabled(False)
        self.BackGroundLabel.setGeometry(QtCore.QRect(0, 0, 1281, 811))
        self.BackGroundLabel.setStyleSheet(
            "background : url(:/Main/background.png)")
        self.BackGroundLabel.setText("")
        self.BackGroundLabel.setObjectName("BackGroundLabel")
        self.FrameTableWidget = QtWidgets.QFrame(self.Window)
        self.FrameTableWidget.setGeometry(QtCore.QRect(350, 180, 900, 601))
        self.FrameTableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameTableWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameTableWidget.setObjectName("FrameTableWidget")
        self.comboBox = QtWidgets.QComboBox(self.FrameTableWidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 10, 850, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.ButtonDelete = QtWidgets.QPushButton(self.FrameTableWidget)
        self.ButtonDelete.setGeometry(QtCore.QRect(220, 540, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonDelete.setFont(font)
        self.ButtonDelete.setAutoFillBackground(True)
        self.ButtonDelete.setObjectName("ButtonDelete")
        self.ButtonClear = QtWidgets.QPushButton(self.FrameTableWidget)
        self.ButtonClear.setGeometry(QtCore.QRect(490, 540, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonClear.setFont(font)
        self.ButtonClear.setAutoFillBackground(True)
        self.ButtonClear.setObjectName("ButtonClear")
        self.TableData = QtWidgets.QTableWidget(self.FrameTableWidget)
        self.TableData.setGeometry(QtCore.QRect(0, 100, 850, 400))
        self.TableData.setObjectName("TableData")
        self.Title = QtWidgets.QLabel(self.Window)
        self.Title.setGeometry(QtCore.QRect(25, 10, 1200, 150))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setWhatsThis("")
        self.Title.setAutoFillBackground(False)
        self.Title.setStyleSheet("color: rgb(255, 255, 255);")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.FrameButton = QtWidgets.QFrame(self.Window)
        self.FrameButton.setGeometry(QtCore.QRect(30, 180, 281, 601))
        self.FrameButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameButton.setObjectName("FrameButton")
        self.LabelClass = QtWidgets.QLabel(self.FrameButton)
        self.LabelClass.setGeometry(QtCore.QRect(60, 10, 150, 50))
        self.LabelClass.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LabelClass.setFont(font)
        self.LabelClass.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelClass.setObjectName("LabelClass")
        self.ButtonFind = QtWidgets.QPushButton(self.FrameButton)
        self.ButtonFind.setGeometry(QtCore.QRect(60, 110, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonFind.setFont(font)
        self.ButtonFind.setObjectName("ButtonFind")
        self.ButtonInsert = QtWidgets.QPushButton(self.FrameButton)
        self.ButtonInsert.setGeometry(QtCore.QRect(60, 210, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonInsert.setFont(font)
        self.ButtonInsert.setObjectName("ButtonInsert")
        self.ButtonUpdate = QtWidgets.QPushButton(self.FrameButton)
        self.ButtonUpdate.setGeometry(QtCore.QRect(60, 310, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonUpdate.setFont(font)
        self.ButtonUpdate.setObjectName("ButtonUpdate")
        self.ButtonQuery = QtWidgets.QPushButton(self.FrameButton)
        self.ButtonQuery.setGeometry(QtCore.QRect(60, 410, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonQuery.setFont(font)
        self.ButtonQuery.setObjectName("ButtonQuery")
        self.ButtonQuit = QtWidgets.QPushButton(self.FrameButton)
        self.ButtonQuit.setGeometry(QtCore.QRect(60, 510, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonQuit.setFont(font)
        self.ButtonQuit.setObjectName("ButtonQuit")
        MainWindow.setCentralWidget(self.Window)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1283, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ? set title
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        # !set table
        self.TableData.setColumnCount(4)
        self.TableData.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(0, item)
        self.TableData.setColumnWidth(0, 150)
        item = QtWidgets.QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(1, item)
        self.TableData.setColumnWidth(1, 270)
        item = QtWidgets.QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(2, item)
        self.TableData.setColumnWidth(2, 270)
        item = QtWidgets.QTableWidgetItem()
        self.TableData.setHorizontalHeaderItem(3, item)
        self.TableData.setColumnWidth(3, 100)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ? Connect multiple window
        self.ButtonFind.clicked.connect(self.findWindow)
        self.ButtonInsert.clicked.connect(self.insertWindow)
        self.ButtonUpdate.clicked.connect(self.updateWindow)
        self.ButtonQuery.clicked.connect(self.queryWindow)

        # ? connect button 
        self.ButtonDelete.clicked.connect(lambda: self.deleteStudent(self.TableData))
        self.ButtonClear.clicked.connect(lambda: self.clear(self.TableData))

        # ? Quit
        self.ButtonQuit.clicked.connect(lambda: self.close(MainWindow))
       
        # ? connect combobox
        self.add(combobox=self.comboBox)
        self.comboBox.activated[str].connect(self.onChanged)

    # Display database 
    def onChanged(self, text):
        query = text[0:3]
        connection = sqlite3.connect('StudentManagement.db')
        cur = connection.cursor()
        res = cur.execute(
            "SELECT * FROM Student Where ClassID = '{}'".format(query))

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

    # ? add combobox
    def add(self, combobox):
        connection = connect('StudentManagement.db')
        cur = connection.cursor()
        cur.execute("""select * from Class""")
        data = cur.fetchall()
        name = []
        for i in range(len(data)):
            className = data[i][0]+' '+data[i][1]
            name.append(className)
        name.sort()
        for i in name:
            combobox.addItem(str(i))

    # ? Function connect multiple window

    def findWindow(self):
        self.FindWindow = QtWidgets.QMainWindow()
        self.ui = Ui_FindWindow()
        self.ui.setupUi(self.FindWindow)
        self.FindWindow.show()

    def insertWindow(self):
        self.InsertWindow = QtWidgets.QMainWindow()
        self.ui = Ui_InsertWindow()
        self.ui.setupUi(self.InsertWindow)
        self.InsertWindow.show()

    def updateWindow(self):
        self.UpdateWindow = QtWidgets.QMainWindow()
        self.ui = Ui_UpdateWindow()
        self.ui.setupUi(self.UpdateWindow)
        self.UpdateWindow.show()

    def queryWindow(self):
        self.QueryWindow = QtWidgets.QMainWindow()
        self.ui = Ui_QueryWindow()
        self.ui.setupUi(self.QueryWindow)
        self.QueryWindow.show()

    # ? Quit
    def close(self, MainWindow):
        mess = QMessageBox()
        mess.setIcon(QMessageBox.Warning)
        mess.setWindowTitle("Window Close")
        mess.setWindowIcon(QtGui.QIcon('warning.png'))
        mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
        mess.setText("Are you sure you want to close the windodw ?")
        mess.setStandardButtons(QMessageBox.Yes | QMessageBox.No )
        question = mess.exec_()
        if question == QMessageBox.Yes :
            MainWindow.close()

    # ? delete
    def deleteStudent(self, TableData):
        mess = QMessageBox()
        mess.setIcon(QMessageBox.Warning)
        mess.setWindowIcon(QtGui.QIcon('warning.png'))
        mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
        mess.setWindowTitle("Delete Student")
        mess.setText("Are you sure you want to delete this student ?")
        mess.setStandardButtons(QMessageBox.Yes | QMessageBox.No )
        question = mess.exec_()

        try:
            if question == QMessageBox.Yes :
                index = TableData.currentRow()
                data = TableData.item(index,0).text()
                connection = sqlite3.connect('StudentManagement.db')
                cur = connection.cursor()
                deleteGrade = "DELETE FROM StudentGrades WHERE StudentID = '{}'".format(data)
                deleteStudent = "DELETE FROM Student WHERE StudentID = '{}'".format(data)
                cur.execute(deleteGrade)
                cur.execute(deleteStudent)
                connection.commit()
                TableData.removeRow(index)
            
        except:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(" Error ")
            mess.exec_()
        pass

    #? clear
    def clear(self, TableData):
        while TableData.rowCount() > 0:
            TableData.removeRow(0)
        pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Management System"))
        self.BackGroundLabel.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p><img src=\":/Main/background.png\"/></p></body></html>"))
        self.ButtonDelete.setText(_translate("MainWindow", "Delete"))
        self.ButtonClear.setText(_translate("MainWindow", "Clear"))
        self.Title.setText(_translate(
            "MainWindow", "Student Management System"))
        self.LabelClass.setText(_translate("MainWindow", "Class"))
        self.ButtonFind.setText(_translate("MainWindow", "Find"))
        self.ButtonInsert.setText(_translate("MainWindow", "Insert"))
        self.ButtonUpdate.setText(_translate("MainWindow", "Update"))
        self.ButtonQuery.setText(_translate("MainWindow", "Query"))
        self.ButtonQuit.setText(_translate("MainWindow", "Quit"))
        item = self.TableData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.TableData.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Student Name"))
        item = self.TableData.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Student Address"))
        item = self.TableData.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Class ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
