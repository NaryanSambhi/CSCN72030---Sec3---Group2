#Software Development Lifecycle Project 3
#Katarina Lukic

#this is the BMI Module
#This module will have 2 smaller clases with Weight and Height Respectively

class BMI(object):
    
    
    #main variables
    
    #you and nick need to fix this in yours in where this is being defined

    _weightUpperLim = 150
    _weightLowerLim = 50
    _heightUpperLim = 225
    _heightLowerLim = 80
    
    #flag variables
    _weight_flag = False
    _height_flag = False

    #internal variables 

    #Parameterized Constructor
    def __init__(self, height, weight, weightLowerLim = 50, weightUpperLim = 150, heightLowerLim = 80, heightUpperLim = 225):
       self.set_height(height)
       self.set_weight(weight)
        
       self.set_weightLowerLimit(weightLowerLim)
       self.set_weightUpperLimit(weightUpperLim)
       self.set_heightLowerLimit(heightLowerLim)
       self.set_heightUpperLimit(heightUpperLim)
        
       self.checkHeightFlag()
       self.checkWeightFlag()
    
    def __str__(self):
        return f'\nHeight: {self._height} \nWeight: {self._weight}\n'
    
    #Getters and Setters for the weight and height 
    def get_weight(self):
        return self._weight
    
    def set_weight(self, weight):
        self._weight = weight

    def get_height(self):
        return self._height
    
    def set_height(self, height):
        self._height = height 

      #Getters and Setter for Internal Variables
    def get_weightUpperLimit(self):
        return self._weightUpperLim
    def set_weightUpperLimit(self, weightUpperLim):
        self._weightUpperLim = weightUpperLim
       
    def get_weightLowerLimit(self):
        return self._weightLowerLim
    def set_weightLowerLimit(self, weightLowerLim):
        self._weightLowerLim = weightLowerLim

    def get_heightUpperLimit(self):
        return self._heightUpperLim
    def set_heightUpperLimit(self, heightUpperLim):
        self._heightUpperLim = heightUpperLim

    def get_heightLowerLimit(self):
        return self._heightLowerLim
    def set_heightLowerLimit(self, heightLowerLim):
        self._heightLowerLim = heightLowerLim

    #setFlags 
    def checkWeightFlag(self):
        if self._weight > self._weightUpperLim or self._weight < self._weightLowerLim:
            self._weight_flag = True
            return self._weight_flag
        else:
            self._weight_flag = False
            return self._weight_flag

    def checkHeightFlag(self):
        if self._height > self._heightUpperLim or self._height < self._heightLowerLim:
            self._height_flag = True
            return self._height_flag
        else:
            self._height_flag = False
            return self._height_flag
    
 #incorporate the calculate bmi function with the flags? 
           
