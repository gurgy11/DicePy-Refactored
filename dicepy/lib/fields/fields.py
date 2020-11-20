class Field():

    def __init__(self, name, value, required=False, min_length=None, max_length=None):
        self.name = name
        self.value = value
        self.required = required
        self.min_length = min_length
        self.max_length = max_length
        self.validation_errors = []

    def validate(self):
        validation_errors = []
        if self.required and self.value is None:
            validation_errors.append(
                'The {} field is required and cannot be empty!'.format(self.name))

            if self.min_length is not None and len(self.value) < self.min_length:
                validation_errors.append('The {} field must be at least {} characters long!'.format(
                    self.name, self.min_length))

            if self.max_length is not None and len(self.value) > self.max_length:
                validation_errors.append('The {} field cannot be greater than {} characters long!'.format(
                    self.name, self.max_length))
        
        self.validation_errors = validation_errors