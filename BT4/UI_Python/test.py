from login import *




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginUi = QtWidgets.QWidget()
    ui = Ui_LoginUi()
    ui.setupUi(LoginUi)
    LoginUi.show()
    sys.exit(app.exec_())