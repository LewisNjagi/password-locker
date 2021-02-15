#!/usr/bin/env python3
from user import User, Credentials

def create_user(first_name,last_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def verify_user(first_name,password):
    '''

    '''
    valid = Credentials.valid_user(first_name,password)
    return valid

def create_credentials(user_name,site,account_name,password):
    '''
    Function to create user credentials
    '''
    new_credential = Credentials(user_name,site,account_name,password)
    return new_credential

def save_credentials(Credentials):
    '''
    Function to save user credentials
    '''
    Credentials.save_credentials()

def main():
    print(' ')
    print('Hello, Welcome to Password Locker')
    print("-"*60)
    while True:
        print('\n')
        print("Use these short codes: \n ca - Create a new Account \n li - Log Into Existing Account \n ex - Exit the user list ")
        short_code = input('\n Enter your short code: ').lower()
        if short_code == 'ca':
            print("\n")
            print('To create a new account: ')

            print("---Enter your First Name---")
            first_name = input("First Name: ")

            print("---Enter your Last Name---")
            last_name = input("Last Name: ")

            print("---Enter your Password---")
            password = input("Password: ")

            save_user(create_user(first_name,last_name,password))
            print("\n")
            print("-"*60)
            print(f"New Account created for: {first_name} {last_name} your password: {password}")
            print("-"*60)

        elif short_code == 'li':
            print('Login Into Your Account: ')

            print("---Enter your First Name---")
            first_name = input("First Name: ")

            print("---Enter your Password---")
            password = input("Password: ")
            
            validity = verify_user(first_name,password)
            if validity == first_name:
                print("\n")
                print("-"*60)
                print(f'Welcome {first_name}.You have logged into you account successfully. Use these short codes to continue.')
                print("-"*60)
                while True:
                    print("\n")
                    print('Navigation codes: \n cc - Create Account Credential \n dc - Display Account Credentials \n ex-Exit')
                    nav_code = input('\n Enter your short code: ').lower()
                    if nav_code == 'cc':
                        print("Create Account Credentials")

                        print("---Enter Website---")
                        site = input("Site Name ")

                        print("---Enter AccountName---")
                        account_name = input("AccountName ")

                        print("\n")
                        print('Password: \n gp - Generate Password \n ep - Enter Password \n ex-Exit')
                        pass_code = input('\n Enter your pasword short code: ').lower()
                        if pass_code == 'gp':
                            print("we'll get there")
                        elif pass_code == 'ep':
                            print("Enter your Password here...")
                            password = input("Password ")
                        elif pass_code == 'ex':
                            break
                        else:
                            print("You did not make a selection")
                    elif nav_code == 'dc':
                        


if __name__=='__main__':
    main()