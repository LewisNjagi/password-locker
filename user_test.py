import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_user = User("Lewis","Njagi","1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Lewis")
        self.assertEqual(self.new_user.last_name,"Njagi")
        self.assertEqual(self.new_user.password,"1234")

if __name__ == '__main__':
    unittest.main()
