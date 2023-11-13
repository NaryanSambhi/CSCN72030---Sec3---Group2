#Software Development Lifecycle Project 3
#Naryan Sambhi 

#this is the userdata class where all the data will be passed from the user 
#this class will also consist of the diagnose function to diagnose the patient

import pickle

from Prescription import *

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
        self.Name = name
        self.Age = age
        self.prescription_manager = PrescriptionManager()
        #other modules here too

    def __str__(self):
        return f'\nName: {self.Name} \nAge: {self.Age}'        
        


#functions 
    def save_to_file(self, filename):
        data_to_save = {
            'Name': self.Name,
            'Age': self.Age,
            'prescriptions': self.prescription_manager.Prescription_Array  
            
            #other modules here
            
            
        }
        
        
        FileIO.save_to_file(data_to_save, filename) #uses dump to file function with pickle

    def load_from_file(self, filename):
        loaded_data = FileIO.load_from_file(filename)
        self.name = loaded_data['Name']
        self.age = loaded_data['Age']
        self.prescription_manager.Prescription_Array = loaded_data.get('prescriptions', [])  
        #other functions here too



#for tests

#create
user = UserData(name="John Doe", age=30)
user.prescription_manager.add_prescription("Aspirin", "Pain relief", "10mg")
user.save_to_file("user_data.pkl")


#load
loaded_user = UserData(name="", age=0)
loaded_user.load_from_file("user_data.pkl")



#print to confirm
print("\n--------- profile --------")
print(user)

print("\n--------- prescriptions --------")
loaded_user.prescription_manager.print_prescriptions()

print("\n--------- heart --------")

print("\n--------- body --------")

print("\n--------- BMI --------\n")



