#!/usr/bin/env python3.9
from user import User
from credentials import Credentials
import random
import string

def create_user(fname,lname,username,password,email,phone_number):
    #function to register new user
    new_user=User(fname,lname,username,password,email,phone_number)
    return new_user

def save_user(user):
    #save user account
    user.register_user(user)

def user_exist_login(username,password):
    #find user by password so they can login
    return User.user_exist(username,password)

def create_account_credential(account,username,email,password):
    #function to create new credentials object
    new_credential=Credentials(account,username,email,password)
    return new_credential

def save_account_credential(credential):
    #save credential
    credential.save_credentials()

def del_credential(credential):
    #delete credential
    credential.delete_credential()

def find_credential(account):
    #search for credential using account name
    return Credentials.find_by_account(account)  

def existing_credential(account):
    #check if a credential exists 
    return Credentials.credential_exists(account)

def displays_credentials():
    #returns all saved credentials
    return Credentials.display_credentials()

def tocopy_password(account):
    #copy password to clipboard
    return Credentials.copy_password(account)

#MAIN function
def main():
    print('Hello! Welcome to Lock-n-Key. \n Do you have an account?  enter y or n')
    have_account=input().lower()

    if have_account=='n':
        print('New Account')
        print('-' *10)

        print('First name...')
        f_name=input()

        print('Last name...')
        l_name=input()

        print('Username...')
        user_name=input()

        print('Email...')
        e_address=input()

        print('Phone number...')
        p_number=input()

        print('Password...')
        passwrd=input() 

        save_user(create_user(f_name,l_name,user_name,passwrd,e_address,p_number))

        print('\n')

    elif have_account=='y':
        print('Please enter your username and password')
        print('-'*10)
        print('Username...')
        user_name=input()
        print('\n')
        print('Password...')
        passwrd=input()
        print('\n')

        if user_exist_login(user_name,passwrd):
            print()
            create_account_credential(account,username,email,password)



