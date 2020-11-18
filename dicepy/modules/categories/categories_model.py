class Category():
    
    def __init__(self, category_name, description, notes):
        self._id = None
        self._category_name = category_name
        self._description = description
        self._notes = notes
        self._created_at = None