from widgets.reg_it import *
from PyQt6.QtWidgets import *
import sys  
if __name__=='__main__':
    app=QApplication(sys.argv)
    regWn=RegWindow()
    regWn.setFixedSize(500,500)
    regWn.show()
    app.exec()