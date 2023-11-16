#Software Development Lifecycle Project 3
#Katarina Lukic, Naryan Sambhi, Nick Packull-Mccormick, Umang Mohini

#This is the Body Info module
#This class will have 2 smaller classes called FLuid Intake and Body Temperature 


class body_info(object):

     #main variables
    temp = 0
    fluid = 0
    _temp = 0
    _fluid = 0

    #flag variables
    _temp_flag = False
    _fluid_flag = False

    
    #shouldnt be defined here, how will the user change this.
    _tempUpperLim = 100
    _tempLowerLim = 97
    _fluidUpperLim = 5000
    _fluidLowerLim = 0

    #Parameterized Constructor
    def __init__(self, temp, fluid, tempLowerLim = 97, tempUpperLim = 100, fluidLowerLim = 0, fluidUpperLim = 5000):
        self.set_fluid(fluid)
        self.set_temp(temp)
        
        self.set_tempLowerLimit(tempLowerLim)
        self.set_tempUpperLimit(tempUpperLim)
        self.set_fluidLowerLimit(fluidLowerLim)
        self.set_fluidUpperLimit(fluidUpperLim)
        
        self.checkFluidFlag()
        self.checkTempFlag()
    
    def __str__(self):
        return f'Temp: {self._temp} \nFluid Intake: {self._fluid}\n'
    
    #Getters and Setters for the weight and height 
    def get_temp(self):
        return self._temp
    def set_temp(self, temp):
        self._temp = temp
        #return temp

    def get_fluid(self):
        return self._fluid
    def set_fluid(self, fluid):
        self._fluid = fluid
        #return fluid 
        
    #Getters and Setter for Internal Variables
    def get_tempUpperLimit(self):
        return self._tempUpperLim
    def set_tempUpperLimit(self, tempUpperLim):
        self._tempUpperLim = tempUpperLim
        #return tempUpperLim

    def get_tempLowerLimit(self):
        return self._tempLowerLim
    def set_tempLowerLimit(self, tempLowerLim):
        self._tempLowerLim = tempLowerLim
        #return tempLowerLim

    def get_fluidUpperLimit(self):
        return self._fluidUpperLim
    def set_fluidUpperLimit(self, fluidUpperLim):
        self._fluidUpperLim = fluidUpperLim
        #return fluidUpperLim

    def get_fluidLowerLimit(self):
        return self._fluidLowerLim
    def set_fluidLowerLimit(self, fluidLowerLim):
        self._fluidLowerLim = fluidLowerLim
        #return fluidLowerLim

    #setFlags 
    def checkTempFlag(self):
        if self._temp > self._tempUpperLim or self._temp < self._tempLowerLim:
            self._temp_flag = True
            return self._temp_flag
        else:
            self._temp_flag = False
            return self._temp_flag

    def checkFluidFlag(self):
        if self._fluid > self._fluidUpperLim or self._fluid < self._fluidLowerLim:
            self._fluid_flag = True
            return self._fluid_flag
            #return True
        else:
            self._fluid_flag = False
            return self._fluid_flag
            #return False
  