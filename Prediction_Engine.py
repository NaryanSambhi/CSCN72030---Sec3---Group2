#Software Development Lifecycle Project 3
#Nick Packull-Mccormick
#Revision History:
#2023-11-24: Created

#This is the Prediction Engine module.
#It takes flag inputs and uses tries to match healt concerns with a diagnosis

class Prediction_Engine(object):

    PredictArray = []
    def __init__(self):
        p1 = Prediction("Flu", True, True, False, True, True)
        self.PredictArray.append(p1)
        p2 = Prediction("Cold", False, True, False, True, False)
        self.PredictArray.append(p2)
        p3 = Prediction("Low Blood Pressure", False, False, True, False, False)
        self.PredictArray.append(p3)
        p4 = Prediction("Dehydration", False, False, False, False, True)
        self.PredictArray.append(p4)

    def Predict(self, hrFlag, boFlag, bpFlag, tempFlag, fluidFlag):
        # make a for loop that runs throug each item in PredictArray
        PredictName = ""
        MaxMatch = 0
        for x in self.PredictArray:
            # compare each flag with the incomming flags
            # incriment a counter if they match
            counter = 0
            if(x.hrFlag == hrFlag):
                counter = counter +1
            if(x.boFlag == boFlag):
                counter = counter +1
            if(x.bpFlag == bpFlag):
                counter = counter +1
            if(x.tempFlag == tempFlag):
                counter = counter +1
            if(x.fluidFlag == fluidFlag):
                counter = counter +1

            # Check if counter is bigger than others, if so save name temporarily
            if(counter > MaxMatch):
                PredictName = x.name
                MaxMatch = counter
            
        # return the name of the prediction
        return PredictName


class Prediction(object):

    def __init__(self, name, hrFlag, boFlag, bpFlag, tempFlag, fluidFlag):
        self.name = name
        self.hrFlag = hrFlag
        self.boFlag = boFlag
        self.bpFlag = bpFlag
        self.tempFlag = tempFlag
        self.fluidFlag = fluidFlag



Test = Prediction_Engine()
output =Test.Predict(True, True, False, True, True)
print(output)
output = Test.Predict(False, False, False, False, True)
print(output)
