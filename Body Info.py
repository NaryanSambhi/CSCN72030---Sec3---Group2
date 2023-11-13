#Software Development Lifecycle Project 3
#Katarina Lukic, Naryan Sambhi, Nick Packull-Mccormick, Umang Mohini

#This is the Body Info module
#This class will have 2 smaller classes called FLuid Intake and Body Temperature 

class body_Info(object):
    def see_body_info():
      print("This is the body info")
      
      fluid = fluid_Intake()
      intake1 = fluid.get_fluid_intake
      
      temp = body_Temp()
      intake2 = temp.get_body_temp

class fluid_Intake(object):
  def __init__(self, fluid):
    self.fluid = fluid
    
  #Functions
  def set_fluid_intake(fluid, input):
    fluid = input("How much water have you had today?")
    
  def get_fluid_intake(self):
    return self.fluid

class body_Temp(object):
  def __init__(self, temp):
    self.temp = temp
    
  #Functions
  def get_body_temp(self, input):
    temp = input("What is temperature currently?")
    
  def set_body_temp(self):
    return self.temp

# find a way to link it to userdata

