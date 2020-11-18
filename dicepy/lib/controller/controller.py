from dicepy.lib.database import Database


class Controller():
    
    def __init__(self):
        self.db = Database()
        self.table = ''
        self.columns = []
    
    def form_to_model(self, form):
        pass
    
    def form_to_values(self, form):
        pass
    
    def result_to_model(self, result):
        pass
    
    def select_all(self):
        results = self.db.select_all(self.table)
        return results
    
    def select_by_id(self, record_id):
        results = self.db.select_by_id(self.table, record_id)
        return results[0]
    
    def create(self, form):
        pass
    
    def register(self, form):
        pass
    
    def edit(self, form, record_id):
        pass
    
    def delete(self, record_id):
        pass