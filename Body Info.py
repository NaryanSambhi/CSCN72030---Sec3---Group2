#Software Development Lifecycle Project 3
#Katarina Lukic, Naryan Sambhi, Nick Packull-Mccormick, Umang Mohini

#This is the Body Info module
#This class will have 2 smaller classes called FLuid Intake and Body Temperature 

class body_Info(object):
     #main variables
    _body_temp = 0
    _fluid_intake = 0

    #flag variables
    _body_temp_flag = False
    _fluid_intake_flag = False

    #internal variables -> change the values 
    _body_temp_UpperLim = 100.4
    _body_temp_LowerLim = 97.0
    _fluid_intake_UpperLim = 5.0
    _fluid_intake_LowerLim = 0.0

    #constructor
    def __init__(self, _fluid_intake, _body_temp):
     self._fluid_intake = _fluid_intake
     self._body_temp = _body_temp
     self.body_temp_Flag(self)
     self.fluid_intake_Flag(self)
        
    #Functions
    def set_fluid_intake(_fluid_intake, input):
      _fluid_intake = input("How much water have you had today?") 
    
    def get_fluid_intake(self):
      return self._fluid_intake
  
    def get_body_temp(self, input):
      return self.temp
    
    def set_body_temp(self):
      temp = input("What is temperature currently?")
  
    def see_body_info():
      print("This is the body info")
      
    #setFlags
    def body_temp_Flag(self):
      if self.get_body_temp >= self.body_temp_UpperLim or self.get_body_temp <= self._body_temp_LowerLim:
          self._body_temp_flag = True
      else:
          self._body_temp_flag = False
    
    def fluid_intake_Flag(self):
      if self.get_fluid_intake >= self._fluid_intake_UpperLim or self.get_fluid_intake <= self._body_temp_LowerLim:
          self. _fluid_intake_flag = True
      else:
          self. _fluid_intake_flag = False
