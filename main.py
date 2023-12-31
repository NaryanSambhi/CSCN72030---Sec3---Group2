#Software Development Lifecycle Project 3
# Naryan Sambhi 

# main run and GUI using functions to create working application 

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QListWidget
from PyQt5.QtGui import QPixmap

import csv 

from UserData import *

from PyQt5.QtCore import QTimer
import random

from general_functions import *


########################################################## GENERAL FUNCTIONS ##########################################################

#create user object to be filled out with new users
#our currently used - user object is loaded and modified here
logged_in_user = UserData(name="", age=0)

#assigning a random heart rate to a user to simulate a real users heart rate
def simulate_heart(self):
    dynamic_heart = (random.randint(logged_in_user.heart_health.get_hr()-5, logged_in_user.heart_health.get_hr()+5))
    if (dynamic_heart <= 70):
        dynamic_heart = 70
    if (dynamic_heart >= 110):
        dynamic_heart = 110
    logged_in_user.heart_health.set_hr(dynamic_heart)      
    current = logged_in_user.heart_health.get_hr()
    
    self.DISPLAY_HEART.setText("Heart-rate: " + str(current))
    
def simulate_blood_oxygen(self):
    dynamic_blood_oxygen = random.randint(logged_in_user.heart_health.get_bo()-2, logged_in_user.heart_health.get_bo()+2)
    if (dynamic_blood_oxygen <= 90):
        dynamic_blood_oxygen = 90
    if (dynamic_blood_oxygen >=100):
        dynamic_blood_oxygen = 100
    logged_in_user.heart_health.set_bo(dynamic_blood_oxygen)
    current_blood_oxygen = logged_in_user.heart_health.get_bo()
    
    self.DISPLAY_BLOOD_OXYGEN.setText("Blood Oxygen: " + str(current_blood_oxygen))


def simulate_blood_pressure(self):
    dynamic_blood_pressure = random.randint(logged_in_user.heart_health.get_bp()-6, logged_in_user.heart_health.get_bp()+6)
    if (dynamic_blood_pressure <= 70):
        dynamic_blood_pressure = 70
    if (dynamic_blood_pressure >=150):
        dynamic_blood_pressure = 150
    logged_in_user.heart_health.set_bp(dynamic_blood_pressure)
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

#go to new widget
def GoToAndLogin(self, new_widget):       
    widget.removeWidget(self)
    widget.addWidget(new_widget)
    widget.setCurrentIndex(widget.currentIndex() - 100)
   
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
        
        
def DisplayJugs(self, Fluid):
       
        try:
            current = float(Fluid)
        except ValueError:
            # Handle the case when Fluid is not a valid number
            current = 0.0

        if current <= 2000:
            qpixmap = QPixmap('UI\\Jugs\\J1.png')
        elif 2001 <= current < 3000:
            qpixmap = QPixmap('UI\\Jugs\\J2.png')
        elif 3001 <= current <= 5000:
            qpixmap = QPixmap('UI\\Jugs\\J3.png')
        elif current >= 5001 and current <= 9000:
            qpixmap = QPixmap('UI\\Jugs\\J4.png')
        elif current > 9000:
            qpixmap = QPixmap('UI\\Jugs\\J5.png')
        else:
            # Add a default condition or handle it as per your requirement
            qpixmap = QPixmap('UI\\nojug.png')

        self.emptyjug.setPixmap(qpixmap)
        return

        
def DisplayTemp(self, Temp):    
    try:
        current = float(Temp)
    except ValueError:
        # Handle the case when Fluid is not a valid number
        current = 0.0    
    
    # Set a default value for qpixmap
    qpixmap = QPixmap('UI\\default_temp.png')

    if current <= 30:
        qpixmap = QPixmap('UI\Temp\T1.png')
    elif 70 >= current > 30:
        qpixmap = QPixmap('UI\\temperature.png')
    elif current > 70:
        qpixmap = QPixmap('UI\Temp\T2.png')

    self.bodytemp.setPixmap(qpixmap)
    return

     
########################################################## Graphic User Interface ##########################################################
def gotowelcome(self):
        welcome = WelcomeScreen()
        GoTo(welcome)

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
                
        # Make sure username isn't already taken
        with open("UserDBS.csv", mode="r", newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f, delimiter=",")

            # Check if the email is already taken
            for row in reader:
                print(f"Comparing user: {user} with row: {row}")

                if row and row[0].strip('ï»¿ ') == user.strip():
                    self.accountError.setText("Username is already taken")
                    return
        
        #open to save
        with open("UserDBS.csv",mode="a", newline="") as f:
            writer = csv.writer(f,delimiter=",") #, useed to sep entries
            writer.writerow([user, password, userSave]) #write in order
                                   
            #create a user save file now
            NewUser = UserData("", age=0)
            NewUser.set_Save_Path(userSave)
            
            NewUser.save_to_file(userSave)
                                          
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
        
        Age = checkAge(int(UserAge))
        Weight = checkWeight(float(UserWeight))
        Height = checkHeight(float(UserHeight))
        
        
        name = checkName(UserName)

        if  name == False:
            self.accountError.setText("Name is too large")
            return
        
        if Age == False or Weight == False or Height == False:
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
                        self.loginError.setText("Error loading user - please contact support")
                        return
                    
                    #open window to homepage
                    home = Home()
                    GoToAndRemove(self, home)
                    return
        
        # If no match found
        self.loginError.setText("Invalid credentials")
        
        
    def Back(self): 
        welcome = WelcomeScreen()
        GoToAndRemove(self, welcome) 
            
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

        
        qpixmap = QPixmap('UI/scale.png')
        self.scale.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/bmipic.png')
        self.BMIpic.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/handwave.png')
        self.welcome.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/gears.png')
        self.Setting.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/logout.png')
        self.logout.setPixmap(qpixmap)
        
        #name
        name = logged_in_user.get_name()
        self.Name.setText("Welcome " + name)
        
        

        #dynamic heart-rate values being updated and displayed on timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000) # 1000 ms = 1 second        
        self.update_label()
        
        
        

        #Display the current BMI info
        DisplayBMI(self)
        
        
        #temp and fluid
        
        temp = logged_in_user.body_Info.get_temp()
        self.DISPLAY_TEMP.setText(str(temp) + " c")

 
        DisplayTemp(self, temp)
        
        fluid = logged_in_user.body_Info.get_fluid()
        self.DISPLAY_FLUID.setText(str(fluid) + " mL")
        
        DisplayJugs(self, fluid)
        
        #buttons
        self.Medication.clicked.connect(self.GoToPrescriptionManager)
        self.BMI.clicked.connect(self.GoToBMI)
        self.Heart.clicked.connect(self.GoToHeartHealth)
        self.Body.clicked.connect(self.GoToBodyStatus)
        self.setting.clicked.connect(self.GoToSetting)
        self.GoBack.clicked.connect(self.Back)
        
    def update_label(self):        
        simulate_heart(self)
        simulate_blood_oxygen(self)
        simulate_blood_pressure(self)
        
        
        #Display current prediction on status
        
        HR = logged_in_user.heart_health.checkHRFlag()
        BO = logged_in_user.heart_health.checkBOFlag()
        BP = logged_in_user.heart_health.checkBPFlag()
        TEMP = logged_in_user.body_Info.checkTempFlag()
        FLUID = logged_in_user.body_Info.checkFluidFlag()

        output = logged_in_user.Prediction_Engine.Predict(HR, BO, BP, TEMP, FLUID)
        
        #print flags
        self.Status.setText(output)
            
    def Back(self):         
        login = LoginScreen()
        #GoBack(self, login)
        GoToAndLogin(self, login)


#navigation links (doesnt close current as we will go back often)
    def GoToPrescriptionManager(self):
        prescription = PrescriptionManager()
        GoToAndRemove(self, prescription)
    
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
        self.Settingprofile.clicked.connect(self.SettingProfile)
        self.Settingheart.clicked.connect(self.SettingHeart)
        self.Settingbodyinfo.clicked.connect(self.SettingBodyInfo)
        self.Conversions.clicked.connect(self.SettingBMI)
        
        # go back to homepage
    def Back(self):         
        home = Home()
        GoBack(self, home)

    def SettingProfile(self):               
        profile = SettingProfile()
        GoToAndRemove(self, profile) 

    def SettingHeart(self):               
        heart = SettingHeart()
        GoToAndRemove(self, heart) 

    def SettingBodyInfo(self):               
        body = SettingBodyInfo()
        GoToAndRemove(self, body) 

    def SettingBMI(self):               
        bmi = SettingBMI()
        GoToAndRemove(self, bmi) 

class SettingProfile(QtWidgets.QMainWindow):
    def __init__(self):
        super(SettingProfile, self).__init__()
        loadUi("UI/Setting_Profile.ui", self)
        self.GoBack.clicked.connect(self.Back)

        qpixmap = QPixmap('UI/handwave.png')
        self.handwave.setPixmap(qpixmap)
        qpixmap = QPixmap('UI/person.png')
        self.person.setPixmap(qpixmap)

        self.GoBack.clicked.connect(self.Back)

        self.Apply_Name.clicked.connect(self.ApplyName)
        self.Apply_Age.clicked.connect(self.ApplyAge)

    def ApplyName(self):
        
        #apply name to object and save object
        name = self.New_Name.text()

        Username = checkName(name)

        if  Username == False:
            self.NameError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.NameError.setText("Name too long")
            return
        if is_float(name) == True:
            self.NameError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.NameError.setText("No numbers")
            return
        if len(name) == 0:
            self.NameError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.NameError.setText("Need an actual input")
            return

        self.NameError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;")
        
        self.NameError.setText("Values have been changed")
            
                

        #saved to the file
        logged_in_user.set_name(name)
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def ApplyAge(self):
        
        #apply age to object and save object
        age = self.New_Age.text()

      #it is a string so cannot do float checks  
        if not(is_float(age)):
            self.AgeError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.AgeError.setText("Age must be numeric.")
            return
        

        user_age = checkAge(int(age))
     
        if user_age == False:
            # Set style sheet with red color and no border
            self.AgeError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.AgeError.setText("Please put reasonable inputs")
            return

        # Set style sheet with green color and no border
        self.AgeError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.AgeError.setText("Values have been changed")
                
        #saved to the file
        logged_in_user.set_age(age)
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def Back(self):         
        setting = Setting()
        GoBack(self, setting)

class SettingHeart(QtWidgets.QMainWindow):
    def __init__(self):
        super(SettingHeart, self).__init__()
        loadUi("UI/Setting_Heart.ui", self)
        self.GoBack.clicked.connect(self.Back)

        self.GoBack.clicked.connect(self.Back)

        self.Apply_Upper_Heart_Rate.clicked.connect(self.ApplyUpperHeartRate)
        self.Apply_Lower_Heart_Rate.clicked.connect(self.ApplyLowerHeartRate)

        self.Apply_Upper_Blood_Oxygen.clicked.connect(self.ApplyUpperBloodOxygen)
        self.Apply_Lower_Blood_Oxygen.clicked.connect(self.ApplyLowerBloodOxygen)

        self.Apply_Upper_Blood_Pressure.clicked.connect(self.ApplyUpperBloodPressure)
        self.Apply_Lower_Blood_Pressure.clicked.connect(self.ApplyLowerBloodPressure)

    def ApplyUpperHeartRate(self):
        
        #apply height to object and save object
        heartrate = self.New_Upper_Heart_Rate.text()
        
        if not(is_float(heartrate)):            
            self.HeartRateError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.HeartRateError.setText("Heart must be numeric.")
            return
        
        CheckHeartRate = checkHeartRate(float(heartrate))

        if  CheckHeartRate == False:
            
            self.HeartRateError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.HeartRateError.setText("Please put reasonable inputs")
            return

        self.HeartRateError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.HeartRateError.setText("Values have been changed")
                
        #self.HeartRateError.setText("")

        #saved to the file
        logged_in_user.heart_health.set_hrUL(float(heartrate))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def ApplyLowerHeartRate(self):
        
        #apply height to object and save object
        heartrate = self.New_Lower_Heart_rate.text()
        
        if not(is_float(heartrate)):            
            self.HeartRateError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.HeartRateError.setText("Heart must be numeric.")
            return
        
        CheckHeartRate = checkHeartRate(float(heartrate))

        if  CheckHeartRate == False:
            self.HeartRateError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.HeartRateError.setText("Please put reasonable inputs")
            return

        self.HeartRateError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.HeartRateError.setText("Values have been changed")

        #self.HeartRateError.setText("")

        #saved to the file
        logged_in_user.heart_health.set_hrLL(float(heartrate))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def ApplyUpperBloodOxygen(self):
        
        #apply height to object and save object
        bloodoxygen = self.New_Upper_Blood_Oxygen.text()
        
        if not(is_float(bloodoxygen)):
            self.BloodOxygenError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.BloodOxygenError.setText("Blood Oxygen must be numeric.")
            return
        
        CheckBloodOxygen = checkBloodOxygen(float(bloodoxygen))

        if  CheckBloodOxygen == False:
            self.BloodOxygenError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.BloodOxygenError.setText("Please put reasonable inputs")
            return

        self.BloodOxygenError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.BloodOxygenError.setText("Values have been changed")
                
       # self.BloodOxygenError.setText("")

        #saved to the file
        logged_in_user.heart_health.set_boUL(float(bloodoxygen))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def ApplyLowerBloodOxygen(self):
        
        #apply height to object and save object
        bloodoxygen = self.New_Lower_Blood_Oxygen.text()
        
        if not(is_float(bloodoxygen)):            
            self.BloodOxygenError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.BloodOxygenError.setText("Blood Oxygen must be numeric.")
            return
        
        CheckBloodOxygen = checkBloodOxygen(float(bloodoxygen))

        if  CheckBloodOxygen == False:
            self.BloodOxygenError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.BloodOxygenError.setText("Please put reasonable inputs")
            return

        self.BloodOxygenError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;")
        self.BloodOxygenError.setText("Values have been changed")
                
       # self.BloodOxygenError.setText("")

        #saved to the file
        logged_in_user.heart_health.set_boLL(float(bloodoxygen))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def ApplyUpperBloodPressure(self):
        
        #apply height to object and save object
        bloodpressure = self.New_Upper_Blood_Pressure.text()
        
        if not(is_float(bloodpressure)):
            self.BloodPressureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.BloodPressureError.setText("Blood Pressure must be numeric.")
            return
        
        CheckBloodPressure = checkBloodPressure(float(bloodpressure))

        if  CheckBloodPressure == False:
            self.BloodPressureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.BloodPressureError.setText("Please put reasonable inputs")
            return  

        self.BloodPressureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.BloodPressureError.setText("Values have been changed")
            
       # self.BloodPressureError.setText("")

        #saved to the file
        logged_in_user.heart_health.set_bpUL(float(bloodpressure))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def ApplyLowerBloodPressure(self):
        
        #apply height to object and save object
        bloodpressure = self.New_Lower_Blood_Pressure.text()
        
        if not(is_float(bloodpressure)):
            self.BloodPressureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.BloodPressureError.setText("Blood Pressure must be numeric.")
            return
        
        CheckBloodPressure = checkBloodPressure(float(bloodpressure))

        if  CheckBloodPressure == False:
            self.BloodPressureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.BloodPressureError.setText("Please put reasonable inputs")
            return
        
        self.BloodPressureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.BloodPressureError.setText("Values have been changed")
                
     #   self.BloodPressureError.setText("")

        #saved to the file
        logged_in_user.heart_health.set_bpLL(float(bloodpressure))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def Back(self):         
        setting = Setting()
        GoBack(self, setting)

class SettingBodyInfo(QtWidgets.QMainWindow):
    def __init__(self):
        super(SettingBodyInfo, self).__init__()
        loadUi("UI/Setting_Body.ui", self)
        self.GoBack.clicked.connect(self.Back)

        self.GoBack.clicked.connect(self.Back)

        self.Apply_Upper_Temp.clicked.connect(self.ApplyUpperTemperature)
        self.Apply_Lower_Temp.clicked.connect(self.ApplyLowerTemperature)

        self.Apply_Upper_Fluid.clicked.connect(self.ApplyUpperFluid)
        self.Apply_Lower_Fluid.clicked.connect(self.ApplyLowerFluid)

    def ApplyUpperTemperature(self):
        
        #apply height to object and save object
        temperature = self.New_Upper_Temp.text()
        
        if not(is_float(temperature)):    
            self.TempError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.TempError.setText("Temperature must be numeric.")
            return
        
        CheckTemp = checkTemperature(float(temperature))

        if  CheckTemp == False:
            self.TempError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.TempError.setText("Please put reasonable inputs")
            return

        self.TempError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.TempError.setText("Values have been changed")
                
       # self.TempError.setText("")

        #saved to the file
        logged_in_user.body_Info.set_tempUpperLimit(float(temperature))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
    
    def ApplyLowerTemperature(self):
        
        #apply height to object and save object
        temperature = self.New_Lower_Temp.text()
        
        if not(is_float(temperature)):
            self.TempError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.TempError.setText("Temperature must be numeric.")
            return
        
        CheckTemp = checkTemperature(float(temperature))

        if  CheckTemp == False:
            self.TempError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.TempError.setText("Please put reasonable inputs")
            return
        
        self.TempError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.TempError.setText("Values have been changed")        
       # self.TempError.setText("")

        #saved to the file
        logged_in_user.body_Info.set_tempLowerLimit(float(temperature))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def ApplyUpperFluid(self):
        
        #apply height to object and save object
        fluid = self.New_Upper_Fluid.text()
        
        if not(is_float(fluid)):
            self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.FluidError.setText("Fluid must be numeric.")
            return
        
        CheckFluid = checkFluid(float(fluid))

        if  CheckFluid == False:
            self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.FluidError.setText("Please put reasonable inputs")
            return
    
        self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.FluidError.setText("Values have been changed") 
                
       # self.FluidError.setText("")

        #saved to the file
        logged_in_user.body_Info.set_fluidUpperLimit(float(fluid))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)

    def ApplyLowerFluid(self):
        
        #apply height to object and save object
        fluid = self.New_Lower_Fluid.text()
        
        if not(is_float(fluid)):
            self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.FluidError.setText("Fluid must be numeric.")
            return
        
        CheckFluid = checkFluid(float(fluid))

        if  CheckFluid == False:
            self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.FluidError.setText("Please put reasonable inputs")
            return
    
        self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.FluidError.setText("Values have been changed") 
            
        #self.FluidError.setText("")

        #saved to the file
        logged_in_user.body_Info.set_fluidUpperLimit(float(fluid))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
    
    def Back(self):         
        setting = Setting()
        GoBack(self, setting)
        
class SettingBMI(QtWidgets.QMainWindow):
    def __init__(self):
        super(SettingBMI, self).__init__()
        loadUi("UI/Setting_BMI.ui", self)
        self.GoBack.clicked.connect(self.Back)

        self.GoBack.clicked.connect(self.Back)

    def Back(self):         
        setting = Setting()
        GoBack(self, setting)
        
        
 
#prescription manager   

class PrescriptionManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(PrescriptionManager, self).__init__()
        uic.loadUi("UI/PHS_prescription.ui", self)

        # Connect signals to slots
        self.GoBack.clicked.connect(self.Back)
        self.GoBackMed.clicked.connect(self.GoBackM)
        self.GoForwardMed.clicked.connect(self.GoForwardM)
        self.GoBack.clicked.connect(self.Back)
        self.UpdateValues.clicked.connect(self.UpdatePrescription)
        self.Delete.clicked.connect(self.deletecurrent)

        # Set initial values
        self.Name.setText("Name: ")
        self.Effect.setText("Effects: ")
        self.Dosage.setText("Dosage: ")

        self.current_index = 0  # counting current place in array

        if logged_in_user.prescription_manager.is_array_empty():
            self.Status.setText("Currently, no medications are stored")
        else:
            medication_count = len(logged_in_user.prescription_manager.Prescription_Array)
            self.Status.setText("Currently have " + str(medication_count) + " medications")
            self.display_current_prescription()

    def display_current_prescription(self):
        try:
            current_prescription = logged_in_user.prescription_manager.Prescription_Array[self.current_index]
            current_prescription_name = current_prescription.get_name()
            current_prescription_effects = current_prescription.get_effects()
            current_prescription_dosage = current_prescription.get_dosage()
            self.Name.setText("Name: " + current_prescription_name)
            self.Effect.setText("Effects: " + current_prescription_effects)
            self.Dosage.setText("Dosage: " + current_prescription_dosage)
        except IndexError:
            self.reset_prescription_display()

    def GoBackM(self):
        try:
            self.current_index = logged_in_user.prescription_manager.navigate_previous(self.current_index)
            self.display_current_prescription()
        except IndexError:
            self.reset_prescription_display()

    def GoForwardM(self):
        try:
            self.current_index = logged_in_user.prescription_manager.navigate_next(self.current_index)
            self.display_current_prescription()
        except IndexError:
            self.reset_prescription_display()
            
    def deletecurrent(self):
        try:
            # Delete current prescription at the current index
            del logged_in_user.prescription_manager.Prescription_Array[self.current_index]

            # Reorganize array to avoid leaving any gaps
            # (optional, you can skip this step if you don't mind having gaps in the array)
            logged_in_user.prescription_manager.Prescription_Array = [
                prescription for prescription in logged_in_user.prescription_manager.Prescription_Array if prescription is not None
            ]

            # Update current index if it exceeds the array bounds
            if self.current_index >= len(logged_in_user.prescription_manager.Prescription_Array):
                self.current_index = len(logged_in_user.prescription_manager.Prescription_Array) - 1

            # Display the updated prescription
            self.display_current_prescription()

            # Update the medication count after deleting the prescription
            medication_count = len(logged_in_user.prescription_manager.Prescription_Array)
            self.Status.setText("Currently have " + str(medication_count) + " medications")
            
            
            save = logged_in_user.get_Save_Path()
            logged_in_user.save_to_file(save)

            self.Status.setText("Medication removed")


        except IndexError:
            self.reset_prescription_display()

    def reset_prescription_display(self):
        self.Name.setText("Name: ")
        self.Effect.setText("Effects: ")
        self.Dosage.setText("Dosage: ")

    def Back(self):
        home = Home()  # Assuming Home class is defined
        GoToAndRemove(self, home)

    def UpdatePrescription(self):
        med = UpdatePrescription()  # Assuming UpdatePrescription class is defined
        GoToAndRemove(self, med)
        
        
        
        


class UpdatePrescription(QtWidgets.QMainWindow):
    def __init__(self):
        super(UpdatePrescription, self).__init__()
        loadUi("UI/input_Prescriptions.ui", self)
        
        self.GoBack.clicked.connect(self.Back)
        self.UpdateValues_2.clicked.connect(self.InsertPrescription)

    def Back(self):         
        body = PrescriptionManager()
        GoBack(self, body)

    def InsertPrescription(self):
        new_name = self.New_Name.text()
        new_effects = self.New_Effects.text()
        new_dosage = self.New_Dosage.text()

        if not new_name or not new_effects or not new_dosage:
            # Check if any field is empty
            self.Status.setText("Please fill in all fields")
            return

        # Assuming you have a reference to the logged_in_user
        logged_in_user.prescription_manager.add_prescription(new_name, new_effects, new_dosage)
        
        save = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(save)

        # Display success message or navigate back to PrescriptionManager
        QtWidgets.QMessageBox.information(self, "Success", "Prescription added successfully.")
        prescription = PrescriptionManager()
        GoToAndRemove(self, prescription)       
        
        
        
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
            self.HeightError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.HeightError.setText("Height must be numeric.")
            return
        
        CheckHeight = checkHeight(float(height))

        if  CheckHeight == False:
            self.HeightError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")

            self.HeightError.setText("Please put reasonable inputs")
            return

        self.HeightError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.HeightError.setText("Values have been changed")
                
       # self.HeightError.setText("")

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
            self.WeightError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.WeightError.setText("Weight must be numeric.")
            return
        
        Checkweight = checkWeight(float(weight))

        if  Checkweight == False:
            self.HeightError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.WeightError.setText("Please put reasonable inputs")
            return
        
        self.WeightError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.WeightError.setText("Values have been changed")
        
        #self.WeightError.setText("")
        
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
        
        #height and weight
        temprature = logged_in_user.body_Info.get_temp()
        self.DISPLAY_TEMPRATURE.setText(str(temprature) + " c")
        
        
        
        fluid = logged_in_user.body_Info.get_fluid()
        self.DISPLAY_FLUID.setText(str(fluid) + " mL")
        
        DisplayTemp(self, temprature)

        DisplayJugs(self, fluid)


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
        self.bodytemp.setPixmap(qpixmap)
        
        qpixmap = QPixmap('UI/nojug.png')
        self.emptyjug.setPixmap(qpixmap)
       
        
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
            self.TemperatureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.TemperatureError.setText("Temprature must be numeric.")
            return
        
        
        CheckTemprature = checkTemperature(float(Temprature))

        if  CheckTemprature == False:
            self.TemperatureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.TemperatureError.setText("Please put reasonable inputs")
            return
        
        self.TemperatureError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.TemperatureError.setText("Values have been changed")
        
        #self.TempratureError.setText("")


        DisplayTemp(self, Temprature)

        #saved to the file
        logged_in_user.body_Info.set_temp(float(Temprature))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
        
        
    #function to change the weight 
    def ApplyFluid(self):
        
        #apply height to object and save object
        Fluid = self.New_Fluid.text()
        
        if not(is_float(Fluid)):
            self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.FluidError.setText("Fluid must be numeric.")
            return
        
        CheckFluid = checkFluid(float(Fluid))

        if  CheckFluid == False:
            self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: red;")
            self.FluidError.setText("Please put reasonable inputs")
            return
        
        self.FluidError.setStyleSheet("font: 12pt MS Shell Dlg 2; border: none; color: green;" )
        self.FluidError.setText("Values have been changed")
        
        #save to the file 
        logged_in_user.body_Info.set_fluid(float(Fluid))
        savepath = logged_in_user.get_Save_Path()
        logged_in_user.save_to_file(savepath)
        
        DisplayJugs(self, Fluid)
     

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