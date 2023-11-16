#Software Development Lifecycle Project 3
#Nick Packull-Mccormick
#Revision History:
#2023-11-01: Created
#2023-11-13: Added Functionality
#2023-11-14: Added extra paramemters to constructor

#This is the hearthealth module.
#It controls the measurements of Heart Rate, Blood Oxygen and Blood Pressure
class heart_Health(object):

    #flag variables
    _hr_flag = False
    _bo_flag = False
    _bp_flag = False

    #internal variables Defaults
    _hrUpperLim = 100
    _hrLowerLim = 60
    _boUpperLim = 99
    _boLowerLim = 95
    _bpUpperLim = 120
    _bpLowerLim = 90

    #Constructor w Custom Settings. Python does not include function overloading so defaults are hard coded
    def __init__(self, heart_rate, blood_oxegen, blood_pressure, hrUpperLim=100, hrLowerLim=60, boUpperLim=99, boLowerLim=95, bpUpperLim=120, bpLowerLim=90):
        self.set_hr(heart_rate)
        self.set_bo(blood_oxegen)
        self.set_bp(blood_pressure)

        self.set_hrUL(hrUpperLim)
        self.set_hrLL(hrLowerLim)
        self.set_boUL(boUpperLim)
        self.set_boLL(boLowerLim)
        self.set_bpUL(bpUpperLim)
        self.set_bpLL(bpLowerLim)

        self.checkHRFlag()
        self.checkBOFlag()
        self.checkBPFlag()

    #Getters and Setters
    def get_hr(self):
        return self._heart_rate
    def set_hr(self, heart_rate):
        self._heart_rate = heart_rate

    def get_bo(self):
        return self._blood_oxegen
    def set_bo(self, blood_oxegen):
        self._blood_oxegen = blood_oxegen

    def get_bp(self):
        return self._blood_pressure
    def set_bp(self, blood_pressure):
        self._blood_pressure = blood_pressure

    #Getters and Setter for Internal Variables
    def get_hrUL(self):
        return self._hrUpperLim
    def set_hrUL(self, hrUpperLim):
        self._hrUpperLim = hrUpperLim

    def get_hrLL(self):
        return self._hrLowerLim
    def set_hrLL(self, hrLowerLim):
        self._hrLowerLim = hrLowerLim

    def get_boUL(self):
        return self._boUpperLim
    def set_boUL(self, boUpperLim):
        self._boUpperLim = boUpperLim

    def get_boLL(self):
        return self._boLowerLim
    def set_boLL(self, boLowerLim):
        self._boLowerLim = boLowerLim

    def get_bpUL(self):
        return self._bpUpperLim
    def set_bpUL(self, bpUpperLim):
        self._bpUpperLim = bpUpperLim

    def get_bpLL(self):
        return self._hrLowerLim
    def set_bpLL(self, bpLowerLim):
        self._bpLowerLim = bpLowerLim

    #setFlags
    def checkHRFlag(self):
        if self._heart_rate > self._hrUpperLim or self._heart_rate < self._hrLowerLim:
            self._hr_flag = True
        else:
            self._hr_flag = False

    def checkBOFlag(self):
        if self._blood_oxegen > self._boUpperLim or self._blood_oxegen < self._boLowerLim:
            self._bo_flag = True
        else:
            self._bo_flag = False

    def checkBPFlag(self):
        if self._blood_pressure > self._bpUpperLim or self._blood_pressure < self._bpLowerLim:
            self._bp_flag = True
        else:
            self._bp_flag = False

    #Display
    def __str__(self):
        return f'\nHeart Rate: {self._heart_rate} \nBlood Oxygen: {self._blood_oxegen} \nBlood Pressure: {self._blood_pressure}\n'  

