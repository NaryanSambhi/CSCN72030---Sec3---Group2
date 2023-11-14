#Software Development Lifecycle Project 3
#Katarina Lukic

#this is the BMI Module
#This module will have 2 smaller clases with Weight and Height Respectively

class BMI(object):
    #main variables
    _height = 0
    _weight = 0

    #flag variables
    _weight_flag = False
    _height_flag = False

    #internal variables 
    _weightUpperLim = 100
    _weightLowerLim = 60
    _heightUpperLim = 225
    _heightLowerLim = 80

    #Parameterized Constructor
    def __init__(self, height, weight):
        self._height = height
        self._weight = weight
        self.checkWeightFlag(self)
        self.checkHeightFlag(self)
    
    #Getters and Setters for the weight and height 
    def get_weight(self):
        return self._weight
    def set_weight(self, weight):
        self._weight = weight

    def get_height(self):
        return self._height
    def set_height(self, height):
        self._height = height 

    #setFlags that can be changed later from the user
    #these ranges will let the user know if they are in the optimal body weight 
    def checkWeightFlag(self):
        if self._weight > self._weightUpperLim or self._weight < self._weightLowerLim:
            self._weightflag = True
        else:
            self._weightflag = False

    def checkHeightFlag(self):
        if self._height > self._heightUpperLim or self._height < self._heightLowerLim:
            self._heightflag = True
        else:
            self._heightflag = False
    
    # a function to calculate the bmi 
    def Calculate(_height, _weight):
        bmi = _weight / (_height ** 2)
        return bmi
   
    # call the function for the calculations
    bmi = Calculate(_height, _weight)

    # Interpret the BMI
    if bmi < 18.5:
      print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
      print("Your weight is normal.")
    elif 25 <= bmi < 29.9:
      print("You are overweight.")
    else:
      print("You are obese.")

    # a temp display function to the user 
    def Display():
      print("This is the BMI info")
