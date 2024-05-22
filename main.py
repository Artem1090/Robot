from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QMessageBox, QHBoxLayout, QPushButton, QGroupBox, QButtonGroup
from random import *
from redactor import app2, win2
from labirint import *
from pinpong import *


app = QApplication([])
main_win = QWidget()
main_win.current_question = -1
main_win.total = 0
main_win.score = 0



label1 = QLabel('Выбирите что хотите')
RadioGroupBox = QGroupBox('Что можно сделать')
button1 = QPushButton('пинпонг')
button2 = QPushButton('лабиринт')
button3 = QPushButton('Арканоид')
button4 = QPushButton('Редактор картинки')
button_group = QButtonGroup()
button_group.addButton(button1)
button_group.addButton(button2)
button_group.addButton(button3)
button_group.addButton(button4)

wse = QHBoxLayout()
wse1 = QVBoxLayout()
wse2 = QVBoxLayout()
wse1.addWidget(button1)
wse1.addWidget(button2)
wse2.addWidget(button3)
wse2.addWidget(button4)
wse.addLayout(wse1)
wse.addLayout(wse2)
RadioGroupBox.setLayout(wse)







v_line = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line1.addWidget(label1)
v_line.addLayout(h_line1)
v_line.addWidget(RadioGroupBox)
v_line.addLayout(h_line3)











answers = [button1, button2, button3, button4]
question = []




def redactor():
    win2.show()
    app2.exec_()







main_win.setLayout(v_line)


def next():
     main_win.total += 1
     main_win.current_question += 1
     print('Статистика тест')
     print('Всего вопросов', main_win.total)
     print('правилбных ответов' , main_win.score)
     print('Рейтинг' , main_win.score/main_win.total*100)
     #x = randint (0, len(question) - 1)
     
     if main_win.current_question >= len(question):
          main_win.current_question = 0
     
     q = question[main_win.current_question]
     #q = question[x]
    

button4.clicked.connect(redactor) 
button2.clicked.connect(labirint)
button1.clicked.connect(pinpong)








main_win.show()
app.exec_() 
