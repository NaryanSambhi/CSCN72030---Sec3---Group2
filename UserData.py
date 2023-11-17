#Software Development Lifecycle Project 3
#Naryan Sambhi 

#this is the userdata class where all the data will be passed from the user 
#this class will also consist of the diagnose function to diagnose the patient

import pickle

from Prescription import *
from Heart_Health import *
from BMI import *
from Body_Info import *

# basic file IO functions
class FileIO:
    @staticmethod
    def save_to_file(data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)
        print(f"Data saved to {filename}.")

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
            print(f"Data loaded from {filename}.")
            return data
        except FileNotFoundError:
            print(f"File {filename} not found. No data loaded.")



class UserData:
    
    #constructors
    def __init__(self, name, age):
        #user
        self._Name = name
        self._Age = age
        
        #modules
        self.prescription_manager = PrescriptionManager()
        self.heart_health = heart_Health(0,0,0,100,60,99,95,120,90)  
                
        self.BMI = BMI(0,0)  
        self.body_Info = body_info(0.0,0.0)    
        

    def __str__(self):
        return f'\nName: {self._Name} \nAge: {self._Age}'        
        


#functions 
    def save_to_file(self, filename):
        data_to_save = {
            'Name': self._Name,
            'Age': self._Age,
            
            #modules
            
            'prescriptions': self.prescription_manager.Prescription_Array,
            
            'Heart_Health': { 
                    'heart_rate': self.heart_health._heart_rate,
                    'blood_oxygen' : self.heart_health._blood_oxygen,
                    'blood_pressure' : self.heart_health._blood_pressure 
                },

            'BMI': { 
                    'height': self.BMI._height,
                    'weight' : self.BMI._height
                },
            'body info': { 
                    'temp': self.body_Info._temp,
                    'fluid' : self.body_Info._fluid
                },
            
                        
        }
        
        
        FileIO.save_to_file(data_to_save, filename) #uses dump to file function with pickle

    def load_from_file(self, filename):
        #user
        loaded_data = FileIO.load_from_file(filename)
        self._Name = loaded_data['Name']
        self._Age = loaded_data['Age']
        
        #modules
        self.prescription_manager.Prescription_Array = loaded_data.get('prescriptions', [])  
        self.prescription_manager.Prescription_Array = loaded_data.get('prescriptions', [])
        self.heart_health._heart_rate = loaded_data['Heart_Health']['heart_rate']
        self.heart_health._blood_oxygen = loaded_data['Heart_Health']['blood_oxygen']
        self.heart_health._blood_pressure = loaded_data['Heart_Health']['blood_pressure']
        self.BMI._height = loaded_data['BMI']['height']
        self.BMI._weight = loaded_data['BMI']['weight']
        self.body_Info._temp = loaded_data['body info']['temp']
        self.body_Info._fluid = loaded_data['body info']['fluid']





#create

#for tests
user = UserData(name="John Doe", age=30)

user.prescription_manager.add_prescription("Aspirin", "Pain relief", "10mg")
user.prescription_manager.add_prescription("Ibuprofen", "Pain relief", "200mg")

user.heart_health._heart_rate = 90
user.heart_health._blood_oxygen = 80
user.heart_health._blood_pressure = 70

user.BMI._weight = 70
user.BMI._height = 190

user.body_Info._temp = 100
user.body_Info._fluid = 750

user.save_to_file("test.pkl")

#load
loaded_user = UserData(name="", age=0)
loaded_user.load_from_file("test.pkl")



#print to confirm
print("\n--------- profile --------")
print(loaded_user)

print("\n--------- prescriptions --------")
loaded_user.prescription_manager.print_prescriptions()

print("\n--------- heart --------")
print(loaded_user.heart_health)


print("\n--------- body --------")
print(loaded_user.body_Info)

print("\n--------- BMI --------")
print(loaded_user.BMI)



