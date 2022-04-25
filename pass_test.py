import unittest
from pass import User
from pass import Credentials

class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("SarahK", "233HR35") 
        
        
def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []        


def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"SarahK")
        self.assertEqual(self.new_user.password,"233HR35")
        self.assertEqual(self.new_user.email,"sarak@gmail.com")
      
def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.user_list),1)  
        
        
def test_find_user_by_username(self):
     '''
        test to check if we can find a user by user name and display it
    '''
    
     self.new_user.save_user()
     test_user = User("username", "password", "test@gmail.com")
     test_user.save_user()
     
     found_user = User.find_by_username("username")
     self.assertEqual(found_user.email, test_user.email)
     
def test_save_multiple_user(self):
    '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
    '''
    self.new_user.save_user()
    test_user = User("username", "password", "test@gmail.com")
    test_user.save_user()
    self.assertEqual(len(User.user_list),2)
    
         
     
     
def test_delete_user(self):
    '''
    test_delete_user to test if we can remove a user from our user list
    '''
    self.new_user.save_user()
    test_user = User("username", "password", "test@gmail.com")
    test_user.save_user()
    
    self.new_user.delete_user()
    self.assertEqual(len(User.user_list),1)
    
      
            
        
class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    '''
def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Yahoo", "Kammy", "233HR60") 
        
def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []        
        
def test_init(self):
    '''
        test_init test case to test if the new credential instance has initialized properly
    '''
    self.assertEqual(self.new_credential.account,"Yahoo")
    self.assertEqual(self.new_credential.username,"Kammy")
    self.assertEqual(self.new_credential.password,"233HR60")
    
    
def test_save_credential(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credential list
        '''
        self.new_credential.save_credential() # saving the new contact
        self.assertEqual(len(Credentials.credential_list),1) 
        
        
def test_save_multiple_credential(self):
    '''
            test_save_multiple_credential to check if we can save multiple user
            objects to our credential_list
    '''
    self.new_credential.save_credential()
    test_credential = Credentials("username", "password", "Instagram")
    test_credential.save_credential()
    self.assertEqual(len(User.user_list),2)
            
        
         
            
        
        
    
               
    
               


if __name__ == '__main__':
    unittest.main()
