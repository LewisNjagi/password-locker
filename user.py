class User:
    """
    Class that generates new intances of users
    """
    user_list = []

    def __init__(self,first_name,last_name,password):

        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

class Credentials:
    """
    Class to generate account credentials
    """
    credentials_list = []

    @classmethod
    def __init__(self,user_name,site,account_name,password):

        self.user_name = user_name
        self.site = site
        self.account_name = account_name
        self.password = password
