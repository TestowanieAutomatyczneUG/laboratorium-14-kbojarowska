import re

class Author:
    def __init__(self, firstName, lastName, email):
        if type(firstName) is not str:
            raise Exception("First name must be str")
        elif type(lastName) is not str:
            raise Exception("Last name must be str")
        elif type(email) is not str and not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',email):
            raise Exception("Email must be str and must be an email")
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
