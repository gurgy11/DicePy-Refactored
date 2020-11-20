class Form():
    
    def __init__(self, name, fields):
        self.name = name
        self.fields = fields
        self.valid = False
        self._validation_errors = []
        
        self.validate()
        
    @property
    def validation_errors(self): return self._validation_errors   
    
    @validation_errors.setter
    def validation_errors(self, validation_errors): self._validation_errors = validation_errors 
    
    def validate(self):
        for field in self.fields:
            if len(field.validation_errors) > 0:
                self.validation_errors.append(field.validation_errors)
        if len(self.validation_errors) > 0:
            self.valid = False
        else:
            self.valid = True
            
    def get_errors(self):
        return self.validation_errors