import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QUrl, QTimer
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QLabel, QMainWindow, QMessageBox
from PyQt6.QtGui import QColor, QIcon, QPixmap
import random

class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setGeometry(650, 250, 600, 510)
        self.setWindowTitle("Игра «Запомни порядок»")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("иконка.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(163, 168, 255)")

        self.label12 = QtWidgets.QLabel("f", self)
        self.pix = QtGui.QPixmap("861039.png")
        self.label12.setPixmap(self.pix)
        self.label12.move(85, 30)
        self.label12.resize(600, 600)

        self.Startgame = QtWidgets.QPushButton(parent=self)
        self.Startgame.setGeometry(QtCore.QRect(240, 120, 121, 41))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)

        self.Startgame.setFont(font)
        self.Startgame.setStyleSheet("""
        QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #AE52D4, stop:1 #7E57C2);
            color: black;
            font-size: 18px;
            border: none;
            border-radius: 20px;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7E57C2, stop:1 #AE52D4);
        }
        QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7E57C2, stop:1 #AE52D4);
            padding-left: 10px;
            padding-top: 13px;
        }
    """)
        self.Startgame.setIconSize(QtCore.QSize(16, 16))
        self.Startgame.setText('Начать игру')
        self.Startgame.setObjectName("Startgame")
        self.Startgame.clicked.connect(self.show_window_3)


        self.main_menu = QtWidgets.QLabel(parent=self)
        self.main_menu.setGeometry(QtCore.QRect(200, 80, 211, 31))
        font = QtGui.QFont()

        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)

        self.main_menu.setFont(font)
        self.main_menu.setStyleSheet("color: rgb(0, 0, 0)")
        self.main_menu.setText("Запомни порядок")
        self.main_menu.setObjectName("label")

        self.finishgame = QtWidgets.QPushButton(parent=self)
        self.finishgame.setGeometry(QtCore.QRect(240, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.finishgame.setFont(font)
        self.finishgame.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #AE52D4, stop:1 #7E57C2);
                    color: black;
                    font-size: 18px;
                    border: none;
                    border-radius: 20px;
                    padding: 5px 10px;
                }
                QPushButton:hover {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7E57C2, stop:1 #AE52D4);
                }
                QPushButton:pressed {
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7E57C2, stop:1 #AE52D4);
                    padding-left: 10px;
                    padding-top: 13px;
                }
            """)
        self.finishgame.setIconSize(QtCore.QSize(16, 16))
        self.finishgame.setText('Выход')
        self.finishgame.setObjectName("finishgame")
        self.finishgame.clicked.connect(self.close_application)

        self.rules = QtWidgets.QPushButton(parent=self)
        self.rules.setGeometry(QtCore.QRect(240, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.rules.setFont(font)
        self.rules.setStyleSheet("""
        QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #AE52D4, stop:1 #7E57C2);
            color: black;
            font-size: 18px;
            border: none;
            border-radius: 20px;
            padding: 5px 10px;
        }
        QPushButton:hover {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7E57C2, stop:1 #AE52D4);
        }
        QPushButton:pressed {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #7E57C2, stop:1 #AE52D4);
            padding-left: 10px;
            padding-top: 13px;
        }
    """)
        self.rules.setIconSize(QtCore.QSize(16, 16))
        self.rules.setText("Правила")
        self.rules.setObjectName("rules")
        self.rules.clicked.connect(self.open_rules)

        self.label = QtWidgets.QLabel(parent=self)
        self.label.setGeometry(QtCore.QRect(100, 100, 390, 250))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:rgb (124, 131, 255)")
        self.label.setObjectName("label")
        self.label.setText("Начните игру, и на экране загорится последовательность кнопок. Запомните эту последовательность. После того, как кнопки погаснут, начните нажимать на них в том же порядке, в котором они загорались. Если вы нажмете на все кнопки правильно, то игра продолжится и добавит еще одну кнопку к последовательности. Если вы допустите ошибку, то игра завершится.")
        self.label.setWordWrap(True)
        self.label.hide()
        self.label.setStyleSheet("border: 2px solid black")

        self.returnToMain = QtWidgets.QPushButton(parent=self)
        self.returnToMain.setGeometry(QtCore.QRect(235, 380, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.returnToMain.setFont(font)
        self.returnToMain.setStyleSheet("background-color: rgb(0, 255, 127)")
        self.returnToMain.setObjectName("returnToMain")
        self.returnToMain.setText('Вернуться назад')
        self.returnToMain.clicked.connect(self.close_rules)
        self.returnToMain.hide()

        self.main_menu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.main_menu.setGeometry(10, 0, 590, 90)
        self.text = 'Запомни порядок'
        self.index = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateText)
        self.timer.start(100)
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.main_menu.setFont(font)
        self.main_menu.setStyleSheet("color: rgb(0,0,0)")
        self.main_menu.setObjectName("label")

    def show_window_3(self):
        self.hide()  # Скрыть текущее окно
        self.w3 = Ui_Dialog()
        self.w3.show()

    def show_window_2(self):
        self.hide()  # Скрыть текущее окно
        self.w2 = MemoryGame(self)
        self.w2.show()

    def open_rules(self):
        self.returnToMain.show()
        self.label.show()
        self.Startgame.setEnabled(False)
        self.rules.setEnabled(False)
        self.finishgame.setEnabled(False)

    def close_rules(self):
        self.returnToMain.hide()
        self.label.hide()
        self.Startgame.setEnabled(True)
        self.rules.setEnabled(True)
        self.finishgame.setEnabled(True)
    def updateText(self):
        if self.index < len(self.text):
            self.main_menu.setText(self.text[:self.index + 1])
            self.index += 1
        else:
            self.timer.stop()


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

class MemoryGame(QtWidgets.QMainWindow):
    def __init__(self, Main_Window):
        super(MemoryGame, self).__init__()
        self.main_window = Main_Window

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Запомни порядок")
        self.resize(480,460)


        self.setStyleSheet("background-color: rgb(163, 168, 255)")
        icon = QIcon("иконка.png")  # Укажите путь к вашей иконке
        self.setWindowIcon(icon)

        self.colors = [QColor("red"), QColor("blue"), QColor("green"), QColor("yellow"),
                       QColor("purple"), QColor("orange"), QColor("pink"), QColor("turquoise"),
                       QColor("brown")]

        self.buttons = []
        self.sequence = []
        self.player_sequence = []
        self.sequence_length = 3

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
            button.setEnabled(False)  # Заблокировать кнопку
            self.buttons.append(button)

            # Устанавливаем координаты кнопки на форме
            button.move(*position)

        self.start_button = QPushButton("Начать", self)
        self.start_button.clicked.connect(self.startGame)
        self.start_button.setStyleSheet("background-color: rgb(255, 20, 147)")
        self.start_button.move(200, 400)

        font_backtomenu = QtGui.QFont()
        font_backtomenu.setPointSize(14)

        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
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
        back_to_menu.clicked.connect(self.open_first_window)

        self.level = 0
        self.level_label = QLabel("", self)  # Создаем пустую метку уровня
        self.level_label.setGeometry(195, 30, 100, 50)  # Устанавливаем размер и позицию текста
        self.level_label.setFont(font)
        self.level_label.setStyleSheet("color: black ")

    def open_first_window(self):
        self.main_window.show()
        self.close()

    def startGame(self):

        self.start_button.hide()

        for button in self.buttons:
            button.setEnabled(True)

        self.playing_sequence = True  # Устанавливаем флаг, что идет воспроизведение последовательности
        self.level += 1  # Увеличиваем уровень на 1

        self.level_label.setText(f"Уровень: {self.level}")  # Обновляем текст метки level_label

        self.sequence = []

        for i in range(self.sequence_length):
            self.sequence.append(random.randint(0, 8))

        for i, button_index in enumerate(self.sequence):
            QTimer.singleShot(850 * i, lambda i=i: self.changeColor(self.buttons[self.sequence[i]]))
            QTimer.singleShot(850 * i + 400, lambda i=i: self.restoreColor(self.buttons[self.sequence[i]]))
            QTimer.singleShot(850 * len(self.sequence), lambda: setattr(self, 'playing_sequence',
                                                                        False))  # Сбрасываем флаг после окончания воспроизведения

    def changeColor(self, button):
        button.setStyleSheet("background-color: white")

    def restoreColor(self, button):
        button.setStyleSheet("background-color: rgb(189, 189, 255)")

    def buttonClicked(self):
        if self.playing_sequence:
            return  # Если идет воспроизведение последовательности, просто выходим из метода

        button = self.sender()
        button.setStyleSheet("background-color: white")

        self.player_sequence.append(self.buttons.index(button))

        if len(self.player_sequence) == len(self.sequence):
            if self.player_sequence == self.sequence:
                QMessageBox.information(self, "Поздравляем!", "Вы верно воспроизвели последовательность!")
                self.player_sequence = []
                self.sequence_length += 1
                QTimer.singleShot(800, self.startGame)  # Запускаем новую последовательность через 0.8 секунды
            else:
                QMessageBox.warning(self, "Попробуйте еще раз", "Вы ошиблись при воспроизведении последовательности :(")
                self.start_button.show()
                self.player_sequence = []
                self.sequence_length = 4
                self.level = 0  # Сбрасываем уровень
                self.level_label.setText(f"Уровень: {self.level}")  # Обновляем текст метки level_label

                for button in self.buttons:
                    button.setEnabled(False)
                    button.setStyleSheet("background-color: rgb(189, 189, 255)")

        QTimer.singleShot(350, lambda: button.setStyleSheet("background-color: rgb(189, 189, 255)"))

class Ui_Dialog(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setWindowTitle("Запомни порядок")
        self.resize(480,460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("иконка.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(163, 168, 255)")

        self.pushButton2x2 = QtWidgets.QPushButton(self)
        self.pushButton2x2.setGeometry(QtCore.QRect(30, 120, 91, 31))
        self.pushButton2x2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton2x2.setObjectName("pushButton2x2")
        self.pushButton2x2.setText('2x2')
        self.pushButton2x2.clicked.connect(self.show_window_2x2)
        self.label = QLabel(self)
        self.label.setGeometry(140, 140, 300, 300)
        self.label.setHidden(True)

        self.pushButton2x2.enterEvent = self.showImage
        self.pushButton2x2.leaveEvent = self.hideImage


        self.pushButton3x3 = QtWidgets.QPushButton(self)
        self.pushButton3x3.setGeometry(QtCore.QRect(190, 120, 91, 31))
        self.pushButton3x3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton3x3.setText('3x3')
        self.pushButton3x3.clicked.connect(self.show_window_3x3)
        self.label1 = QLabel(self)
        self.label1.setGeometry(100, 165, 300, 300)
        self.label1.setHidden(True)

        self.pushButton3x3.enterEvent = self.showImage2
        self.pushButton3x3.leaveEvent = self.hideImage2

        self.pushButton3x3.setObjectName("pushButton3x3")
        self.rezhim = QtWidgets.QLabel(self)
        self.rezhim.setGeometry(QtCore.QRect(160, 30, 161, 21))

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.rezhim.setFont(font)
        self.rezhim.setObjectName("rezhim")
        self.rezhim.setText('Выберите режим')

        self.pushButton4x4 = QtWidgets.QPushButton(self)
        self.pushButton4x4.setGeometry(QtCore.QRect(350, 120, 91, 31))
        self.pushButton4x4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton4x4.setObjectName("pushButton4x4")
        self.pushButton4x4.setText('4x4')
        self.pushButton4x4.clicked.connect(self.show_window_4x4)
        self.label2 = QLabel(self)
        self.label2.setGeometry(90, 175, 300, 270)
        self.label2.setHidden(True)

        self.pushButton4x4.enterEvent = self.showImage3
        self.pushButton4x4.leaveEvent = self.hideImage3

        font_backtomenu = QtGui.QFont()
        font_backtomenu.setPointSize(14)

        back_to_menu = QPushButton("назад.png", self)
        back_to_menu.setFont(font_backtomenu)
        back_to_menu.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("назад.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        back_to_menu.setIcon(icon1)
        back_to_menu.setFlat(True)
        back_to_menu.setObjectName("pushButton_10")
        back_to_menu.setGeometry(QtCore.QRect(10, 10, 21, 21))
        back_to_menu.clicked.connect(self.open_first_window)

    def showImage(self, event):
        pixmap = QPixmap('2x2.jpg')
        self.label.setPixmap(pixmap)
        self.label.setHidden(False)

    def hideImage(self, event):
        self.label.clear()
        self.label.setHidden(True)

    def showImage2(self, event):
        pixmap = QPixmap('3x3.jpg')
        self.label1.setPixmap(pixmap)
        self.label1.setHidden(False)

    def hideImage2(self, event):
        self.label1.clear()
        self.label1.setHidden(True)

    def showImage3(self, event):
        pixmap = QPixmap('4x4.jpg')
        scaled_pixmap = pixmap.scaled(300, 270)  # Уменьшаем размер изображения до 200x200
        self.label2.setPixmap(scaled_pixmap)
        self.label2.setHidden(False)

    def hideImage3(self, event):
        self.label2.clear()
        self.label2.setHidden(True)

    def show_window_2x2(self):
        self.hide()  # Скрыть текущее окно
        self.w2 = MemoryGame2x2(self)
        self.w2.show()

    def show_window_3x3(self):
        self.hide()  # Скрыть текущее окно
        self.w3 = MemoryGame(self)
        self.w3.show()

    def show_window_4x4(self):
        self.hide()  # Скрыть текущее окно
        self.w4 = MemoryGame4x4(self)
        self.w4.show()

    def open_first_window(self):
        self.w5 = Main_Window()
        self.w5.show()
        self.close()

class MemoryGame4x4(QtWidgets.QMainWindow):
    def __init__(self, Main_Window):
        super(MemoryGame4x4, self).__init__()
        self.main_window = Main_Window

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Запомни порядок")
        self.resize(500,500)


        self.setStyleSheet("background-color: rgb(163, 168, 255)")
        icon = QIcon("иконка.png")  # Укажите путь к вашей иконке
        self.setWindowIcon(icon)

        self.colors = [QColor("red"), QColor("blue"), QColor("green"), QColor("yellow"),
                       QColor("purple"), QColor("orange"), QColor("pink"), QColor("turquoise"),
                       QColor("brown")]

        self.buttons = []
        self.sequence = []
        self.player_sequence = []
        self.sequence_length = 4

        buttons_positions = [(80, 80), (170, 80), (260, 80), (350, 80),
                             (80, 160), (170, 160), (260, 160), (350, 160),
                             (80, 240), (170, 240), (260, 240), (350, 240),
                             (80, 320), (170, 320), (260, 320), (350, 320),]
        button_size = (75, 71)

        for i, position in enumerate(buttons_positions):
            button = QPushButton(self)
            button.setFixedSize(*button_size)
            button.setStyleSheet("background-color: rgb(189, 189, 255)")
            button.setObjectName(f"pushButton_{i + 1}")
            button.clicked.connect(self.buttonClicked)
            button.setEnabled(False)  # Заблокировать кнопку
            self.buttons.append(button)

            # Устанавливаем координаты кнопки на форме
            button.move(*position)

        self.start_button = QPushButton("Начать", self)
        self.start_button.clicked.connect(self.startGame)
        self.start_button.setStyleSheet("background-color: rgb(255, 20, 147)")
        self.start_button.move(200, 430)

        font_backtomenu = QtGui.QFont()
        font_backtomenu.setPointSize(14)

        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
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
        back_to_menu.clicked.connect(self.open_first_window)

        self.level = 0
        self.level_label = QLabel("", self)  # Создаем пустую метку уровня
        self.level_label.setGeometry(200, 10, 100, 50)  # Устанавливаем размер и позицию текста
        self.level_label.setFont(font)
        self.level_label.setStyleSheet("color: black ")

    def open_first_window(self):
        self.main_window.show()
        self.close()

    def startGame(self):

        self.start_button.hide()

        for button in self.buttons:
            button.setEnabled(True)

        self.playing_sequence = True  # Устанавливаем флаг, что идет воспроизведение последовательности
        self.level += 1  # Увеличиваем уровень на 1

        self.level_label.setText(f"Уровень: {self.level}")  # Обновляем текст метки level_label

        self.sequence = []

        for i in range(self.sequence_length):
            self.sequence.append(random.randint(0, 8))

        for i, button_index in enumerate(self.sequence):
            QTimer.singleShot(850 * i, lambda i=i: self.changeColor(self.buttons[self.sequence[i]]))
            QTimer.singleShot(850 * i + 400, lambda i=i: self.restoreColor(self.buttons[self.sequence[i]]))
            QTimer.singleShot(850 * len(self.sequence), lambda: setattr(self, 'playing_sequence',
                                                                        False))  # Сбрасываем флаг после окончания воспроизведения

    def changeColor(self, button):
        button.setStyleSheet("background-color: white")

    def restoreColor(self, button):
        button.setStyleSheet("background-color: rgb(189, 189, 255)")

    def buttonClicked(self):
        if self.playing_sequence:
            return  # Если идет воспроизведение последовательности, просто выходим из метода

        button = self.sender()
        button.setStyleSheet("background-color: white")

        self.player_sequence.append(self.buttons.index(button))

        if len(self.player_sequence) == len(self.sequence):
            if self.player_sequence == self.sequence:
                QMessageBox.information(self, "Поздравляем!", "Вы верно воспроизвели последовательность!")
                self.player_sequence = []
                self.sequence_length += 1
                QTimer.singleShot(800, self.startGame)  # Запускаем новую последовательность через 0.8 секунды
            else:
                QMessageBox.warning(self, "Попробуйте еще раз", "Вы ошиблись при воспроизведении последовательности :(")
                self.start_button.show()
                self.player_sequence = []
                self.sequence_length = 4
                self.level = 0  # Сбрасываем уровень
                self.level_label.setText(f"Уровень: {self.level}")  # Обновляем текст метки level_label

                for button in self.buttons:
                    button.setEnabled(False)
                    button.setStyleSheet("background-color: rgb(189, 189, 255)")

        QTimer.singleShot(350, lambda: button.setStyleSheet("background-color: rgb(189, 189, 255)"))

class MemoryGame2x2(QtWidgets.QMainWindow):
    def __init__(self, Main_Window):
        super(MemoryGame2x2, self).__init__()
        self.main_window = Main_Window

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Запомни порядок")
        self.resize(400,400)


        self.setStyleSheet("background-color: rgb(163, 168, 255)")
        icon = QIcon("иконка.png")  # Укажите путь к вашей иконке
        self.setWindowIcon(icon)

        self.colors = [QColor("red"), QColor("blue"), QColor("green"), QColor("yellow"),
                       QColor("purple"), QColor("orange"), QColor("pink"), QColor("turquoise"),
                       QColor("brown")]

        self.buttons = []
        self.sequence = []
        self.player_sequence = []
        self.sequence_length = 1

        buttons_positions = [(120, 100), (205, 100),
                             (120, 180), (205, 180)]
        button_size = (75, 71)

        for i, position in enumerate(buttons_positions):
            button = QPushButton(self)
            button.setFixedSize(*button_size)
            button.setStyleSheet("background-color: rgb(189, 189, 255)")
            button.setObjectName(f"pushButton_{i + 1}")
            button.clicked.connect(self.buttonClicked)
            button.setEnabled(False)  # Заблокировать кнопку
            self.buttons.append(button)

            # Устанавливаем координаты кнопки на форме
            button.move(*position)

        self.start_button = QPushButton("Начать", self)
        self.start_button.clicked.connect(self.startGame)
        self.start_button.setStyleSheet("background-color: rgb(255, 20, 147)")
        self.start_button.move(155, 300)

        font_backtomenu = QtGui.QFont()
        font_backtomenu.setPointSize(14)

        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(16)
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
        back_to_menu.clicked.connect(self.open_first_window)

        self.level = 0
        self.level_label = QLabel("", self)  # Создаем пустую метку уровня
        self.level_label.setGeometry(155, 20, 100, 50)  # Устанавливаем размер и позицию текста
        self.level_label.setFont(font)
        self.level_label.setStyleSheet("color: black ")

    def open_first_window(self):
        self.main_window.show()
        self.close()

    def startGame(self):

        self.start_button.hide()

        for button in self.buttons:
            button.setEnabled(True)

        self.playing_sequence = True  # Устанавливаем флаг, что идет воспроизведение последовательности
        self.level += 1  # Увеличиваем уровень на 1

        self.level_label.setText(f"Уровень: {self.level}")  # Обновляем текст метки level_label

        self.sequence = []

        for i in range(self.sequence_length):
            self.sequence.append(random.randint(0, 3))

        for i, button_index in enumerate(self.sequence):
            QTimer.singleShot(850 * i, lambda i=i: self.changeColor(self.buttons[self.sequence[i]]))
            QTimer.singleShot(850 * i + 400, lambda i=i: self.restoreColor(self.buttons[self.sequence[i]]))
            QTimer.singleShot(850 * len(self.sequence), lambda: setattr(self, 'playing_sequence',
                                                                        False))  # Сбрасываем флаг после окончания воспроизведения

    def changeColor(self, button):
        button.setStyleSheet("background-color: white")

    def restoreColor(self, button):
        button.setStyleSheet("background-color: rgb(189, 189, 255)")

    def buttonClicked(self):
        if self.playing_sequence:
            return  # Если идет воспроизведение последовательности, просто выходим из метода

        button = self.sender()
        button.setStyleSheet("background-color: white")

        self.player_sequence.append(self.buttons.index(button))

        if len(self.player_sequence) == len(self.sequence):
            if self.player_sequence == self.sequence:
                QMessageBox.information(self, "Поздравляем!", "Вы верно воспроизвели последовательность!")
                self.player_sequence = []
                self.sequence_length += 1
                QTimer.singleShot(800, self.startGame)  # Запускаем новую последовательность через 0.8 секунды
            else:
                QMessageBox.warning(self, "Попробуйте еще раз", "Вы ошиблись при воспроизведении последовательности :(")
                self.start_button.show()
                self.player_sequence = []
                self.sequence_length = 1
                self.level = 0  # Сбрасываем уровень
                self.level_label.setText(f"Уровень: {self.level}")  # Обновляем текст метки level_label

                for button in self.buttons:
                    button.setEnabled(False)
                    button.setStyleSheet("background-color: rgb(189, 189, 255)")

        QTimer.singleShot(350, lambda: button.setStyleSheet("background-color: rgb(189, 189, 255)"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = Main_Window()
    ui = Main_Window()
    ui.timer.start(100)
    Main.show()

    ui.finishgame.clicked.connect(ui.close_application)

    sys.exit(app.exec())