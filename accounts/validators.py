import re


def is_email(email) : 
    regex = re.compile('^([a-zA-Z0-9\-\.\_])+@([a-zA-Z0-9\-\.\_])+\.([a-zA-Z0-9]{2,4})$')
    print("response = ", regex.match(email), email)
    return regex.match(email)