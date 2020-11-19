import math
from . import Category
from dicepy.lib.database import Database


class CategoriesController():
    
    def __init__(self):
        self.db = Database()
        self.table = 'categories'
        self.columns = ['category_name', 'description', 'notes']
        
    def form_to_model(self, form):
        category = Category(form.get('category_name'), form.get('description'), form.get('notes'))
        return category
    
    def form_to_values(self, form):
        category = self.form_to_model(form)
        values = (category.category_name, category.description, category.notes)
        return values
    
    def result_to_model(self, result):
        category = Category(result[1], result[2], result[3])
        category.id = result[0]
        category.created_at = result[4]
        return category
    
    def select_all(self):
        results = self.db.select_all(self.table)
        
        categories = []
        for res in results:
            category = self.result_to_model(res)
            categories.append(category)
            
        return categories
    
    def select_by_id(self, category_id):
        result = self.db.select_by_id(self.table, category_id)
        category = self.result_to_model(result)
        return category
    
    def category_name_exists(self, category_name):
        results = self.db.select_all_where(self.table, 'category_name', category_name)
        
        if len(results) > 0:
            return True
        else:
            return False
    
    def create(self, form):
        ''' Creates a new category in the database '''
        
        ''' Validate '''
        errors = []
        
        if self.category_name_exists(form.get('category_name')) is True:
            error = 'The category name provided is already being used!'
            errors.append(error)
        else:
            values = self.form_to_values(form)
            self.db.insert_record(self.table, self.columns, values)
            
        return errors
    
    def number_of_rows(self):
        return self.db.number_of_records(self.table)
    
    def number_of_pages(self, limit):
        num_rows = self.number_of_rows()
        num_pages = math.ceil(num_rows / limit)
        
        return num_pages
    
    def get_start_index(self, page, limit):
        start_index = int((page - 1) * limit)
        return start_index
    
    def get_end_index(self, page, limit):
        end_index = int(page * limit)
        return end_index
    
    def select_in_range(self, page, limit):
        start_index = self.get_start_index(page, limit)
        end_index = self.get_end_index(page, limit)
        
        all_categories = self.select_all()
        categories_in_range = []
        
        in_range = False
        for cat in all_categories:
            
            if all_categories.index(cat) == start_index:
                in_range = True
            elif all_categories.index(cat) == end_index:
                in_range = False
            
            if in_range is True:
                categories_in_range.append(cat)
                
        return categories_in_range
    
    def edit(self, category_id, form):
        errors = []
        
        if self.category_name_exists(form.get('category_name')) is True:
            error = 'The category name provided is already being used!'
            errors.append(error)
        else:
            values = self.form_to_values(form)
            self.db.update_record(self.table, self.columns, values, category_id)
            print('Edited category with ID: ' + str(category_id))
            
        return errors
    
    def delete(self, category_id):
        self.db.delete_record(self.table, category_id)
        print('Delete category with ID: ' + str(category_id))