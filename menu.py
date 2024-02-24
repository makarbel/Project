from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import Qt, QTimer

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
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
        self.finishgame.setGeometry(QtCore.QRect(240, 220, 121, 41))
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.finishgame.clicked.connect(self.close_application)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(10, 20, 590, 90)
        self.text = 'Запомни порядок'
        self.index = 0
        self.timer = QTimer()
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

    def close_application(self):
        reply = QMessageBox()
        reply.setWindowIcon(QtGui.QIcon('icon.png'))
        reply.setWindowTitle('Подтверждение')
        reply.setText("Вы уверены, что хотите покинуть приложение?")
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        reply.button(QMessageBox.StandardButton.Yes).setText('Да')
        reply.button(QMessageBox.StandardButton.No).setText('Нет')

        if reply.exec() == QMessageBox.StandardButton.Yes:
            Dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.timer.start(100)
    Dialog.show()
    sys.exit(app.exec())
