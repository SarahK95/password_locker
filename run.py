#!/usr/bin/env python3.8
from password import User, Credentials

def create_user(username, password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
     '''
    Function to save a new user
    '''
     user.save_user()
    
def delete_user(user):   
    '''
    Function to delete a contact
    '''
    user.delete_contact() 
    
def find_user(username):
    '''
    Function that finds a user by username and returns the user
    '''
    return User.find_by_username(username) 

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()  

def create_credential(account, username, password):
    '''
    Function to create a new credentail with a account, username and password
    '''
    new_credential = Credentials(account, username, password)
    return new_credential


def save_credential(credential):
     """
    Function to save Credentials to the credentials list
    """
     credential.save_credential() 
     
def delete_credential(credential):
    """
    Function to delete a Credentials from credential list
    """
    credential.delete_credential()  
    
def display_credential():
    """
    Function to display existing credential
    """
    return Credentials.display_credential()   

def credential_exists(password):
    """
    Function that check if a Credentials exists with that password and return true or false
    """
    return Credentials.credential_exist(password)

def copy_password(account):
    return Credentials.copy_password(account)

def main():
    print("Hello Welcome! What is your name?")
    user_username = input()
    
    print(f"Hello {user_username}. Welcome")
    print('\n')
    
    while True:
        print("Use these short codes : cu - create a new user, du - display user, fu -find a user, ex -exit the user list ")
        
        short_code = input().lower()
        
        if short_code == 'cu':
            print("New user")
            print("_"*10)
            
            print("Username...")
            username = input()
            
            print ("Password...")
            password = input()
            
            print('\n')
            
        elif short_code == 'du':
            if display_user():
                print("Here is a list of all your users")
                print('\n')
                
                for user in display_user():
                    print(f"{user.username} ")
                    print('\n')
                  
            else:
                print('\n')
                print("No user found")
                print('\n') 
                
        elif short_code == 'fu':
            print("Enter username to find user")
            search_username = input()
            
            if find_user(search_username):
                search_username = find_user(search_username)
                print(f"{search_username.username}")
                print("_"*20)      
                
                print(f"Password{search_username.username}") 
                    
            else:
                print("User does not exist") 
                print('\n') 
                
        elif short_code == "ex":
            print("Bye. Have a good one!")
            break
        
        else:
            print("I really didn't get that. Please use the short codes")
            
if __name__ == '__main__':
    main()            
            
        
            
            
            
   
                
  
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                  
                
                     
            
            
            
            
        

        

    
     
     
     
     
                                                                                                                                                                                                                                                                                             
     
     
    

     
    
    