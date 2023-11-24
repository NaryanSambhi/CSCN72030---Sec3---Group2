#Software Development Lifecycle Project 3
#Katarina Lukic

#this is the BMI Module
#This module will have 2 smaller clases with Weight and Height Respectively

class BMI(object):
    
    #set private variables to be equal to 0 as a placeholder
    _weight = 0
    _height = 0
    _bmi = 0
    _feet = 0
    _cm = 0
    _kg = 0
    _pound = 0
    
    #internal variables 

    #Parameterized Constructor
    def __init__(self, height, weight):
       
       self.set_height(height)
       self.set_weight(weight)
              
    #calculate BMI function was added to calculate the BMI from height and weight   
    def calculate_bmi(self, height, weight):
        height = height / 100
        bmi = weight / (height ** 2)
        BMI._bmi = bmi
        return bmi
    
    def get_bmi(self):
        return round(self._bmi, 2)

    #anohter function was added for the BMI status if the user is underweight or normal weight    
    def get_bmi_status(self):
        bmi = self._bmi
        
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obesity"
        
    # the string to the terminal now includes the bmi
    def __str__(self):
        return f'\nHeight: {self._height} \nWeight: {self._weight}\nBMI: {self._bmi}\n'
    
    #Getters and Setters for the weight and height 
    def get_weight(self):
        return round(self._weight, 2)
    
    def set_weight(self, weight):
        self._weight = weight

    def get_height(self):
        return round(self._height, 2)
    
    def set_height(self, height):
        self._height = height 

#conversions as flags

#feet to cm = times by 30.48
#cm to feet = divide by 30.48

#kg to pound = times by 2.20
#pound to kilogram = divided by 2.20


#def GetHeightInCm(self, cm):
   # self.cm = cm
   # return cm

#def SetHeightInFeet(self, height, feet):
    #self._feet = feet
   # feet = height / 30.48
   # return feet

#def GetWeightInKilogram(self, kg):
   # self.kg = kg
   # return kg

#def SetWeightInKilogram(self, weight, kg):
   # self._kg = kg
   # kg = weight / 30.48
   # return kg