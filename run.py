#!/usr/bin/env python3.9
import sys
from user import User
from credentials import Credentials
import random
import string

def create_user(fname,lname,username,password,email,phone_number):
    '''function to register new user'''
    new_user=User(fname,lname,username,password,email,phone_number)
    return new_user

def save_user(user):
    '''save user account'''
    user.register_user()

def user_exist_login(username,password):
    '''find user by password so they can login'''
    return User.user_exist(username,password)

def create_account_credential(account,username,email,password):
    '''function to create new credentials object'''
    new_credential=Credentials(account,username,email,password)
    return new_credential

def save_account_credential(credential):
    '''save credential'''
    credential.save_credential()

def del_credential(credential):
    '''delete credential'''
    credential.delete_credential()

def find_credential(account):
    '''search for credential using account name'''
    return Credentials.find_by_account(account)  

def existing_credential(account):
    '''check if a credential exists'''
    return Credentials.credential_exists(account)

def displays_credentials():
    '''returns all saved credentials'''
    return Credentials.display_credentials()

def tocopy_password(account):
    '''copy password to clipboard'''
    return Credentials.copy_password(account)


def main():
    '''MAIN function'''
    def log_in():
        '''main function that runs after login'''
        if user_exist_login(user_name,passwrd):
            print(f'Login successful! Welcome {user_name} ')
            print('-'*20)
            
            print('Please use these short-codes:\n ac -add new credential \n fc - find credential by account \n dc -display all saved credentials\n del -delete a credential\n ex -exit' )
            
            short_code=input().lower()

            if short_code=='ac':
                print('New Credential')
                print('-'*10)

                print('Account name...')
                account=input()

                print('Username...')
                username=input()

                print('Email...')
                email=input()

                print('To manually enter a password type M ; To autogenerate a password type G ')
                psw=input().lower()
                if psw=='g':
                    print('Enter the length of your password')
                    length=int(input())
                    characters=string.ascii_letters+string.punctuation+string.digits
                    password=''.join(random.choice(characters) for x in range(0,length))
                    print('autogenerated!')
                    

                elif psw=='m':
                    print('Enter a password')
                    password=input()
                    print('Password added')

                else:
                    print('I did not quite get that. Please use a valid prompt')

                save_account_credential(create_account_credential(account,username,email,password))

                print('\n')
                print(f"New credential for {username}'s {account} created and saved successfully. ")

            elif short_code=='fc':
                print('Enter the account you want to find')
                search_account=input()

                if existing_credential(search_account):
                    found_account=find_credential(search_account)

                    print(f'Found {found_account.account} for {found_account.username}. ')
                    print('-'*20)
                    print(f'Email: {found_account.email} \n Password: {found_account.password} ')

                else:
                    print('Account does not exist')

            elif short_code=='del':
                print('Enter the account name you want to delete')
                delete_account=input()

                if existing_credential(delete_account):
                    del_account=find_credential(delete_account)
                    del_credential(del_account)
                    print(f'{del_account.account} credentials for {del_account.username} deleted successfully.')
                else:
                    print('The account credential does not exist')

            elif short_code=='dc':
                if displays_credentials():
                    print('Here is a list of your saved credentials.')
                    print('\n')

                    for credential in displays_credentials():
                        print(f'Account: {credential.account} \n Username: {credential.username}\n Password: {credential.password} ')
                        print('\n')

                else:
                    print('You dont seem to have any credentials saved.')

            elif short_code=='cp':
                print('Enter account whose password you want to copy.')
                copy_account=input()

                if existing_credential(copy_account):
                    print('account exists')
                    copy_passwd=find_credential(copy_account)
                    tocopy_password(copy_passwd)

                    print(f'The password for {copy_passwd.account} has been copied to clipboard ')

                else:
                    print('Credential not found.')

            elif short_code=='ex':
                print(f'Bye {user_name}... ')
                sys.exit()
            

            else:
                print('I did not get that. Please use the short codes.')

        else:
            print('we cannot find your account. Please create a new user account')
            sys.exit()


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
        print('User created successfully')
        while True:
            log_in()

    elif have_account=='y':
        print('Please enter your username and password')
        print('-'*10)
        print('Username...')
        user_name=input()
        
        print('Password...')
        passwrd=input()
        print('\n')

        while True:
            log_in()   

    else:
        print('Please confirm if you have an account or not')


    
           
if __name__=='__main__':
    main()


