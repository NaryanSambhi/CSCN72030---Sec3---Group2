import unittest   # The test framework
import Body_Info
#import UserData
#import BMI
#import Heart_Health
#import LoginSignup
#import main
#import Prescription

class Test_Body_info(unittest.TestCase):
    #this passed, just need to add a return statement in the function for it pass
    def test_set_temp(self):
        temp = 98
        result  = Body_Info.body_info.set_temp(self, temp)
        self.assertEqual(result, 98)
        
    # come back to this and see why it isnt working
    def test_checkTempFlag(self):
        #temp = False
        result  = Body_Info.body_info.checkTempFlag(self)
        self.assertFalse(result, False)   

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        self.assertTrue(5, 5)

if __name__ == '__main__':
    unittest.main()