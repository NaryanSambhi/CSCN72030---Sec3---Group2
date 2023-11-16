import unittest   # The test framework
#from Body_Info import body_info
from Body_Info import body_info
#import UserData
#import BMI
import Heart_Health
#import LoginSignup
#import main
#import Prescription

class Test_Body_info(unittest.TestCase):
    #pass to make the user is able to input in their body temp
    def test_set_temp_pass(self):
        body = body_info(98,2000)
        result  = body.get_temp()
        self.assertEqual(result, 98)
        
    #make the rest of changes based on test_set_temp_pass    
    
    #pass to make sure the user is able to input in their fluid intake
    def test_set_fluid_pass(self):
        body = body_info(98,2500)
        result  = body.get_fluid()
        self.assertEqual(result, 2500)    
    
    #tests for set upper and lower temp limits
    def test_set_tempUpperLimit_pass(self):
        body = body_info(97,2000,98, 110)
        result  = body.get_tempUpperLimit()
        self.assertEqual(result, 110) 
    
    def test_set_tempLowerLimit_pass(self):
        body = body_info(97,2000,60, 110)
        result  = body.get_tempLowerLimit()
        self.assertEqual(result, 60) 
        
        
    #tests for set upper and lower fluid limits
    def test_set_fluidUpperLimit_pass(self):
        body = body_info(97,2000,60, 110, 0, 10000)
        result  = body.get_fluidUpperLimit()
        self.assertEqual(result, 10000) 
    
    def test_set_fluidLowerLimit_pass(self):
        body = body_info(97,2000,60, 110, -60, 10000)
        result  = body.get_fluidLowerLimit()
        self.assertEqual(result, -60) 
        
    
    #tests for the checkTempFlag function

    # fail to see if it will raise true flag when in range
    def test_checkTempFlag_inLimit_Fail(self):
        body = body_info(temp=99, fluid=2000)
        self.assertTrue(body.checkTempFlag())

    # pass to see if it will flag if it is over the limit
        body = body_info(temp=102, fluid=2000)
        self.assertTrue(body.checkTempFlag())

    # pass to make sure that it does not raise a flag meaning that it is in range
    def test_checkTempFlag_inLimit_Pass(self):
        body = body_info(temp=99, fluid=4000)
        self.assertFalse(body.checkTempFlag())

    # fail to make sure that it does raise a flag meaning that it is below range
    def test_checkTempFlag_overLimit_Fail(self):
        body = body_info(temp=80, fluid=2000)
        self.assertTrue(body.checkTempFlag())

    # tests for checkFluidFlag function

    # fail to see if it will raise true flag when in range
    def test_checkFluidFlag_inLimit_Fail(self):
        body = body_info(temp=99, fluid=4000)
        self.assertTrue(body.checkFluidFlag())

    # pass to see if it will flag if it is over the limit
    def test_checkFluidFlag_overLimit_Pass(self):
        body = body_info(temp=102, fluid=7000)
        self.assertTrue(body.checkFluidFlag())

    # pass to make sure that it does not raise a flag meaning that it is in range
    def test_checkFluidFlag_inLimit_Pass(self):
        body = body_info(temp=99, fluid=1000)
        self.assertFalse(body.checkFluidFlag())

    # fail to make sure that it does raise a flag meaning that it is over range
    def test_checkFluidFlag_overLimit_Fail(self):
        body = body_info(temp=80, fluid=-800)
        self.assertFalse(body.checkFluidFlag())



class Test_Heart_Health(unittest.TestCase):
    #pass to make sure the user is able to enter in their heart rate
    def test_set_hr_pass(self):
       hr = 98
       result  = Heart_Health.heart_Health.set_hr(self, hr)
       self.assertEqual(result, hr) 
    
    
    
if __name__ == '__main__':
    unittest.main()