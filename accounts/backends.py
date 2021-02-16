
from django.contrib.auth.models import User

#   class to deal with email authenticate automatically
class EmailAuthentication : 

    """
        Function to authenticate a user using his / her email address
    """
    def authenticate(self, request, username = None, password = None) : 
        try : 
            user = User.objects.get(email = username)
            #   if the password is validated returns the user
            if user.check_password(password) : 
                return user

            #   returns None if the user is not validated
            return None

        except User.DoesNotExist : 
            return None

    
    """
        Method to return the user details if authenticated succesfully
    """
    def get_user(self, user_id) : 
        
        try : 
            user = User.objects.get(id = user_id)

            return user

        except User.DoesNotExist : 
            return None
