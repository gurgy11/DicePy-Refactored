import re
from . import Field


class EmailField(Field):
    
    def __init__(self, name, value, required=True):
        super().__init__(name, value)
        self.required = required
        self.min_length = 5
        self.max_length = 255
        self.validation_errors = []
        
        self.validate_email()
        
    def validate_email(self):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
        if (re.search(regex, self.value)) is not True:
            self.validation_errors.append('The email {} provided is invalid!'.format(self.value))