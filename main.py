#Software Development Lifecycle Project 3
# Naryan Sambhi 

# main run and GUI using functions to create working application 



import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget



#GUI OBJECTS

#welcome screen to login or create account
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("login_or_create.ui", self)
        self.Login.clicked.connect(self.gotologin)
        
    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


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
        

        #errors 
        if len(user)==0 or len(password)==0:
            self.loginError.setText("Please fill out the entire form")
            return
            
            
        #log in code  
                #should be from file or DBS
                
        if user == "john" and password == "123": #will be changed after testing phase
            print("Logging in")  
            self.loginError.setText("")

            #login = LoginScreen()
            #widget.addWidget(login)
            #widget.setCurrentIndex(widget.currentIndex()+1) 
        
        #failure code 
        else:        
            self.loginError.setText("Invalid Login")

        
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