import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QPushButton

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("иконка.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(124, 131, 255)")

        self.Startgame = QtWidgets.QPushButton(parent=Dialog)

        self.Startgame.setGeometry(QtCore.QRect(240, 160, 121, 41))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.Startgame.setFont(font)
        self.Startgame.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.Startgame.setIconSize(QtCore.QSize(16, 16))
        self.Startgame.setDefault(False)
        self.Startgame.setFlat(False)
        self.Startgame.setObjectName("Startgame")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(200, 80, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0)")
        self.label.setObjectName("label")
        self.finishgame = QtWidgets.QPushButton(parent=Dialog)
        self.finishgame.setGeometry(QtCore.QRect(240, 280, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.finishgame.setFont(font)
        self.finishgame.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.finishgame.setIconSize(QtCore.QSize(16, 16))
        self.finishgame.setDefault(False)
        self.finishgame.setFlat(False)
        self.finishgame.setObjectName("finishgame")
        self.rules = QtWidgets.QPushButton(parent=Dialog)
        self.rules.setGeometry(QtCore.QRect(240, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.rules.setFont(font)
        self.rules.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.rules.setIconSize(QtCore.QSize(16, 16))
        self.rules.setDefault(False)
        self.rules.setFlat(False)
        self.rules.setObjectName("rules")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 470, 41, 31))
        self.pushButton.setStyleSheet("    border-radius:  10px;\n"
                                      "    background-color:  rgb(126, 255, 163);\n"
                                      "    color:  rgb(255, 255, 255);\n"
                                      "    font-size:  33px;")
        button = QPushButton()
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("музыка.png"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setObjectName("pushButton")

        def change_color():
            if self.pushButton.styleSheet() == ("    border-radius:  10px;\n"
                                                "    background-color:  rgb(255, 52, 62);\n"
                                                "    color:  rgb(255, 255, 255);\n"
                                                "    font-size:  33px;"):
                self.pushButton.setStyleSheet("    border-radius:  10px;\n"
                                              "    background-color:  rgb(126, 255, 163);\n"
                                              "    color:  rgb(255, 255, 255);\n"
                                              "    font-size:  33px;")
            else:
                self.pushButton.setStyleSheet("    border-radius:  10px;\n"
                                              "    background-color:  rgb(255, 52, 62);\n"
                                              "    color:  rgb(255, 255, 255);\n"
                                              "    font-size:  33px;")

        self.pushButton.clicked.connect(change_color)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(10, 20, 590, 90)
        self.text = 'Запомни порядок'
        self.index = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateText)
        self.timer.start(100)
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0,0,0)")
        self.label.setObjectName("label")

    def updateText(self):
        if self.index < len(self.text):
            self.label.setText(self.text[:self.index + 1])
            self.index += 1
        else:
            self.timer.stop()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Игра запомни порядок"))
        self.Startgame.setText(_translate("Dialog", "Начать"))
        self.finishgame.setText(_translate("Dialog", "Выйти"))
        self.rules.setText(_translate("Dialog", "Правила"))

    def close_application(self):
        reply = QMessageBox()
        reply.setWindowIcon(QtGui.QIcon('иконка.png'))
        reply.setWindowTitle('Подтверждение')
        reply.setText("Вы уверены, что хотите покинуть игру?")
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        reply.button(QMessageBox.StandardButton.Yes).setText('Да')
        reply.button(QMessageBox.StandardButton.No).setText('Нет')

        if reply.exec() == QMessageBox.StandardButton.Yes:
            sys.exit()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.timer.start(100)
    Dialog.show()

    ui.finishgame.clicked.connect(ui.close_application)

    sys.exit(app.exec())