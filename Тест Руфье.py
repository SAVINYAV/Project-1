from PyQt5.QtWidgets import QLabel, QWidget, QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit
from PyQt5.QtCore import Qt, QTime, QTimer 


class Experiment():
    def __init__(self, age, p1, p2, p3):
        self.age = age
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def result(self):
        self.index = (4*(self.p1 + self.p2 + self.p3)-200)/10
        
        if self.age < 7:
            self.recomen = "Нет результата, вы очень маленький!"
        
        if self.age == 7 or self.age == 8:
            if self.index >= 21:
                self.recomen = "Низкий. Срочно обратетесь к врачу!!!"
            elif self.index >= 17 and self.index <21:
                self.recomen = "Ниже среднего. Обратетесь к врачу!"
            elif self.indef >= 12 and self.index <17:
                self.recomen = "Средний. Можно обратиться к врачу"
            elif self.index >= 6.5 and self.index <12:
                self.recomen = "Выше среднего"
            else:
                self.recomen = 'Высокий'
        
        if self.age == 9 or self.age == 10:
            if self.index >= 19.5:
                self.recomen = "Низкий. Срочно обратетесь к врачу!!!"
            elif self.index >= 15.5 and self.index <19.4:
                self.recomen = "Ниже среднего. Обратетесь к врачу!"
            elif self.indef >= 10.5 and self.index <15.4:
                self.recomen = "Средний. Можно обратиться к врачу"
            elif self.index >= 5 and self.index <10.4:
                self.recomen = "Выше среднего"
            else:
                self.recomen = 'Высокий'
        
        if self.age == 11 or self.age == 12:
            if self.index >= 18:
                self.recomen = "Низкий. Срочно обратетесь к врачу!!!"
            elif self.index >= 14 and self.index <17.9:
                self.recomen = "Ниже среднего. Обратетесь к врачу!"
            elif self.indef >=9 and self.index <14:
                self.recomen = "Средний. Можно обратиться к врачу"
            elif self.index >= 3.5 and self.index <9:
                self.recomen = "Выше среднего"
            else:
                self.recomen = 'Высокий'
        
        if self.age == 13 or self.age == 14:
            if self.index >= 16.5:
                self.recomen = "Низкий. Срочно обратетесь к врачу!!!"
            elif self.index >= 12.5 and self.index <16.4:
                self.recomen = "Ниже среднего. Обратетесь к врачу!"
            elif self.indef >=7.5 and self.index <12.5:
                self.recomen = "Средний. Можно обратиться к врачу"
            elif self.index >= 2 and self.index <7.5:
                self.recomen = "Выше среднего"
            else:
                self.recomen = 'Высокий'

        if self.age >= 15:
            if self.index >= 15:
                self.recomen = "Низкий. Срочно обратетесь к врачу!!!"
            elif self.index >= 11 and self.index <15:
                self.recomen = "Ниже среднего. Обратетесь к врачу!"
            elif self.indef >= 6 and self.index <11:
                self.recomen = "Средний. Можно обратиться к врачу"
            elif self.index >= 0.5 and self.index <6:
                self.recomen = "Выше среднего"
            else:
                self.recomen = 'Высокий'



class MainWin(QWidget):                                           #Первый экран
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.unitUI()
        self.connects()                                            
        self.show()

    def set_appear(self):
        self.resize(600,400)
        self.setWindowTitle("Инструкция")
        self.move(250,250)

    def unitUI(self):                                             #Виджеты 1
        hello = QLabel("Добро пожаловать в программу для определения здоровья.")
        instr = QLabel("Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вышего здоровья.\nПроба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\nУ испытуемого, находящегося  положении лёжа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\nзатем в течение 45 секунд испытуемый выполняет 30 приседаний.\nПосле окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\nа потом - за последние 15 секунд первой минуты периода восстановления.\nВажно! Если в прочессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\nушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.")
        self.button = QPushButton("Начать")
        v_line = QVBoxLayout()
        v_line.addWidget(hello)
        v_line.addWidget(instr)
        v_line.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(v_line)

    def connects(self):                                          #Переброс на 2-й экран
        self.button.clicked.connect(self.next)
    def next(self):
        self.hide()
        second.show()

class TestWin(QWidget):                                           #Второй экран
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.unitUI()                                                  
        self.connects()

    def set_appear(self):
        self.resize(600,400)
        self.setWindowTitle("Тест Руфье")
        self.move(250,250)

    def unitUI(self):                                             #Виджеты 2
        label_fio = QLabel('Введите ФИО:')
        fio = QLineEdit()
        label_age = QLabel('Введите ваш возраст:')
        self.age = QLineEdit('0')
        instr1 = QLabel('ИНСТРУКЦИЯ 1')
        self.test1 = QPushButton('1 тест')
        self.p1 = QLineEdit('0')
        instr2 = QLabel('ИНСТРУКЦИЯ 2')
        self.test2 = QPushButton('2 тест')
        instr3 = QLabel('ИНСТРУКЦИЯ 2')
        self.test3 = QPushButton('3 тест')
        self.p2 = QLineEdit('0')
        self.p3 = QLineEdit('0')
        self.button = QPushButton('Завершить')
        self.label_timer = QLabel('00:00:00')
        main_line = QHBoxLayout()
        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()
                
        v_line1.addWidget(label_fio)
        v_line1.addWidget(fio)                                     #Прикрепляем виджеты к линиям
        v_line1.addWidget(label_age)
        v_line1.addWidget(self.age)
        v_line1.addWidget(instr1)
        v_line1.addWidget(self.test1)
        v_line1.addWidget(self.p1)
        v_line1.addWidget(instr2)
        v_line1.addWidget(self.test2)
        v_line1.addWidget(instr3)
        v_line1.addWidget(self.test3)
        v_line1.addWidget(self.p2)
        v_line1.addWidget(self.p3)
        v_line1.addWidget(self.button, alignment=Qt.AlignCenter)

        v_line2.addWidget(self.label_timer)

        main_line.addLayout(v_line1)                              #присоединение к главной линии
        main_line.addLayout(v_line2)
        self.setLayout(main_line)   #-----------------------размещение главной линии 

    def connects(self):                                         #Переброс на 3-й экран
        self.button.clicked.connect(self.next)
        self.test1.clicked.connect(self.timer1)
        self.test2.clicked.connect(self.timer2)
        self.test3.clicked.connect(self.timer3)

    def timer1(self):
        self.timer = QTimer()
        self.time = QTime(0,0,16)
        self.timer.timeout.connect(self.event1)
        self.timer.start(1000)

    def timer2(self):
        self.timer = QTimer()
        self.time = QTime(0,0,31)
        self.timer.timeout.connect(self.event2)
        self.timer.start(2000)

    def timer3(self):
        self.timer = QTimer()
        self.time = QTime(0,1,0)
        self.timer.timeout.connect(self.event3)
        self.timer.start(1000)

    def event1(self):
        self.time = self.time.addSecs(-1)
        self.label_timer.setText(self.time.toString("hh:mm:ss"))
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def event2(self):
        self.time = self.time.addSecs(-1)
        self.label_timer.setText(self.time.toString("hh:mm:ss") [6:8])
        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def event3(self):
        self.time = self.time.addSecs(-1)
        self.label_timer.setText(self.time.toString("hh:mm:ss"))
        if int(self.time.toString("hh:mm:ss")[6:8]) < 59 and int(self.time.toString("hh:mm:ss")[6:8]) > 45:
            self.label_timer.setStyleSheet('color:rgb(0,255,0)')
        elif int(self.time.toString("hh:mm:ss")[6:8]) < 45 and int(self.time.toString("hh:mm:ss")[6:8]) > 15:
            self.label_timer.setStyleSheet('color:rgb(0,0,0)')
        else:
            self.label_timer.setStyleSheet('color:rgb(0,255,0)')

        if self.time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


    def next(self):
        exp = Experiment(int(self.age.text()), int(self.p1.text()), int(self.p2.text()), int(self.p3.text()))
        exp.result()
        third.setResult(exp.index, exp.recomen)
        self.hide()
        third.show()

class FinalWin(QWidget):                                          #Финальный экран
    def __init__(self):
        QWidget.__init__(self)
        self.set_appear()
        self.unitUI()                                                  

    def set_appear(self):
        self.resize(600,400)
        self.setWindowTitle("Результаты")
        self.move(250,250)

    def unitUI(self):
        self.index = QLabel('index')                  #Баллы
        self.recomen = QLabel('recomen')              #Рекомендации
        v_line = QVBoxLayout()
        v_line.addWidget(self.index, alignment=Qt.AlignCenter)
        v_line.addWidget(self.recomen, alignment=Qt.AlignCenter)
        self.setLayout(v_line)

    def setResult(self, index, recomen):
        self.index.setText("Ваш индекс: "+str(index))
        self.recomen.setText('Ваш уровень работы сердца: '+recomen)

if __name__ == "__main__":
    app = QApplication([])
    main = MainWin()
    second = TestWin()
    third = FinalWin()


    app.exec_()
