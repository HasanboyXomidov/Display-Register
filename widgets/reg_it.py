from PyQt6.QtWidgets import *
from PyQt6 import QtGui
from PyQt6.QtCore import *
import typing
from aiogram import Dispatcher,Bot,types,executor
import requests
import re

      
            
class RegWindow(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.setUpWindow()
        self.cancel_button.clicked.connect(QApplication.quit)
        self.send_button.clicked.connect(self.send_click1 and self.check_name_g and self.check_email_g and self.check_telegram_id_t )
        self.send_button.clicked.connect(self.check_all)

    def setUpWindow(self):
        



        # t_pl=QSplitter(Qt.Orientation.Horizontal)

        self.lbl_name=QLabel("Ismingizni kiriting : ")
        self.name_edit=QLineEdit()
        self.name_edit.setPlaceholderText("Hasanboy")


        self.lbl_email=QLabel("Email kiriting : ")
        self.email_edit=QLineEdit()
        self.email_edit.setPlaceholderText("abcd@gmail.com")

        self.lbl_password=QLabel("Parolingizni kirintg : ")
        self.password_edit=QLineEdit()
        self.password_edit.setPlaceholderText("Parolingizni kiritng : ")
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)

        self.lbl_telegram=QLabel("Telegram ID : ")
        self.telegram_edit=QLineEdit()
        self.telegram_edit.setPlaceholderText("ID")

        

        self.check=QCheckBox("I accept all cookies")
        self.check.setChecked(False)

        self.send_button=QPushButton("Jo'natish")
        self.cancel_button=QPushButton("Bekor qilish")

        layout_send=QHBoxLayout()
        layout_send.addStretch()
        layout_send.addWidget(self.send_button)
        layout_send.addStretch()
        
        layout_cancel=QHBoxLayout()
        layout_cancel.addStretch()
        layout_cancel.addWidget(self.cancel_button)
        layout_cancel.addStretch()


        layout_check=QHBoxLayout()
        layout_check.addStretch()
        layout_check.addWidget(self.check)
        layout_check.addStretch()

        layout_name=QHBoxLayout()
        layout_name.addStretch()
        layout_name.addWidget(self.lbl_name)
        # layout_name.addWidget(t_pl)
        layout_name.addWidget(self.name_edit)
        layout_name.addStretch()

        

        layout_email=QHBoxLayout()
        layout_email.addStretch()
        layout_email.addWidget(self.lbl_email)
        layout_email.addWidget(self.email_edit)
        layout_email.addStretch()

        layout_password=QHBoxLayout()
        layout_password.addStretch()
        layout_password.addWidget(self.lbl_password)
        layout_password.addWidget(self.password_edit)
        layout_password.addStretch()

        layout_telegram=QHBoxLayout()
        layout_telegram.addStretch()
        layout_telegram.addWidget(self.lbl_telegram)
        layout_telegram.addWidget(self.telegram_edit)
        layout_telegram.addStretch()

        # layout_check=QHBoxLayout()
        # layout_check.addStretch()
        # layout_check.addWidget(self.check)
        # layout_check.addStretch()


        layout_v=QVBoxLayout()
        layout_v.addStretch()
        layout_v.addLayout(layout_name)
        layout_v.addLayout(layout_email)
        layout_v.addLayout(layout_password)
        layout_v.addLayout(layout_telegram)
        layout_v.addStretch(4)
        layout_v.addLayout(layout_check)
        layout_v.addLayout(layout_send)
        layout_v.addLayout(layout_cancel)
        # layout_v.addStretch()




        center=QWidget()
        center.setLayout(layout_v)
        self.setCentralWidget(center)

    
    



    
    def check_telegram_id(self):
        telegram_id=self.telegram_edit.text()
        send_message=f"Assalomu alekum siz bizning dasturdan ruyxatdan utdingiz\nSizning emailingiz : {self.email_edit.text()}\nSizning kirish uchung parolingiz : {self.password_edit.text()} !! Malumotlaringizni esdan chiqarmang "
        url=f"https://api.telegram.org/bot6118223345:AAHjYDnUYVhsP4tmC7vUvIPvbLC2VL4gNow/sendMessage?chat_id={telegram_id}&text={send_message}"
        response = requests.post(url)
        print(response.json())
        if response.status_code==200:
             return True
        else:
             return False
    def check_telegram_id_t(self):
        if self.check_telegram_id():
             pass
        else:
            QMessageBox.critical(self,"Xatolig","Telegram Id Topilmadi ")




    def check_data(self):
        td=self.telegram_edit
        

        return len(td.text()) ==8 and td.text().isdigit()
    def send_click1(self):
            if self.check_data():
                 pass
            else:
                QMessageBox.critical(self,"Xatolig","Telegram ID bunday bulishi mumkin emas")

                

    def check_name(self):
         ab=self.name_edit
         return ab.text().isalpha() and ab.text()[0].isupper()
    def check_name_g(self):
         if self.check_name():
              pass
         else:
              QMessageBox.critical(self,"Xatolig","Ism notugri kiritilgan")
    @staticmethod
    def check_email(self):
        abb=self.email_edit
        return re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+",abb.text())
    def check_email_g(self):
         if self.check_email(self):
              pass
         else:
              QMessageBox.critical(self,"Xatolig","Ism Email notugri kiritilgan")

    def check_all(self):
         if  self.check_data() and self.check_name() and self.check_email():
            #   QMessageBox.about(self,"Xabarnoma","Siz Muvofaqqiyatli Ruyxatdan utdingiz ")
            self.name_edit.clear()
            self.email_edit.clear()
            self.password_edit.clear()
            self.telegram_edit.clear()
            