#Software Development Lifecycle Project 3
#Katarina Lukic, Naryan Sambhi, Nick Packull-Mccormick, Umang Mohini

#This is the Body Info module
#This class will have 2 smaller classes called FLuid Intake and Body Temperature 


class body_info(object):
    #main variables
    _temp = 0
    _fluid = 0

    #flag variables
    _temp_flag = False
    _fluid_flag = False

    #internal variables
    _tempUpperLim = 100
    _tempLowerLim = 90
    _fluidUpperLim = 1000
    _fluidLowerLim = 500

    #Parameterized Constructor
    def __init__(self, temp, fluid):
        self._temp = temp
        self._fluid = fluid
        self.checkTempFlag(self)
        self.checkFluidFlag(self)
    
    #Getters and Setters for the weight and height 
    def get_temp(self):
        return self._temp
    def set_temp(self, temp):
        self._temp = temp

    def get_fluid(self):
        return self._fluid
    def set_fluid(self, fluid):
        self._fluid = fluid 


    #setFlags that can be changed later from the user
    #these ranges will let the user know if they are in the optimal body weight 
    def checkTempFlag(self):
        if self._temp > self._tempUpperLim or self._temp < self._tempLowerLim:
            self._tempflag = True
        else:
            self._tempflag = False

    def checkFluidFlag(self):
        if self._fluid > self._fluidUpperLim or self._fluid < self._fluidLowerLim:
            self._fluidflag = True
        else:
            self._fluidflag = False
  