#general shared functions code that can be reused anywhere



#input validation functions

#makes sure input values are numbers only 



def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

#same for floats
def is_float(value):
   try:
       float(value)
       return True
   except ValueError:
       return False    

def checkName(name):
    if(len(name) >= 14):
        return False
    else:
        return True   

def checkAge(age):
    if (age > 99):
        return False
    if (age < 18):
        return False
    else:
        return True
        
def checkWeight(weight):
    if (weight > 700):
        return False
    if (weight < 22):
        return False
    else:
        return True

def checkHeight(height):
    if (height > 274):
        return False
    if (height < 50):
        return False
    else:
        return True
    
def checkTemperature(temp):
    if (temp > 150):
        return False
    if (temp < 0):
        return False
    else:
        return True
    
def checkFluid(fluid):
    if (fluid > 10000):
        return False
    if (fluid < 0):
        return False
    else:
        return True
    
def checkHeartRate(heartrate):
    if (heartrate > 200):
        return False
    if (heartrate < 50):
        return False
    else:
        return True

def checkBloodOxygen(bloodoxygen):
    if (bloodoxygen > 200):
        return False
    if (bloodoxygen < 50):
        return False
    else:
        return True

def checkBloodPressure(bloodpressure):
    if (bloodpressure > 200):
        return False
    if (bloodpressure < 50):
        return False
    else:
        return True

