class User:
     """
    Class that generates new instances of users
    """
user_list = [] # Empty contact list store detail of user

def __init__(self, username, password, email):

    

    self.username = username
    self.password = password
    self.email = email
    
def save_user(self):
    
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
        
        
@classmethod
def find_user_by_username(cls, username):
    
    for user in cls.user_list:
        if user.username == username:
            return user
        

def delete_user(self):
    '''
        delete_user method deletes a saved user from the user_list
        '''
    User.user_list.remove(self)
    
@classmethod
def display_all_users(cls):
    '''
    method that returns the all users in user list
    '''
    return cls.user_list    

    
class Credentials:
    
    """
        Class that generates new instances of credential
    """
    
    credential_list = []
    
def _init_(self, account, username, password):
    self.account = account
    self.username = username
    self.password = password
    
    
def save_credential(self):
    
        '''
        save_credential method saves credential objects into credential_list
        '''
        Credentials.credential_list.append(self)
        
def delete_credential(self):
    '''
        delete_credential method deletes a saved credential from the credential_list
        '''
    Credentials.credential_list.remove(self)    
    
@classmethod
def find_credential_by_account_type(cls, account):
    
    for credential in cls.credential_list:
        if credential.account == account:
            return account
                
            
    
    
    
    
    

    
    
        
    
            