# from PyQt6.QtWidgets import *
# import sys
# if __name__=='__main__':
#     app = QApplication(sys.argv)
#     wind = QLineEdit()
#     wind.show()
#     txt = QTextEdit()
#     scr = QApplication.primaryScreen()
#     x=scr.size().width()//2-txt.width()//2
#     y=scr.size().height()//2-txt.height()//2
#     txt.move(x,y)
 
#     app.exec()

from PyQt6.QtWidgets import *
import sys
from widgets.regw import *
if __name__=='__main__':
    app=QApplication(sys.argv)
    regWn=RegWindow()
    regWn.show()
    app.exec()