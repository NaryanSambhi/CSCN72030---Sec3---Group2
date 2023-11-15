#Software Development Lifecycle Project 3
# Naryan Sambhi 

# main run and GUI using functions to create working application 



import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget

import csv 

#GUI OBJECTS

#welcome screen to login or create account
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("login_or_create.ui", self)
        self.Login.clicked.connect(self.gotologin)
        self.Account.clicked.connect(self.gotocreate)

        
    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
    def gotocreate(self):
        create = CreateScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)


class CreateScreen(QDialog):
    def __init__(self):
        super(CreateScreen, self).__init__()
        loadUi("create.ui", self)
        
        
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Confirm.setEchoMode(QtWidgets.QLineEdit.Password)

        
        self.SignUp.clicked.connect(self.registerfunction)
        
        
    def registerfunction(self):    
        user = self.Email.text()
        password = self.Password.text()
        password2 = self.Confirm.text()
        
        with open("UserDBS.csv",mode="a", newline="") as f:
            writer = csv.writer(f,delimiter=",")
            

            if password == password2:   
                writer.writerow( [user, password])
                self.accountError.setText("")
                
                print("creating account")
                
            else: 
                    self.accountError.setText("your passwords dont match")
        
        
        

#login 
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)    
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        
        
        self.LoginAccount.clicked.connect(self.loginfunction)
        
        
    
    def loginfunction(self):
        user = self.Email.text()
        password = self.Password.text()
        
        print(user, password)
        
        # errors
        if len(user) == 0 or len(password) == 0:
            self.loginError.setText("Please fill out the entire form")
            return
            
        with open("UserDBS.csv", mode="r", encoding="utf-8-sig") as f:
            reader = csv.reader(f, delimiter=",")
            
            for row in reader:
                # Check if both user and password match
                if row[0] == user and row[1] == password:
                    print("Logging in")  
                    self.loginError.setText("")

                    # Add your logic to proceed after successful login
                    return
        
        # If no match found
        self.loginError.setText("Invalid credentials")
        
        
        
        
        
        
        
#main 
app = QApplication(sys.argv)
welcome=WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(1280)
widget.setFixedWidth(720)

widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")