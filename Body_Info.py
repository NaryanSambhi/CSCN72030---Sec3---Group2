#Software Development Lifecycle Project 3
#Katarina Lukic, Naryan Sambhi, Nick Packull-Mccormick, Umang Mohini

#This is the Body Info module
#This class will have 2 smaller classes called FLuid Intake and Body Temperature 


class body_info(object):

     #main variables
    temp = 0
    fluid = 0

    #flag variables
    _temp_flag = False
    _fluid_flag = False

    
    #shouldnt be defined here, how will the user change this.
    _tempUpperLim = 100
    _tempLowerLim = 97
    _fluidUpperLim = 5000
    _fluidLowerLim = 0

    #Parameterized Constructor
    def __init__(self, temp, fluid):
        self._temp = temp
        self._fluid = fluid
        self.checkFluidFlag()
        self.checkTempFlag()
    
    def __str__(self):
        return f'Temp: {self._temp} \nFluid Intake: {self._fluid}\n'
    
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
  