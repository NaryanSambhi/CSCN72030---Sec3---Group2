import unittest   # The test framework
import Body_Info
#import UserData
#import BMI
import Heart_Health
#import LoginSignup
#import main
#import Prescription

class Test_Body_info(unittest.TestCase):
    #pass to make the user is able to input in their body temp
    def test_set_temp_pass(self):
        temp = 98
        result  = Body_Info.body_info.set_temp(self, temp)
        self.assertEqual(result, 98)
        
    #pass to make sure the user is able to input in their fluid intake
    def test_set_fluid_pass(self):
        fluid = 2500
        result  = Body_Info.body_info.set_fluid(self, fluid)
        self.assertEqual(result, 2500)    
    
    #tests for set upper and lower temp limits
    def test_set_tempUpperLimit_pass(self):
        temp = 110
        result  = Body_Info.body_info.set_tempUpperLimit(self, temp)
        self.assertEqual(result, temp) 
    
    def test_set_tempLowerLimit_pass(self):
        temp = 60
        result  = Body_Info.body_info.set_tempLowerLimit(self, temp)
        self.assertEqual(result, temp) 
        
        
    #tests for set upper and lower fluid limits
    def test_set_fluidUpperLimit_pass(self):
        fluid = 7000
        result  = Body_Info.body_info.set_fluidUpperLimit(self, fluid)
        self.assertEqual(result, fluid) 
    
    def test_set_fluidLowerLimit_pass(self):
        fluid = -60
        result  = Body_Info.body_info.set_fluidLowerLimit(self, fluid)
        self.assertEqual(result, fluid) 
        
    
    #tests for the checkTempFlag function
    
    #fail to see if it will raise true flag when in range
    def test_checkTempFlag_inLimit_Fail(self):
        body = Body_Info.body_info(temp=99, fluid=4000)
        self.assertTrue(body.checkTempFlag()) 
    
    #pass to see if it will flag if it is over the limit
    def test_checkTempFlag_overLimit_Pass(self):
        body = Body_Info.body_info(temp=102, fluid=2000)
        self.assertTrue(body.checkTempFlag())
        
   #pass to make sure that it does not raise a flag meaning that it is in range
    def test_checkTempFlag_inLimit_Pass(self):
        body = Body_Info.body_info(temp=99, fluid=4000)
        self.assertFalse(body.checkTempFlag()) 
    
    #fail to make sure that it does raise a flag meaning that it is over range
    def test_checkTempFlag_overLimit_Fail(self):
        body = Body_Info.body_info(temp=80, fluid=2000)
        self.assertFalse(body.checkTempFlag())   

    #tests for checkFluidFlag function
    
    #fail to see if it will raise true flag when in range
    def test_checkFluidFlag_inLimit_Fail(self):
        body = Body_Info.body_info(temp=99, fluid=4000)
        self.assertTrue(body.checkFluidFlag()) 
    
    #pass to see if it will flag if it is over the limit
    def test_checkFluidFlag_overLimit_Pass(self):
        body = Body_Info.body_info(temp=102, fluid=7000)
        self.assertTrue(body.checkFluidFlag())
        
   #pass to make sure that it does not raise a flag meaning that it is in range
    def test_checkFluidFlag_inLimit_Pass(self):
        body = Body_Info.body_info(temp=99, fluid=1000)
        self.assertFalse(body.checkFluidFlag()) 
    
    #fail to make sure that it does raise a flag meaning that it is over range
    def test_checkFluidFlag_overLimit_Fail(self):
        body = Body_Info.body_info(temp=80, fluid=-800)
        self.assertFalse(body.checkFluidFlag())      
    


class Test_Heart_Health(unittest.TestCase):
    #pass to make sure the user is able to enter in their heart rate
    def test_set_hr_pass(self):
       hr = 98
       result  = Heart_Health.heart_Health.set_hr(self, hr)
       self.assertEqual(result, hr) 
    
    
    
if __name__ == '__main__':
    unittest.main()