from PyQt5.QtWidgets import *
from calculator import Ui_MainWindow
import sys
import math

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.textChanged.connect(self.warning)
        self.setWindowTitle('Calculator')
        # ===============
        self.curr = ''
        # ===============
        self.pushButton_num1.clicked.connect(lambda : self.update('1'))
        self.pushButton_num0.clicked.connect(lambda : self.update('0'))
        self.pushButton_num9.clicked.connect(lambda : self.update('9'))
        self.pushButton_bracketl.clicked.connect(lambda : self.update('('))
        self.pushButton_clear.clicked.connect(lambda : self.update('C'))
        self.pushButton_pi.clicked.connect(lambda : self.update('pi')) 
        self.pushButton_num4.clicked.connect(lambda : self.update('4')) 
        self.pushButton_div.clicked.connect(lambda : self.update('/')) 
        self.pushButton_num5.clicked.connect(lambda : self.update('5')) 
        self.pushButton_num8.clicked.connect(lambda : self.update('8')) 
        self.pushButton_pow.clicked.connect(lambda : self.update('**')) 
        self.pushButton_bracketr.clicked.connect(lambda : self.update(')'))
        self.pushButton_num6.clicked.connect(lambda : self.update('6')) 
        self.pushButton_percent.clicked.connect(lambda : self.update('/100'))
        self.pushButton_mod.clicked.connect(lambda : self.update('%')) 
        self.pushButton_res.clicked.connect(lambda : self.update('=')) 
        self.pushButton_root.clicked.connect(lambda : self.update('**.5')) 
        self.pushButton_dot.clicked.connect(lambda : self.update('.')) 
        self.pushButton_num3.clicked.connect(lambda : self.update('3')) 
        self.pushButton_num2.clicked.connect(lambda : self.update('2')) 
        self.pushButton_num7.clicked.connect(lambda : self.update('7')) 
        self.pushButton_mul.clicked.connect(lambda : self.update('*')) 
        self.pushButton_sub.clicked.connect(lambda : self.update('-')) 
        self.pushButton_add.clicked.connect(lambda : self.update('+')) 
        # ===============
        self.show()
    def update(self,val):
        if val == 'pi':
            self.curr += str(math.pi)
        elif val == 'C':
            self.curr = self.curr[:-1]
        elif val == '=':
            self.calc()
        else:
            self.curr += val
        self.change_edit()

    def warning(self):
        self.curr = self.lineEdit.text()

    def change_edit(self):
        self.lineEdit.setText(self.curr )

    def calc(self):
        res = eval(self.curr)
        w = f'{self.curr} = {res}'
        self.curr = str(res)
        self.change_edit()
        self.textBrowser.setText(w)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    app.exec_()