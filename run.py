#!/usr/bin/env python3.8
from traceback import print_last
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
    return Credentials.display_all_credential()   

def credential_exists(password):
    """
    Function that check if a Credentials exists with that password and return true or false
    """
    return Credentials.credential_exist(password)

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential_by_account_type(account)

def copy_password(account):
    return Credentials.copy_password(account)

def generate_password():
    '''
    generates a random password for the user.
    '''
    password=Credentials.generate_password()
    return password

def main():
    print("Hello Welcome! To proceed create new account.\n use ca -- to create new acc with username and password")
    short_code = input().lower()
    if short_code == 'ca':
        print("New User")
        print("_"*20)
        username = input()
        
    while True:
        print("use short code\n ip to Input Password: \n gp to generate password") 
        password_option = input().lower()
        if password_option == 'ip':
            password = input("Enter Password\n")
            break
        elif password_option == 'gp':
            password = generate_password()
             
            break
        else:
            print("invalid password,try again")
            
    save_user(create_user(username, password))
    print("_"*100)
    print(f"Hello {username}, Your account has succesfully been created!Your password is {password}")
    print("_"*100)
    
    
    while True:
        print("Use these short codes : cc - create a new credential,\n del- delete credential,\n dc - display credential,\n fc -find a credential,\n ex -exit the credential list ")
        
        short_code = input().lower()
        
        if short_code == 'cc':
            print("Create new credential")
            print("_"*10)
            
            print("Account type...")
            account =input().lower()
            print("Your username for this account")
            username = input()
            
            while True:
                print("use short code ip to Input Password:\n gp- generate password")
                password_option = input().lower()
                if password_option == 'ip':
                    password = input("Enter Password\n")
                    break
                elif password_option == 'gp':
                    password = generate_password()
                    break
                else:
                    print("invalid password,try again")
                    
            save_credential(create_credential(account, username,password))
            print('\n')
            print(f"Account:{account} \n Username:{username}\n Password:{password} created succesfully!" )
            print('\n')
            
        elif short_code == 'dc':
            
            results= display_credential()
            print("Here are your credentials")
            print("_"*50)
            for account in results:
                print(f"Account:{account.account}\n ,Username:{account.username}\n ,Password:{account.password}")
                print("_"*50)
            
                  
                
                
        elif short_code == 'fc':
            print("Enter account you want to find")
            search_username = input().lower()
            if find_credential(search_username):
                search_credential = find_credential(search_username)
                
                print(f"Username: {search_credential.username} Password :{search_credential.password}")
                print('-' * 50)
                
            else:
                print("Credential does not exist")
                print("\n")    
                
                
        elif short_code == 'del':
            print("Enter account you want to delete")
            search_account = input().lower()
            # delete_credential(find_credential(search_username))
            if find_credential(search_account):
                cred =find_credential(search_account)
                delete_credential(cred)
                
                print("\n")
                print(f"Your  account has been successfully deleted!")
                print('\n')
            else:
                print("No account found")
                
              
                
        elif short_code == 'ex':
            print("Bye .......")
            break
        else:
            
            print("I really didn't get that. Please use the short codes")
            
if __name__ == '__main__':
    main()


            
                    
                    
                
                
                
              
              
                
                
                 
                 
                
                
                
              
            
             
               
            
             
               
              
            
              
             
            
            
            
            
            
            
            
            
            
            
           
if __name__ == '__main__':
    main()            
            
        
            
            
            
   
                
  
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                  
                
                     
            
            
            
            
        

        

    
     
     
     
     
                                                                                                                                                                                                                                                                                             
     
     
    

     
    
    