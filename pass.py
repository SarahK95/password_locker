class User:
     """
    Class that generates new instances of users
    """
user_list = [] # Empty contact list store detail of user

def __init__(self, username, password):

    

    self.username = username
    self.password = password
    
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
        