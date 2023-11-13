# Software Development Lifecycle Project 3
# Naryan Sambhi 

#prescription and manager classes for user to view and manage medications 

#prescription class 
#blueprint for creating prescriptions 
class Prescription: 
    
    #constructor 
    def __init__(self, name, effects, dosage):
        self.Name = name
        self.Effects = effects
        self.Dosage = dosage
        
    #string output
    def __str__(self):
        return f'\nMedication Name: {self.Name} \nEffects: {self.Effects} \nDosage: {self.Dosage}\n'
    
    #functions
    

#prescription manager class
#manages a collection of prescriptions
class PrescriptionManager:
    
    #constructor 
    def __init__(self):
        self.Prescription_Array = [] #array of prescription objects 

    #functions
    def add_prescription(self, Name, Effects, Dosage): #attributes of presc object
        prescription = Prescription(Name, Effects, Dosage)
        self.Prescription_Array.append(prescription)
        #creating prescription object and appending it to array / manager
    
    #remove
    def remove_prescription(self, name):
        for prescription in self.Prescription_Array: #search for prescription and remove
            if prescription.Name == name: 
                self.Prescription_Array.remove(prescription)
                print(f'{prescription.Name} has been removed from user file')
                return
            
    def print_prescriptions(self):
        for prescription in self.Prescription_Array:
            print(prescription)
            
            
    def edit_prescription_dose(self, name, new_dose):
          for prescription in self.Prescription_Array:  #search for prescription and change
            if prescription.Name == name: 
                prescription.Dosage = new_dose
                print(f'{prescription.Name} dosage has been changed to {prescription.Dosage}')
                return


