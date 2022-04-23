from PyQt5.QtWidgets import QLabel, QWidget, QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit
from PyQt5.QtCore import Qt

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

    def unitUI(self):                                             #Виджеты
        hello = QLabel("Добро пожаловать в программу для определения злоровья.")
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

    def unitUI(self):                                             #Виджеты
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
    def next(self):
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

if __name__ == "__main__":
    app = QApplication([])
    main = MainWin()
    second = TestWin()
    third = FinalWin()



    
    
    
    
    
    
    app.exec_()
