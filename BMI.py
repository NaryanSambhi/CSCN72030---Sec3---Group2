#Software Development Lifecycle Project 3
#Katarina Lukic

#this is the BMI Module
#This module will have 2 smaller clases with Weight and Height Respectively

class BMI(object):
    
    _weight = 0
    _height = 0
    _bmi = 0
    
    #internal variables 

    #Parameterized Constructor
    def __init__(self, height, weight):
       
       self.set_height(height)
       self.set_weight(weight)
              
       
    def calculate_bmi(self, height, weight):
        height = height / 100
        bmi = weight / (height ** 2)
        BMI._bmi = bmi
        return bmi
    
    def get_bmi(self):
        return round(self._bmi, 2)
        
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