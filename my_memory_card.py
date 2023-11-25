#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGroupBox, QPushButton, QButtonGroup, QButtonGroup, QRadioButton, QHBoxLayout

from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3)
    self.question = question
    self.right_answer = right_answer_answer
    self.wrong1 = wrong1
    self.wrong2 = wrong2
    self.wrong3 = wrong3

Question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'бразилский'))
question_list.append(Question('Какого цвета нет в флаге России', 'Зелёный', 'Красный', 'белый', 'синий'))

app = QApplication([])

btn_OK = PushButton("Ответить")
lb_Question = QLabel('Самый сложный вопрос в мире')

RadioGroupBox = QGroupBox('Варианты ответов')
qwerty_1 = QRadioButton('Варианты 1')
qwerty_2 = QRAdioButton('Варианты 2')
qwerty_3 = QRadioButton('Варианты 3')
qwerty_4 = QRadioButton('Варианты 4')

RadioGroup = QButtonGroup()
RadioGroup = addButton(qwerty_1)
RadioGroup = addButton(qwerty_2)
RadioGroup = addButton(qwerty_3)
RadioGroup = addButton(qwerty_4)

Layout_ans1 = addLayout(layout_ans2)
Layout_ans1 = addLayout(Layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addwidget(lb_Result, alignment=(Qt.Ali))
layout_res.addWidget(lb_Correct, alignment=(Qt.AlignHCenter, stretch=2)
AnsGroupBox.hide()

layout_line1.addWidget(lb_Question, alignment=(Qt.alignHCenter / Qt.alignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide

































