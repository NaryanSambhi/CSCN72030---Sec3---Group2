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

from PyQt5.QtCore import QTimer
import random

from general_functions import *


def checkAge(age):
    if (age > 99):
        return False
    if (age < 18):
        return False
    else:
        return True
        
def checkWeight(weight):
    if (weight > 700):
        return False
    if (weight < 22):
        return False
    else:
        return True

def checkHeight(height):
    if (height > 274):
        return False
    if (height < 50):
        return False
    else:
        return True
    
def checkTemperature(temp):
    if (temp > 150):
        return False
    if (temp < 0):
        return False
    else:
        return True
    
def checkFluid(fluid):
    if (fluid > 10000):
        return False
    if (fluid < 0):
        return False
    else:
        return True


########################################################## GENERAL FUNCTIONS ##########################################################

#create user object to be filled out with new users
#our currently used - user object is loaded and modified here
logged_in_user = UserData(name="", age=0)

#assigning a random heart rate to a user to simulate a real users heart rate
def simulate_heart(self):
    dyanmic_heart = (random.randint(40, 120))
    logged_in_user.heart_health.set_hr(dyanmic_heart)      
    current = logged_in_user.heart_health.get_hr()
    
    self.DISPLAY_HEART.setText("Heart-rate: " + str(current))
    
def simulate_blood_oxygen(self):
    dynamic_blood_oxygen = random.randint(90, 100)
    logged_in_user.heart_health.set_bo(dynamic_blood_oxygen)
    current_blood_oxygen = logged_in_user.heart_health.get_bo()
    
    self.DISPLAY_BLOOD_OXYGEN.setText("Blood Oxygen: " + str(current_blood_oxygen))


def simulate_blood_pressure(self):
    pressure = random.randint(70, 150)
    logged_in_user.heart_health.set_bp(pressure)
    current_pressure = logged_in_user.heart_health.get_bp()
    
    self.DISPLAY_BLOOD_PRESSURE.setText("Blood Pressure: " + str(current_pressure))


#close current widget and go back to new widget
    #used for update values widgets in order to reopen a refreshed version of the previous page with new values shown
def GoBack(self, new_widget):        
   widget.removeWidget(self)
   widget.addWidget(new_widget)
   widget.setCurrentIndex(widget.currentIndex() + 1)
   
#go to new widget
def GoTo(new_widget):       
    widget.addWidget(new_widget)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    
#go to new widget
def GoToAndRemove(self, new_widget):       
    widget.removeWidget(self)
    widget.addWidget(new_widget)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    
    
 #displays the BMI values currently   
def DisplayBMI(self):
    
        #height and weight
        height = logged_in_user.BMI.get_height()
        weight = logged_in_user.BMI.get_weight()
        
        #bmi
        logged_in_user.BMI.calculate_bmi(height, weight)
        bmi = logged_in_user.BMI.get_bmi()
        
        self.DISPLAY_BMI.setText("BMI: " + str(bmi))
        
        #status
        bmi_status = logged_in_user.BMI.get_bmi_status()
        self.DISPLAY_BMI_STATUS.setText(str(bmi_status))
        
    
     
########################################################## Graphic User Interface ##########################################################

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
        GoTo(login)
        
    def gotocreate(self):
        create = CreateScreen()
        GoTo(create)


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
        
        #check if passwords match
        if password != password2:   
            self.accountError.setText("Passwords dont match")
            return
        
        
        #bugged function doesnt work:
        
        #make sure username isnt already taken
        with open("UserDBS.csv", mode="r", newline="") as f:
            reader = csv.reader(f, delimiter=",")

            # Check if the email is already taken
            for row in reader:
                if row and row[0] == user:
                    self.accountError.setText("Username is already taken")
                    return
        
        #open to save
        with open("UserDBS.csv",mode="a", newline="") as f:
            writer = csv.writer(f,delimiter=",") #, useed to sep entries
            writer.writerow([user, password, userSave]) #write in order
                              
            CreateUser = CreateUserProfile(userSave)
            GoToAndRemove(self, CreateUser)
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
        NewUser.set_Save_Path(self.userSave)
        
        
        #verify  
        if not all([UserName, UserAge, UserWeight, UserHeight]):
            self.accountError.setText("Please fill out all forms.")
            return

        if not (is_int(UserAge)):
            self.accountError.setText("Age must be a whole number")
            return

        if not(is_float(UserWeight) and is_float(UserHeight)):
            self.accountError.setText("Weight and height must be numeric.")
            return
        
        Age = checkAge(float(UserAge))
        Weight = checkWeight(float(UserWeight))
        Height = checkHeight(float(UserHeight))
        
        if Age or Weight or Height == False:
            self.accountError.setText("Please put reasonable inputs")
            return
        
        self.accountError.setText("")

        
        NewUser.BMI.set_height(float(UserHeight))
        NewUser.BMI.set_weight(float(UserWeight))

        #save person object and save to file
        print(NewUser)
        
        self.accountError.setText("")
        NewUser.save_to_file(self.userSave)
        
        login = LoginScreen()        
        GoToAndRemove(self, login)
        



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
                    home = Home()
                    GoToAndRemove(self, home)
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
    
        #images
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
        qpixmap = QPixmap('UI/bmipic.png')
        self.BMIpic.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/handwave.png')
        self.welcome.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/gears.png')
        self.Setting.setPixmap(qpixmap)
        
        #name
        name = logged_in_user.get_name()
        self.Name.setText("Welcome " + name)
        
        
        #Display current prediction on status
        
        HR = logged_in_user.heart_health.checkHRFlag()
        BO = logged_in_user.heart_health.checkBOFlag()
        BP = logged_in_user.heart_health.checkBPFlag()
        TEMP = logged_in_user.body_Info.checkTempFlag()
        FLUID = logged_in_user.body_Info.checkFluidFlag()

        output = logged_in_user.Prediction_Engine.Predict(HR, BO, BP, TEMP, FLUID)
        
        #print flags
        self.Status.setText(output)

        #dynamic heart-rate values being updated and displayed on timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000) # 1000 ms = 1 second        
        self.update_label()
        
        
        

        #Display the current BMI info
        DisplayBMI(self)
        
        
        #temp and fluid
        
        temp = logged_in_user.body_Info.get_temp()
        self.DISPLAY_TEMP.setText("Temperature: " + str(temp))

 
        
        #buttons
        self.Medication.clicked.connect(self.GoToPrescriptionManager)
        self.BMI.clicked.connect(self.GoToBMI)
        self.Heart.clicked.connect(self.GoToHeartHealth)
        self.Body.clicked.connect(self.GoToBodyStatus)
        self.setting.clicked.connect(self.GoToSetting)
        
    def update_label(self):        
        simulate_heart(self)


#navigation links (doesnt close current as we will go back often)
    def GoToPrescriptionManager(self):
        PHS = PrescriptionManager()
        GoToAndRemove(self, PHS)
    
    def GoToBMI(self):
        bmi = BMI()
        GoToAndRemove(self, bmi)
        
    def GoToHeartHealth(self):
        heart = HeartHealth()
        GoToAndRemove(self, heart)

    def GoToBodyStatus(self):
        body_status = BodyStatus()
        GoToAndRemove(self, body_status)

    def GoToSetting(self):
        setting = Setting()
        GoToAndRemove(self, setting)

#setting class
class Setting(QtWidgets.QMainWindow):
    def __init__(self):
        super(Setting, self).__init__()
        loadUi("UI/PHS_setting.ui", self)
        self.GoBack.clicked.connect(self.Back)
        
        #images
        qpixmap = QPixmap('UI/person.png')
        self.profile.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/blackheart.png')
        self.heart.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/temperature.png')
        self.bodyinfo.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/scale.png')
        self.BMI.setPixmap(qpixmap)

        #buttons
        self.GoBack.clicked.connect(self.Back)
        
        # go back to homepage
    def Back(self):         
        home = Home()
        GoBack(self, home)
 
#prescription manager     
class PrescriptionManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(PrescriptionManager, self).__init__()
        loadUi("UI/PHS_prescription.ui", self)
        self.GoBack.clicked.connect(self.Back)

        #buttons
        self.GoBack.clicked.connect(self.Back)       
        self.UpdateValues.clicked.connect(self.UpdatePrescription)

    def Back(self): 
        home = Home()
        GoToAndRemove(self, home)
        
    def UpdatePrescription(self):               
        med = UpdatePrescription()
        GoToAndRemove(self, med)  

class UpdatePrescription(QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdatePrescription, self).__init__()
        loadUi("UI/input_Prescriptions.ui", self)
        
        self.GoBack.clicked.connect(self.Back)

    def Back(self):         
        body = PrescriptionManager()
        GoBack(self, body)
       
#bmi class 
class BMI(QtWidgets.QMainWindow):
    def __init__(self):
        super(BMI, self).__init__()
        loadUi("UI/PHS_BMI.ui", self)
        
        #display and calculate values to GUI        

        #height and weight
        height = logged_in_user.BMI.get_height()
        self.DISPLAY_HEIGHT.setText(str(height) + " cm")
        weight = logged_in_user.BMI.get_weight()
        self.DISPLAY_WEIGHT.setText(str(weight) + " Kilograms")

        #display the current BMI values       
        DisplayBMI(self)

        #images
        qpixmap = QPixmap('UI/ruler.png')
        self.rulerpic.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/person.png')
        self.person.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/scale.png')
        self.bmi.setPixmap(qpixmap)

        #buttons
        self.GoBack.clicked.connect(self.Back)       
        self.UpdateValues.clicked.connect(self.UpdateBMI)
        
    def Back(self): 
        home = Home()
        GoToAndRemove(self, home)
            
    #go to the update page
    def UpdateBMI(self):               
        bmi = UpdateBMI()
        GoToAndRemove(self, bmi)       

#update the BMI values   
class UpdateBMI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdateBMI, self).__init__()
        loadUi("UI/input_BMI.ui", self)
        
        
        qpixmap = QPixmap('UI/person.png')
        self.person.setPixmap(qpixmap)
        
        qpixmap = QPixmap('UI/scale.png')
        self.bmi.setPixmap(qpixmap)
        
        qpixmap = QPixmap('UI/ruler.png')
        self.rulerpic.setPixmap(qpixmap)
        
        #display current bmi        
        DisplayBMI(self)

        #buttons
        self.GoBack.clicked.connect(self.Back)
        self.Apply_Height.clicked.connect(self.ApplyHeight)
        self.Apply_Weight.clicked.connect(self.ApplyWeight)

    #function to change the height
    def ApplyHeight(self):
        
        #apply height to object and save object
        height = self.New_Height.text()
        
        if not(is_float(height)):
            self.HeightError.setText("Height must be numeric.")
            return
        
        CheckHeight = checkHeight(float(height))

        if  CheckHeight == False:
            self.HeightError.setText("Please put reasonable inputs")
            return
                
        self.HeightError.setText("")

        #saved to the file
        logged_in_user.BMI.set_height(float(height))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
        
        
        #display current bmi
        DisplayBMI(self)

        
    #function to change the weight 
    def ApplyWeight(self):
        
        #apply height to object and save object
        weight = self.New_Weight.text()
        
        if not(is_float(weight)):
            self.WeightError.setText("Weight must be numeric.")
            return
        
        Checkweight = checkHeight(float(weight))

        if  Checkweight == False:
            self.WeightError.setText("Please put reasonable inputs")
            return
        
        self.WeightError.setText("")
        
        #save to the file 
        logged_in_user.BMI.set_weight(float(weight))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
        
        
        #display current bmi
        DisplayBMI(self)
    
    #go back to the BMi class
    def Back(self):         
        bmi = BMI()
        GoBack(self, bmi)
 
#heart class     
class HeartHealth(QtWidgets.QMainWindow):
    def __init__(self):
        super(HeartHealth, self).__init__()
        loadUi("UI/PHS_Heart_Health.ui", self)

        #pictures
        qpixmap = QPixmap('UI/bloodpressure.png')
        self.bloodpressure.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/bloodoxygen.png')
        self.bloodoxygen.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/heart.png')
        self.heartrate.setPixmap(qpixmap)


        #buttons
        self.GoBack.clicked.connect(self.Back)        
        
        #dynamic values
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000) # 1000 ms = 1 second

        self.update_label()


    def Back(self): 
        home = Home()
        GoToAndRemove(self, home)
            
    def update_label(self):
        simulate_heart(self)
        simulate_blood_pressure(self)
        simulate_blood_oxygen(self)


#body status class
  
class BodyStatus(QtWidgets.QMainWindow):
    def __init__(self):
        super(BodyStatus, self).__init__()
        loadUi("UI/PHS_Body_Info.ui", self)
        
        #images
        qpixmap = QPixmap('UI/temperature.png')
        self.bodytemp.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/bodyfluid.png')
        self.bodyfluid.setPixmap(qpixmap)
        
        
        
        #height and weight
        temprature = logged_in_user.body_Info.get_temp()
        self.DISPLAY_TEMPRATURE.setText(str(temprature))
        
        
        
        fluid = logged_in_user.body_Info.get_fluid()
        self.DISPLAY_FLUID.setText(str(fluid))

         #buttons
        self.GoBack.clicked.connect(self.Back)       
        self.UpdateValues.clicked.connect(self.UpdateBody)
        
    def Back(self): 
        home = Home()
        GoToAndRemove(self, home)
            
    #go to the update body page
    def UpdateBody(self):               
        body = UpdateBody()
        GoToAndRemove(self, body)  

#update body values 
class UpdateBody(QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdateBody, self).__init__()
        loadUi("UI/input_Body_Info.ui", self)
        
        #images
        qpixmap = QPixmap('UI/temperature.png')
        self.Temperature.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/bodyfluid.png')
        self.IV.setPixmap(qpixmap)

        
        self.GoBack.clicked.connect(self.Back)
        
        
        
        #buttons
        self.GoBack.clicked.connect(self.Back)
        self.Apply_Temperature.clicked.connect(self.ApplyTemperature)
        self.Apply_Fluid.clicked.connect(self.ApplyFluid)

    #function to change the height
    def ApplyTemperature(self):
        
        #apply height to object and save object
        Temprature = self.New_Temperature.text()
        
        if not(is_float(Temprature)):
            self.TempratureError.setText("Temprature must be numeric.")
            return
        
        
        CheckTemprature = checkHeight(float(Temprature))

        if  CheckTemprature == False:
            self.TempratureError.setText("Please put reasonable inputs")
            return
        
        
        self.TempratureError.setText("")

        #saved to the file
        logged_in_user.body_Info.set_temp(float(Temprature))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
        
        
    #function to change the weight 
    def ApplyFluid(self):
        
        #apply height to object and save object
        Fluid = self.New_Fluid.text()
        
        if not(is_float(Fluid)):
            self.FluidError.setText("Fluid must be numeric.")
            return
        
        CheckFluid = checkHeight(float(Fluid))

        if  CheckFluid == False:
            self.FluidError.setText("Please put reasonable inputs")
            return
        
        
        self.FluidError.setText("")
        
        #save to the file 
        logged_in_user.body_Info.set_fluid(float(Fluid))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
        
        
    
    #go back to the body status page
    def Back(self):         
        body = BodyStatus()
        GoBack(self, body)
      
        
########################################################## MAIN ##########################################################
        
#main 
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(1280)
widget.setFixedWidth(720)

widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")