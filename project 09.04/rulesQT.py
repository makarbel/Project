from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt

class Ui_Rules(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 370)

        Dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)

        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("иконка.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(124, 131, 255")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 401, 271))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.returnToMain = QtWidgets.QPushButton(parent=Dialog)
        self.returnToMain.setGeometry(QtCore.QRect(130, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.returnToMain.setFont(font)
        self.returnToMain.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.returnToMain.setObjectName("returnToMain")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Правила"))
        self.label.setText(_translate("Dialog", "Начните игру, и на экране загорится\n"
"последовательность кнопок.\n"
"Запомните эту последовательность. \n"
"После того, как кнопки погаснут,\n"
"начните нажимать на них в том же порядке,\n"
"в котором они загорались. \n"
"Если вы нажмете на все кнопки правильно,\n"
"то игра продолжится и добавит\n"
"еще одну кнопку к последовательности.\n"
"Если вы допустите ошибку, то игра завершится."))
        self.returnToMain.setText(_translate("Dialog", "Вернуться назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Rules()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
