from PyQt6.QtWidgets import *
from PyQt6 import QtGui
from PyQt6.QtCore import *

import typing 
class RegWindow(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.setUpWindow()
    def setUpWindow(self):
        self.lbl_name=QLabel("Ismngizni kiriting : ")  
        self.name_edit=QLineEdit()
        self.name_edit.setPlaceholderText(" Hikmatillo ")
        
        layout = QHBoxLayout()
        layout.addWidget(self.lbl_name)
        layout.addWidget(self.name_edit)
        layout_em=QHBoxLayout()
        self.lbl_email=QLabel("Emailingizni kiriting : ")
        self.email_edit=QLineEdit()
        self.email_edit.setPlaceholderText("ism@gmail.com")
        layout_em.addWidget(self.lbl_email)
        layout_em.addWidget(self.email_edit)

        layout_pas=QHBoxLayout()
        self.lbl_pass=QLabel("Parolingizni kiriting : ")
        self.pass_edit = QLineEdit()
        self.pass_edit.setPlaceholderText("Parolni kiritng : ")
        self.pass_edit.setEchoMode(QLineEdit.EchoMode.Password)
        layout_pas.addWidget(self.lbl_pass)
        layout_pas.addWidget(self.pass_edit)
        v_lay=QVBoxLayout()
        v_lay.addLayout(layout)         
        v_lay.addLayout(layout_em)
        v_lay.addLayout(layout_pas)
        center=QWidget()
        center.setLayout(v_lay)
        self.setCentralWidget(center)

