import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QMessageBox, QApplication, QLabel
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QColor
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore, QtGui
import random


class MemoryGame(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Запомни порядок")
        self.resize(480,480)


        self.setStyleSheet("background-color: rgb(43,135,209)")
        icon = QIcon("иконка.png")  # Укажите путь к вашей иконке
        self.setWindowIcon(icon)

        self.colors = [QColor("red"), QColor("blue"), QColor("green"), QColor("yellow"),
                       QColor("purple"), QColor("orange"), QColor("pink"), QColor("turquoise"),
                       QColor("brown")]

        self.buttons = []
        self.sequence = []
        self.player_sequence = []
        self.sequence_length = 4

        buttons_positions = [(110, 110), (200, 110), (290, 110),
                             (110, 190), (200, 190), (290, 190),
                             (110, 270), (200, 270), (290, 270)]
        button_size = (75, 71)

        for i, position in enumerate(buttons_positions):
            button = QPushButton(self)
            button.setFixedSize(*button_size)
            button.setStyleSheet("background-color: rgb(189, 189, 255)")
            button.setObjectName(f"pushButton_{i + 1}")
            button.clicked.connect(self.buttonClicked)
            self.buttons.append(button)

            # Устанавливаем координаты кнопки на форме
            button.move(*position)

        start_button = QPushButton("Начать", self)
        start_button.clicked.connect(self.startGame)
        start_button.setStyleSheet("background-color: rgb(255, 20, 147)")
        start_button.move(200, 400)

        font_backtomenu = QtGui.QFont()
        font_backtomenu.setPointSize(14)

        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        back_to_menu = QPushButton("назад.png", self)
        back_to_menu.setFont(font_backtomenu)
        back_to_menu.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("назад.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        back_to_menu.setIcon(icon1)
        back_to_menu.setFlat(True)
        back_to_menu.setObjectName("pushButton_10")
        back_to_menu.setGeometry(QtCore.QRect(10, 10, 21, 21))

        level_label = QLabel("Level 1", self)
        level_label.setGeometry(210, 30, 71, 31)  # Устанавливаем размер и позицию текста
        level_label.setFont(font)
        level_label.setStyleSheet("color: rgb(170,207,237)")

    def startGame(self):
        self.sequence = []
        for i in range(self.sequence_length):
            self.sequence.append(random.randint(0, 8))

        for i, button_index in enumerate(self.sequence):
            QTimer.singleShot(750 * i, lambda i=i: self.changeColor(self.buttons[self.sequence[i]]))
            QTimer.singleShot(750 * i + 500, lambda i=i: self.restoreColor(self.buttons[self.sequence[i]]))

    def changeColor(self, button):
        button.setStyleSheet("background-color: white")

    def restoreColor(self, button):
        button.setStyleSheet("background-color: rgb(189, 189, 255)")

    def buttonClicked(self):
        button = self.sender()
        button.setStyleSheet("background-color: white")

        self.player_sequence.append(self.buttons.index(button))

        if len(self.player_sequence) == len(self.sequence):
            if self.player_sequence == self.sequence:
                QMessageBox.information(self, "Поздравляем!", "Вы верно воспроизвели последовательность!")
                self.player_sequence = []
                self.sequence_length += 1
            else:
                QMessageBox.warning(self, "Ошибка", "Вы ошиблись при воспроизведении последовательности")
                self.player_sequence = []
                self.sequence_length = 4

        QTimer.singleShot(300, lambda: button.setStyleSheet("background-color: rgb(189, 189, 255)"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = MemoryGame()
    game.show()
    sys.exit(app.exec())
