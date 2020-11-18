from .. import Category


class SubCategory(Category):
    
    def __init__(self, name, description, notes, parent_category_id):
        super().__init__(name, description, notes)
        self._id = None
        self._parent_category_id = parent_category_id
        self._created_at = None
        