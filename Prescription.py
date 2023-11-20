# Software Development Lifecycle Project 3
# Naryan Sambhi 

#prescription and manager classes for user to view and manage medications 

#prescription class 
#blueprint for creating prescriptions 
class Prescription: 
    
    #constructor 
    def __init__(self, name, effects, dosage):
        self._Name = name
        self._Effects = effects
        self._Dosage = dosage
        
    #string output
    def __str__(self):
        return f'\nMedication Name: {self._Name} \nEffects: {self._Effects} \nDosage: {self._Dosage}\n'
    
    # getters and setters
    def get_name(self):
        return self._Name

    def set_name(self, name):
        self._Name = name

    def get_effects(self):
        return self._Effects

    def set_effects(self, effects):
        self._Effects = effects

    def get_dosage(self):
        return self._Dosage

    def set_dosage(self, dosage):
        self._Dosage = dosage


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
            if prescription._Name == name: 
                self.Prescription_Array.remove(prescription)
                print(f'{prescription._Name} has been removed from user file')
                return
            
    def print_prescriptions(self):
        for prescription in self.Prescription_Array:
            print(prescription)
            
            
    def edit_prescription_dose(self, name, new_dose):
          for prescription in self.Prescription_Array:  #search for prescription and change
            if prescription._Name == name: 
                prescription._Dosage = new_dose
                print(f'{prescription._Name} dosage has been changed to {prescription._Dosage}')
                return



'''
# Create a PrescriptionManager instance
manager = PrescriptionManager()

# Add prescriptions
manager.add_prescription("Aspirin", "Pain relief", "10mg")
manager.add_prescription("Ibuprofen", "Anti-inflammatory", "20mg")
manager.add_prescription("Paracetamol", "Fever reducer", "15mg")

# Print prescriptions
print("Initial Prescriptions:")
manager.print_prescriptions()

# Remove a prescription
manager.remove_prescription("Ibuprofen")

# Print prescriptions after removal
print("\nPrescriptions after Removal:")
manager.print_prescriptions()

# Edit a prescription dose
manager.edit_prescription_dose("Aspirin", "15mg")

# Print prescriptions after editing dose
print("\nPrescriptions after Editing Dose:")
manager.print_prescriptions()


'''