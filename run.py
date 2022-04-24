from user import User
from credentials import Credentials
import random
import string

def register_user(fname,lname,username,password,email,phone_number):
    #function to register new user
    new_user=User(fname,lname,username,password,email,phone_number)
    return new_user

def user_exist_login(password):
    #find user by password so they can login
    return User.user_exist(password)

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

 