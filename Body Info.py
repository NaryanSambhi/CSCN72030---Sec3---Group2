#Software Development Lifecycle Project 3
#Katarina Lukic, Naryan Sambhi, Nick Packull-Mccormick, Umang Mohini

#This is the Body Info module
#This class will have 2 smaller classes called FLuid Intake and Body Temperature 

class body_Info(object):
    def Display():
      print("This is the body info")

class fluid_Intake(object):
  def __init__(self, fluid):
    self.fluid = fluid

class body_Temp(object):
  def __init__(self, temp):
    self.temp = temp



