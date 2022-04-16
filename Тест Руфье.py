from PyQt5.QtWidgets import QLabel, QWidget, QApplication,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit
from PyQt5.QtCore import Qt

class MainWin(QWidget):
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



    def unitUI(self):
        hello = QLabel("Здесь будет приветствие")
        instr = QLabel("Здесь будет инсрукция")
        button = QPushButton("Начать")
        v_line = QVBoxLayout()

    def connects(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    main = MainWin()
    
    
    
    
    
    
    
    
    
    
    
    app.exec_()
