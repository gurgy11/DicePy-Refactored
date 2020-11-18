class Category():
    
    def __init__(self, category_name, description, notes):
        self._id = None
        self._category_name = category_name
        self._description = description
        self._notes = notes
        self._created_at = None
        
    ''' Properties '''
    
    @property
    def id(self):
        return self._id
    
    @property
    def category_name(self):
        return self._category_name
    
    @property
    def description(self):
        return self._description
    
    @property
    def notes(self):
        return self._notes
    
    @property
    def created_at(self):
        return self._created_at
    
    ''' Setters '''
    
    @id.setter
    def id(self, category_id):
        self._id = category_id
        
    @category_name.setter
    def category_name(self, category_name):
        self._category_name = category_name
        
    @description.setter
    def description(self, description):
        self._description = description
        
    @notes.setter
    def notes(self, notes):
        self._notes = notes
        
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
        
    ''' To Dict '''
    def to_dict(self):
        category_dict = {
            'id': self._id,
            'category_name': self._category_name,
            'description': self._description,
            'notes': self._notes,
            'created_at': self._created_at
        }
        
        return category_dict