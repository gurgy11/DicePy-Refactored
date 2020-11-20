from . import Field


class PhoneField(Field):
    
    def __init__(self, name, value):
        super().__init__(name, value)
        self.required = True
        self.min_length = 6
        
        self.validate_phone()
        
    def validate_phone(self):
        if int(self.value) is not type(int):
            self.validation_errors.append('The {} field can only contain digits!'.format(self.name))