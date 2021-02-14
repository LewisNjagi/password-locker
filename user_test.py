import unittest
from user import User, Credentials

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

    def test_save_user(self):
        '''
        test case to test if the user object is saved to the user list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_credential = Credentials("Lewis","Twitter","Lewis","1234")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.user_name,"Lewis")
        self.assertEqual(self.new_credential.site,"Twitter")
        self.assertEqual(self.new_credential.account_name,"Lewis")
        self.assertEqual(self.new_credential.password,"1234")

    def test_save_credentials(self):
        '''
        test case to test if the credentials object is saved to credentials lists
        '''

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()
