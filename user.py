import pyperclip 
from credential import Credential

class User:

    user_list = []  

    def __init__(self,first_name,last_name,name,password):
 


        self.first_name = first_name
        self.last_name = last_name
        self.username = name
        self.password = password

        

    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.user_list.append(self)  


    def delete_user(self):

        User.user_list.remove(self)

    @classmethod
    def find_by_name(cls,name):


        for user in cls.user_list:
            if user.username == name:
                return user
            
    @classmethod
    def user_exist(cls,name):

        for user in cls.user_list:
            if user.username == name:
                    return True

        return False
    
    @classmethod
    def display_users(cls):

        return cls.user_list

    @classmethod
    def copy_password(cls,name):
        user_found = User.find_by_name(name)
        pyperclip.copy(user_found.password)
        
    @classmethod
    def display_user(cls,password):

        user_user_list = []

        for user in cls.user_list:
            if user.user_password == password:
                user_user_list.append(password)

        return user_user_list

    @classmethod
    def log_in(cls, name, password):

    
        for user in cls.user_list:
            if user.username == name and user.password == password:
                return Credential.credential_list

        return False

