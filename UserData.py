#Software Development Lifecycle Project 3
#Naryan Sambhi 

#this is the userdata class where all the data will be passed from the user 
#this class will also consist of the diagnose function to diagnose the patient

import pickle

from Prescription import *
from Heart_Health import *
from BMI import *
from Body_Info import *

import re

#ensures save files follow specific format
def sanitize_filename(filename):

    invalid_chars_pattern = re.compile(r'[\\/:*?"<>|@.]')

    # Replace disallowed characters with an underscore
    sanitized_filename = re.sub(invalid_chars_pattern, '_', filename)

    return sanitized_filename

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
        
        self._Save_Path = ""
        
        #modules
        self.prescription_manager = PrescriptionManager()
        self.heart_health = heart_Health(0,0,0,100,60,99,95,120,90)  
                
        self.BMI = BMI(0,0)  
        self.body_Info = body_info(0.0,0.0)    
        

    def __str__(self):
        return f'\nName: {self._Name} \nAge: {self._Age}' 
    
    
    # Getters and setters
    def get_name(self):
        return self._Name

    def set_name(self, name):
        self._Name = name

    def get_age(self):
        return self._Age

    def set_age(self, age):
        self._Age = age
        
    def set_Save_Path(self, Save_Path):
        self._Save_Path = Save_Path
        
    def get_Save_Path(self):
        return self._Save_Path


#functions 
    def save_to_file(self, filename):
        data_to_save = {
            'Name': self._Name,
            'Age': self._Age,
            'Savepath' : self._Save_Path,
            
            #modules
            
            'prescriptions': self.prescription_manager.Prescription_Array,
            
            'Heart_Health': { 
                    'heart_rate': self.heart_health._heart_rate, 
                    'blood_oxygen' : self.heart_health._blood_oxygen,
                    'blood_pressure' : self.heart_health._blood_pressure,
                    'hr_flag' : self.heart_health._hr_flag,
                    'bo_flag' :self.heart_health._bo_flag,
                    'bp_flag' : self.heart_health._bp_flag
                },

            'BMI': { 
                    'height': self.BMI._height,
                    'weight' : self.BMI._weight
                },
            'body info': { 
                    'temp': self.body_Info._temp,
                    'fluid' : self.body_Info._fluid,
                    'temp_flag' : self.body_Info._temp_flag,
                    'fluid_flag' : self.body_Info._fluid_flag
                },
            
                        
        }
        
        
        FileIO.save_to_file(data_to_save, filename) #uses dump to file function with pickle

    def load_from_file(self, filename):
        #user
        loaded_data = FileIO.load_from_file(filename)
        self._Name = loaded_data['Name']
        self._Age = loaded_data['Age']
        self._Save_Path = loaded_data['Savepath']
        
        #modules
        self.prescription_manager.Prescription_Array = loaded_data.get('prescriptions', [])  
        self.prescription_manager.Prescription_Array = loaded_data.get('prescriptions', [])
        self.heart_health._heart_rate = loaded_data['Heart_Health']['heart_rate']
        self.heart_health._blood_oxygen = loaded_data['Heart_Health']['blood_oxygen']
        self.heart_health._blood_pressure = loaded_data['Heart_Health']['blood_pressure']
        self.heart_health._hr_flag = loaded_data['Heart_Health']['hr_flag']
        self.heart_health._bo_flag = loaded_data['Heart_Health']['bo_flag']
        self.heart_health._bp_flag = loaded_data['Heart_Health']['bp_flag']
        self.BMI._height = loaded_data['BMI']['height']
        self.BMI._weight = loaded_data['BMI']['weight']
        self.body_Info._temp = loaded_data['body info']['temp']
        self.body_Info._fluid = loaded_data['body info']['fluid']
        self.body_Info._temp_flag = loaded_data['body info']['temp_flag']
        self.body_Info._fluid_flag = loaded_data['body info']['fluid_flag']

