

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import BackGround
import sqlite3


class Ui_QueryWindow(object):
    def setupUi(self, QueryWindow):
        QueryWindow.setObjectName("QueryWindow")
        QueryWindow.resize(911, 800)
        self.centralwidget = QtWidgets.QWidget(QueryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleFind = QtWidgets.QLabel(self.centralwidget)
        self.titleFind.setGeometry(QtCore.QRect(-1, 10, 901, 100))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.titleFind.setFont(font)
        self.titleFind.setStyleSheet("color: rgb(255, 255, 255);")
        self.titleFind.setAlignment(QtCore.Qt.AlignCenter)
        self.titleFind.setObjectName("titleFind")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 900, 770))
        self.Background.setStyleSheet("background-image: url(:/Main/background.png);")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.LabelStudentID = QtWidgets.QLabel(self.centralwidget)
        self.LabelStudentID.setGeometry(QtCore.QRect(50, 90, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LabelStudentID.setFont(font)
        self.LabelStudentID.setStyleSheet("color: rgb(255, 255, 255);")
        self.LabelStudentID.setObjectName("LabelStudentID")
        self.TextQuery = QtWidgets.QTextEdit(self.centralwidget)
        self.TextQuery.setGeometry(QtCore.QRect(50, 150, 601, 151))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        self.TextQuery.setFont(font)
        self.TextQuery.setObjectName("TextQuery")
        self.ButtonExecute = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonExecute.setGeometry(QtCore.QRect(700, 200, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonExecute.setFont(font)
        self.ButtonExecute.setObjectName("ButtonExecute")
        self.ButtonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonQuit.setGeometry(QtCore.QRect(200, 680, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonQuit.setFont(font)
        self.ButtonQuit.setObjectName("ButtonQuit")


        self.ButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonClear.setGeometry(QtCore.QRect(550, 680, 150, 50))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonClear.setFont(font)
        self.ButtonClear.setObjectName("ButtonClear")



        self.TableData = QtWidgets.QTableWidget(self.centralwidget)
        self.TableData.setGeometry(QtCore.QRect(50, 320, 800, 320))
        self.TableData.setObjectName("TableData")
        self.TableData.setColumnCount(0)
        self.TableData.setRowCount(0)
        self.Background.raise_()
        self.titleFind.raise_()
        self.LabelStudentID.raise_()
        self.TextQuery.raise_()
        self.ButtonExecute.raise_()
        self.ButtonQuit.raise_()
        self.TableData.raise_()
        self.ButtonClear.raise_()
        QueryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QueryWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 26))
        self.menubar.setObjectName("menubar")
        QueryWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QueryWindow)
        self.statusbar.setObjectName("statusbar")
        QueryWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(QueryWindow)
        QtCore.QMetaObject.connectSlotsByName(QueryWindow)

        self.ButtonQuit.clicked.connect(lambda:self.close(QueryWindow))
        self.ButtonExecute.clicked.connect(self.query_execute)
        self.ButtonClear.clicked.connect(lambda: self.clear(self.TableData))
        # ? set title
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        QueryWindow.setWindowIcon(icon)

    def close(self,QueryWindow):
        mess = QMessageBox()
        mess.setIcon(QMessageBox.Warning)
        mess.setWindowTitle("Window Close")
        mess.setWindowIcon(QtGui.QIcon('warning.png'))
        mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
        mess.setText("Are you sure you want to close the windodw ?")
        mess.setStandardButtons(QMessageBox.Yes | QMessageBox.No )
        question = mess.exec_()
        if question == QMessageBox.Yes :
            QueryWindow.hide()

    def query_execute(self):
        try:
            connection = sqlite3.connect('StudentManagement.db')
            cur = connection.cursor()
            query = self.TextQuery.toPlainText()
            res = cur.execute(query)

            self.TableData.horizontalHeader().setStretchLastSection(True)
            self.TableData.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            columnName =[]
            for column in res.description:
                columnName.append(column[0])

    # ?Set rowcount vs columnCount
            for row_number, row_data in enumerate(res):
                self.TableData.setRowCount(row_number)
                self.TableData.setColumnCount(len(row_data))
                self.TableData.insertRow(row_number)

                # St columns name
                self.TableData.setHorizontalHeaderLabels(columnName)

                for column_number, data in enumerate(row_data): 
                    self.TableData.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        except:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Critical)
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setStyleSheet("QLabel{min-height:30 px; font-size: 24px;}")
            mess.setWindowIcon(QtGui.QIcon('cancel.png'))
            mess.setWindowTitle("Error")
            mess.setText(" Error ")
            mess.exec_()

    def clear(self, TableData):
        TableData.horizontalHeader().hide()
        while TableData.rowCount() > 0:
            TableData.removeRow(0)
        pass


    def retranslateUi(self, QueryWindow):
        _translate = QtCore.QCoreApplication.translate
        QueryWindow.setWindowTitle(_translate("QueryWindow", "Query SQL"))
        self.titleFind.setText(_translate("QueryWindow", "Query"))
        self.Background.setWhatsThis(_translate("QueryWindow", "<html><head/><body><p><img src=\":/Main/background.png\"/></p></body></html>"))
        self.LabelStudentID.setText(_translate("QueryWindow", " Query"))
        self.ButtonExecute.setText(_translate("QueryWindow", "Execute"))
        self.ButtonQuit.setText(_translate("QueryWindow", "Quit"))
        self.ButtonClear.setText(_translate("QueryWindow", "Clear"))


        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QueryWindow = QtWidgets.QMainWindow()
    ui = Ui_QueryWindow()
    ui.setupUi(QueryWindow)
    QueryWindow.show()
    sys.exit(app.exec_())
