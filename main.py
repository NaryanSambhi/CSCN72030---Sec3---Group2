#Software Development Lifecycle Project 3
# Naryan Sambhi 

# main run and GUI using functions to create working application 

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget
from PyQt5.QtGui import QPixmap

import csv 

from UserData import *

#create user object to be filled out with new users
logged_in_user = UserData(name="", age=0)


#makes sure input values are numbers only 
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
    
#GUI OBJECTS
#welcome screen to login or create account
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("UI/login_or_create.ui", self)
        self.Login.clicked.connect(self.gotologin)
        self.Account.clicked.connect(self.gotocreate)

#navigation functions
    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotocreate(self):
        create = CreateScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)


#creating a new account screen
class CreateScreen(QDialog):
    def __init__(self):
        super(CreateScreen, self).__init__()
        loadUi("UI/create.ui", self)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignUp.clicked.connect(self.registerfunction)
        self.GoBack.clicked.connect(self.Back)
        
#register a new account to DBS
    def registerfunction(self):    
        
        #vars
        user = self.Email.text().lower()
        password = self.Password.text()
        password2 = self.Confirm.text()
        
        #organize a save file name into ours  
        userSave = "saves/" + sanitize_filename(user) + '.pkl'
        
        #checking forum and passwords 
        if len(user) == 0 or len(password) == 0 or len(password2) == 0:
            self.accountError.setText("Please fill out the entire form")
            return
        
        if password != password2:   
            self.accountError.setText("Passwords dont match")
            return
        
        
        #bugged function doesnt work:
        """
        #make sure username isnt already taken
        with open("UserDBS.csv", mode="r", newline="") as f:
            reader = csv.reader(f, delimiter=",")

            # Check if the email is already taken
            for row in reader:
                if row and row[0] == user:
                    self.accountError.setText("Username is already taken")
                    return
         """
        
        #open to save
        with open("UserDBS.csv",mode="a", newline="") as f:
            writer = csv.writer(f,delimiter=",") #, useed to sep entries
            writer.writerow([user, password, userSave]) #write in order
                              
            #close current window open next window
            self.close()
            CreateUser = CreateUserProfile(userSave)
            widget.addWidget(CreateUser)            
            widget.setCurrentIndex(widget.currentIndex()+1)
            return
        
    def Back(self): 
        widget.removeWidget(self)

#creates user profile after login including making a save file
class CreateUserProfile(QDialog):
    def __init__(self, user_save):
        super(CreateUserProfile, self).__init__()
        loadUi("UI/createUser.ui", self)    
        self.SignUp.clicked.connect(self.CreateFunction)
        self.userSave = user_save

#create new user
    def CreateFunction(self):
        
        #vars
        UserName = self.Name.text()
        UserAge = self.Age.text()
        UserWeight = self.Weight.text()
        UserHeight = self.Height.text()
        
        #assign to object
        NewUser = UserData(name=UserName, age=UserAge)
        
        NewUser.BMI.set_height(UserHeight)
        NewUser.BMI.set_weight(UserWeight)
        NewUser.set_Save_Path(self.userSave)
        
        #verify  
        if not all([UserName, UserAge, UserWeight, UserHeight]):
            self.accountError.setText("Please fill out all forms.")
            return

        if not (is_int(UserAge) and is_int(UserWeight) and is_int(UserHeight)):
            self.accountError.setText("Age, Weight, and Height must be numeric.")
            return

        #save person object and save to file
        print(NewUser)
        
        self.accountError.setText("")
        NewUser.save_to_file(self.userSave)
        
        self.close()
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)



#login 
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("UI/login.ui", self)    
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LoginAccount.clicked.connect(self.loginfunction)
        self.GoBack.clicked.connect(self.Back)

        
    #check login details to DBS
    def loginfunction(self):
        
        #vars
        user = self.Email.text().lower()
        password = self.Password.text()
        print(user, password)
        
        # error checks
        if len(user) == 0 or len(password) == 0:
            self.loginError.setText("Please fill out the entire form")
            return
            
        #open and find user
        with open("UserDBS.csv", mode="r", encoding="utf-8-sig") as f:
            reader = csv.reader(f, delimiter=",")
            
            for row in reader:
                # Check if both user and password match
                if row[0] == user and row[1] == password:
                    print("Logging in")                                    
                    
                    self.loginError.setText("")
                    
                    #intialize objects from save file
                    try: 
                        user_save = row[2]
                        logged_in_user.load_from_file(user_save)
                        print("loaded", logged_in_user)
                    except:
                        self.loginError.setText("Error loading user")
                        return
                    
                    #open window to homepage
                    self.close()
                    home = Home()
                    widget.addWidget(home)
                    widget.setCurrentIndex(widget.currentIndex() + 1)         
                    return
        
        # If no match found
        self.loginError.setText("Invalid credentials")
        
        
    def Back(self): 
        widget.removeWidget(self)
        
        
#homepage
class Home(QtWidgets.QMainWindow):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("UI/PHS_homepage.ui", self)
    
        #inmages
        qpixmap = QPixmap('UI/Pill_Bottle.png')
        self.medpic.setPixmap(qpixmap)

        qpixmap = QPixmap('UI/heart.png')
        self.heartpic.setPixmap(qpixmap)

        qpixmap = QPixmap('UI/person.png')
        self.personpic.setPixmap(qpixmap)

        qpixmap = QPixmap('UI/blackheart.png')
        self.blackheart.setPixmap(qpixmap)

        qpixmap = QPixmap('UI/temperature.png')
        self.bodyinfo.setPixmap(qpixmap)

        qpixmap = QPixmap('UI/scale.png')
        self.scale.setPixmap(qpixmap)
        
        #buttons
        
        self.Medication.clicked.connect(self.GoToPrescriptionManager)
        self.BMI.clicked.connect(self.GoToBMI)
        self.Heart.clicked.connect(self.GoToHeartHealth)
        self.Body.clicked.connect(self.GoToBodyStatus)

        

#navigation links (doesnt close current as we will go back often)
    def GoToPrescriptionManager(self):
        PHS = PrescriptionManager()
        widget.addWidget(PHS)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def GoToBMI(self):
        bmi = BMI()
        widget.addWidget(bmi)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
    def GoToHeartHealth(self):
        heart = HeartHealth()
        widget.addWidget(heart)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def GoToBodyStatus(self):
        body_status = BodyStatus()
        widget.addWidget(body_status)
        widget.setCurrentIndex(widget.currentIndex() + 1)     

        
#prescription manager     
class PrescriptionManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(PrescriptionManager, self).__init__()
        loadUi("UI/PHS_prescription.ui", self)
        self.GoBack.clicked.connect(self.Back)

    def Back(self): 
        widget.removeWidget(self)
        
        
#bmi class 
class BMI(QtWidgets.QMainWindow):
    def __init__(self):
        super(BMI, self).__init__()
        loadUi("UI/PHS_BMI.ui", self)
        
        
        #commented out until standardized units are picked
        height = logged_in_user.BMI.get_height()
        self.DISPLAY_HEIGHT.setText(str(height) + " Feet")

        weight = logged_in_user.BMI.get_weight()
        self.DISPLAY_WEIGHT.setText(str(weight) + " Pounds")
        

        
        #bmi = logged_in_user.BMI.get


        #images
        qpixmap = QPixmap('UI/ruler.png')
        self.rulerpic.setPixmap(qpixmap)

        qpixmap = QPixmap('UI/person.png')
        self.person.setPixmap(qpixmap)
        
        qpixmap = QPixmap('UI/scale.png')
        self.bmi.setPixmap(qpixmap)

        self.GoBack.clicked.connect(self.Back)
        
        self.UpdateValues.clicked.connect(self.UpdateBMI)
        
    def Back(self): 
        widget.removeWidget(self)
        
    def UpdateBMI(self):      
        
        widget.removeWidget(self)

         
        bmi = UpdateBMI()
        widget.addWidget(bmi)
        widget.setCurrentIndex(widget.currentIndex() + 1)     
        
        
class UpdateBMI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdateBMI, self).__init__()
        loadUi("UI/input_BMI.ui", self)
        
        
        qpixmap = QPixmap('UI/person.png')
        self.person.setPixmap(qpixmap)
        
        qpixmap = QPixmap('UI/scale.png')
        self.bmi.setPixmap(qpixmap)
        
        self.GoBack.clicked.connect(self.Back)
        self.Apply_Height.clicked.connect(self.ApplyHeight)
        self.Apply_Weight.clicked.connect(self.ApplyWeight)


    def ApplyHeight(self):
        
        #apply height to object and save object
        height = self.New_Height.text()
        logged_in_user.BMI.set_height(height)
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
        

    def ApplyWeight(self):
        
        #apply height to object and save object
        weight = self.New_Weight.text()
        logged_in_user.BMI.set_weight(weight)
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)


    def Back(self):         
        widget.removeWidget(self)
        bmi = BMI()
        widget.addWidget(bmi)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
        

            
        
    

#heart class     
   
class HeartHealth(QtWidgets.QMainWindow):
    def __init__(self):
        super(HeartHealth, self).__init__()
        loadUi("UI/PHS_Heart_Health.ui", self)

        qpixmap = QPixmap('UI/bloodpressure.png')
        self.bloodpressure.setPixmap(qpixmap)
        
        qpixmap = QPixmap('UI/bloodoxygen.png')
        self.bloodoxygen.setPixmap(qpixmap)
        
        qpixmap = QPixmap('UI/heart.png')
        self.heartrate.setPixmap(qpixmap)

        self.GoBack.clicked.connect(self.Back)

        
    def Back(self): 
        widget.removeWidget(self)
        


#body status class
  
class BodyStatus(QtWidgets.QMainWindow):
    def __init__(self):
        super(BodyStatus, self).__init__()
        loadUi("UI/PHS_Body_Info.ui", self)

        qpixmap = QPixmap('UI/temperature.png')
        self.bodytemp.setPixmap(qpixmap)
        
        qpixmap = QPixmap('UI/bodyfluid.png')
        self.bodyfluid.setPixmap(qpixmap)

        self.GoBack.clicked.connect(self.Back)

        
    def Back(self): 
        widget.removeWidget(self)
        

        
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