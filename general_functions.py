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
   