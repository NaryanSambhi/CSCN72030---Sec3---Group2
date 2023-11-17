import unittest   # The test framework
#from Body_Info import body_info
from Body_Info import body_info
import UserData
#import BMI
from Heart_Health import heart_Health
#import LoginSignup
#import main
#import Prescription
import os

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
   
   # pass to make sure that it does not raise a flag meaning that it is in range
    def test_checkTempFlag_inLimit_Pass(self):
        body = body_info(temp=99, fluid=4000)
        self.assertFalse(body.checkTempFlag())

    # pass to see if it will flag if it is over the limit
    def test_checkTempFlag_overLimit_Pass(self):
        body = body_info(temp=102, fluid=2000)
        self.assertTrue(body.checkTempFlag())

    # fail to make sure that it does raise a flag meaning that it is below range
    def test_checkTempFlag_overLimit_Fail(self):
        body = body_info(temp=80, fluid=2000)
        self.assertFalse(body.checkTempFlag())

    # tests for checkFluidFlag function

    # fail to see if it will raise true flag when in range
    def test_checkFluidFlag_inLimit_Fail(self):
        body = body_info(temp=99, fluid=4000)
        self.assertTrue(body.checkFluidFlag())

    # pass to make sure that it does not raise a flag meaning that it is in range
    def test_checkFluidFlag_inLimit_Pass(self):
        body = body_info(temp=99, fluid=1000)
        self.assertFalse(body.checkFluidFlag())
    
    # pass to see if it will flag if it is over the limit
    def test_checkFluidFlag_overLimit_Pass(self):
        body = body_info(temp=102, fluid=7000)
        self.assertTrue(body.checkFluidFlag())

    # fail to make sure that it does raise a flag meaning that it is over range
    def test_checkFluidFlag_overLimit_Fail(self):
        body = body_info(temp=80, fluid=-800)
        self.assertFalse(body.checkFluidFlag())



class Test_Heart_Health(unittest.TestCase):
    #pass to make sure the user is able to enter in their heart rate
    def test_set_hr_pass(self):
        hr = heart_Health(80,97,100)
        result  = hr.get_hr()
        self.assertEqual(result, 80)
        
    #pass to make sure the user is able to enter in their blood oxygen
    def test_set_bo_pass(self):
        hr = heart_Health(80,97,100)
        result  = hr.get_bo()
        self.assertEqual(result, 97)
    
    #pass to make sure the user is able to enter in their blood pressure
    def test_set_bp_pass(self):
        hr = heart_Health(80,97,100)
        result  = hr.get_bp()
        self.assertEqual(result, 100)
    
    #testing for the flags set by the user
    
    #this is supposed to pass
    def test_set_hrUL_pass(self):
        hr = heart_Health(80,97,100, 120, 20)
        result  = hr.get_hrUL()
        self.assertEqual(result, 120) 
    
    #this is supposed to pass
    def test_set_hrLL_pass(self):
        hr = heart_Health(80,97,100, 120, 20)
        result  = hr.get_hrLL()
        self.assertEqual(result, 20) 
    
   #this is supposed to pass
    def test_set_boUL_pass(self):
        hr = heart_Health(80,97,100, 120, 20, 100, 93)
        result  = hr.get_boUL()
        self.assertEqual(result, 100)  
        
    #this is supposed to pass
    def test_set_boLL_pass(self):
        hr = heart_Health(80,97,100, 120, 20, 100, 93)
        result  = hr.get_boLL()
        self.assertEqual(result, 93)
    
    #this is supposed to pass
    def test_set_bpUL_pass(self):
        hr = heart_Health(80,97,100, 120, 20, 100, 93, 150, 80)
        result  = hr.get_bpUL()
        self.assertEqual(result, 150)
    
    #this is supposed to pass
    def test_set_bpLL_pass(self):
        hr = heart_Health(80,97,100, 120, 20, 100, 93, 150, 80)
        result  = hr.get_bpLL()
        self.assertEqual(result, 20)
    
    #test cases for the flag checks
    
    #this is supposed to pass
    def test_checkHRFlag_overLimit_Pass(self):
        hr = heart_Health(heart_rate=120, blood_oxegen=100, blood_pressure=130)
        self.assertTrue(hr.checkHRFlag())
    
    #fail to see if it will flag if it is over the limit
    def test_checkHRFlag_overLimit_Fail(self):
        hr = heart_Health(heart_rate=120, blood_oxegen=100, blood_pressure=130)
        self.assertFalse(hr.checkHRFlag())

    #fail to make sure that it does not raise a flag meaning that it is in range
    def test_checkHRFlag_inLimit_Fail(self):
        hr = heart_Health(heart_rate=99, blood_oxegen=100, blood_pressure=130)
        self.assertTrue(hr.checkHRFlag())
 
    #pass to see if it will raise true flag when in range
    def test_checkHRFlag_inLimit_Pass(self):
        hr = heart_Health(heart_rate=91, blood_oxegen=100, blood_pressure=130)
        self.assertFalse(hr.checkHRFlag())
        
    #test cases for blood oxygen 
    #this is supposed to pass
    def test_checkBOFlag_overLimit_Pass(self):
        bo = heart_Health(heart_rate=120, blood_oxegen=100, blood_pressure=130)
        self.assertTrue(bo.checkBOFlag())
    
    # fail to see if it will flag if it is over the limit
    def test_checkBOFlag_overLimit_Fail(self):
        bo = heart_Health(heart_rate=120, blood_oxegen=100, blood_pressure=130)
        self.assertFalse(bo.checkBOFlag())

    #Fail to make sure that it does not raise a flag meaning that it is in range
    def test_checkBOFlag_inLimit_Fail(self):
        bo = heart_Health(heart_rate=99, blood_oxegen=98, blood_pressure=130)
        self.assertTrue(bo.checkBOFlag())
 
    # pass to see if it will raise true flag when in range
    def test_checkBOFlag_inLimit_Pass(self):
        bo = heart_Health(heart_rate=91, blood_oxegen=98, blood_pressure=130)
        self.assertFalse(bo.checkBOFlag())

    #test cases for blood pressure 
    #this is supposed to pass
    def test_checkBPFlag_overLimit_pass(self):
        bp = heart_Health(heart_rate=120, blood_oxegen=100, blood_pressure=130)
        self.assertTrue(bp.checkBPFlag())
    
    # fail to see if it will flag if it is over the limit
    def test_checkBPFlag_overLimit_fail(self):
        bp = heart_Health(heart_rate=120, blood_oxegen=100, blood_pressure=130)
        self.assertFalse(bp.checkBPFlag())

    # fail to make sure that it does not raise a flag meaning that it is in range
    def test_checkBPFlag_inLimit_Fail(self):
        bp = heart_Health(heart_rate=99, blood_oxegen=98, blood_pressure=100)
        self.assertTrue(bp.checkBPFlag())
 
    # pass to see if it will raise true flag when in range
    def test_checkBPFlag_inLimit_Pass(self):
        bp = heart_Health(heart_rate=91, blood_oxegen=98, blood_pressure=99)
        self.assertFalse(bp.checkBPFlag())
    
   
class Test_UserData(unittest.TestCase):
    #both are supposed to pass
    def setUp(self):
    
        self.user = UserData.UserData(name="John Doe", age=30)

        self.user.prescription_manager.add_prescription("Aspirin", "Pain relief", "10mg")
        self.user.prescription_manager.add_prescription("Ibuprofen", "Pain relief", "200mg")
        self.user.heart_health._heart_rate = 90
        self.user.heart_health._blood_oxygen = 80
        self.user.heart_health._blood_pressure = 70
        self.user.BMI._weight = 70
        self.user.BMI._height = 190
        self.user.body_Info._temp = 100
        self.user.body_Info._fluid = 750

        self.test_file = "test_save_to_file.pkl"

    def test_save_to_file(self):
        self.user.save_to_file(self.test_file)
        self.assertTrue(os.path.isfile(self.test_file))
        os.remove(self.test_file)   
   
    
if __name__ == '__main__':
    unittest.main()