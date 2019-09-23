import unittest  
import pyperclip
from user import User 

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("limo","brian","limobrian","limooh") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"limo")
        self.assertEqual(self.new_user.last_name,"brian")
        self.assertEqual(self.new_user.username,"limobrian")
        self.assertEqual(self.new_user.password,"limooh")
        

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)
        

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0703276744","test@user.com") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
         

if __name__ == '__main__':
    unittest.main()

    