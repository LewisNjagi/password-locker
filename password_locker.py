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
    while True:
        print('\n')
        print("Use these short codes: \n ca - Create a new Account \n li - Log Into Existing Account \n ex - Exit the user list ")
        short_code = input('\n Enter your short code: ').lower()
        if short_code == 'ca':
            print('To create a new account: ')

            print("---Enter your First Name---")
            first_name = input("First Name: ")

            print("---Enter your Last Name---")
            last_name = input("Last Name: ")

            print("---Enter your Password---")
            password = input("Password: ")

            save_user(create_user(first_name,last_name,password))
            print("\n")
            print(f"New Account created for: {first_name} {last_name} your password: {password}")

        elif short_code == 'li':
            print('Login Into Your Account: ')

            print("---Enter your First Name---")
            user_name = input("First Name: ")

            print("---Enter your Password---")
            password = input("Password: ")


if __name__=='__main__':
    main()