#Software Development Lifecycle Project 3
#Katarina Lukic, Naryan Sambhi, Nick Packull-Mccormick, Umang Mohini

#This is the hearthealth module where 3 smaller classes will be created called Heart rate, blood oxygen, blood pressure


class heart_Health(object):
    #main variables
    _heart_rate = 0
    _blood_oxegen = 0
    _blood_pressure = 0

    #flag variables
    _hr_flag = False
    _bo_flag = False
    _bp_flag = False

    #internal variables
    _hrUpperLim = 100
    _hrLowerLim = 60
    _boUpperLim = 99
    _boLowerLim = 95
    _bpUpperLim = 120
    _bpLowerLim = 90

    #Constructor
    def __init__(self, heart_rate, blood_oxegen, blood_pressure):
        self._heart_rate = heart_rate
        self._blood_oxegen = blood_oxegen
        self._blood_pressure = blood_pressure
        self.checkHRFlag(self)
        self.checkBOFlag(self)
        self.checkBPFlag(self)
    

    #Getters and Setters
    def get_hr(self):
        return self._heart_rate
    def set_hr(self, heart_rate):
        self._heart_rate = heart_rate

    def get_bo(self):
        return self._blood_oxegen
    def set_bo(self, blood_oxegen):
        self._blood_oxegen = blood_oxegen

    def get_hr(self):
        return self._blood_pressure
    def set_hr(self, blood_pressure):
        self._blood_pressure = blood_pressure

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

    def Display():
      print("This is the heart health info")



