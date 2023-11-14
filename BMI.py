#Software Development Lifecycle Project 3
#Katarina Lukic

#this is the BMI Module
#This module will have 2 smaller clases with Weight and Height Respectively

class BMI(object):
    
    
    #main variables
    
    
    #why are you defining these here? 
    '''
    _height = 0
    _weight = 0
    '''
    
    
    #you and nick need to fix this in yours in where this is being defined

    _weightUpperLim = 100
    _weightLowerLim = 60
    _heightUpperLim = 225
    _heightLowerLim = 80
    
    #flag variables
    _weight_flag = False
    _height_flag = False

    #internal variables 

    #Parameterized Constructor
    def __init__(self, height, weight):
        self._height = height
        self._weight = weight
        
        
        #causing errors
        # self.checkWeightFlag(self)
       #   self.checkHeightFlag(self)
    
    
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
        
        
        #exception case? 
        
        #needs something like this
        try:
            bmi = _weight / (_height ** 2)
        except:
            return

        
        #you need to set these to flags for the GUI to use
        
        #need to move this code and fix it into calculate. shouldnt be two sepperate 
        # Interpret the BMI
        if bmi < 18.5:
            print("You are underweight.") #you need to use flags how would this work
                                            #in a gui outside testing?
        elif 18.5 <= bmi < 24.9:
            print("Your weight is normal.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")
        
        return bmi
           

#useless function, remove
    # a temp display function to the user 
    # def Display():
    #  print("This is the BMI info")
