import pyperclip
from user import User
from credential import Credential



def create_user(first_name, last_name, phone, password):

    new_user = User(first_name, last_name, phone, password)
    return new_user


def save_users(user):

    user.save_user()


def del_user(user):

    user.delete_user()


def find_user(name):

    return User.find_by_name(name)

def check_existing_users(name):

    return User.user_exist(name)


def display_users():

    return User.display_users()

def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)



def main():
    print("Welcome to your  password locker. What is your name?")
    user_name = input()

    print(f"Hi {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print(
                        "Use these cheat codes to navigate through : cn - create a new user, Du - display users, Fu -find a user, Lu - log users ,ex -exit the users list ")

                    cheat_code = input().lower()

                    if cheat_code == 'cn':
                            print("New Credentials")
                            print("-"*10)

                            print("First name ....")
                            f_name = input()

                            print("Last name ...")
                            l_name = input()

                            print("Username ...")
                            p_name = input()

                            print("password ...")
                            u_name = input()

                            # create and save new contact.
                            save_users(create_user(
                                f_name, l_name, p_name, u_name))
                            print('\n')
                            print(f"New User {f_name} {l_name} created")
                            print('\n')

                    elif cheat_code == 'Du':

                            if display_users():
                                    print("Here is a list of all your users")
                                    for user in display_users():
                                            print(
                                                f"{user.first_name} {user.last_name} .....{user.username}")
                            else:
                                    print("You dont have any users saved yet")
                                    
                    elif cheat_code == 'Lu':
                                    print("Log into Password Locker Account")
                                    print("Enter the user name")
                                    username = input()
                                    if user_log_in(username,u_name) == "":
                                        print("Please try again or create a new account")
                                    else:
                                        user_log_in(username,u_name)
                                        print(f'''{username} welcome to your Credentials\n
                                        Use these cheat codes to get around''')
                                        print("Enter the password")
                                        u_name = input()

                    elif cheat_code == 'Fu':

                            print("Enter the username you want to search for")

                            search_name = input()
                            if check_existing_users(search_name):
                                    search_user = find_user(search_name)
                                    print(
                                        f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(
                                        f"Username.......{search_user.username}")
                                    print(
                                        f"Password.......{search_user.password}")
                            else:
                                    print("That user does not exist in our system")

                    elif cheat_code == "ex":
                            print("Thank you for using this application you are welcome to use it again  ")
                            break
                    else:
                            print(
                                "Please use the cheat codes for better understanding.")

if __name__ == '__main__':

    main()
