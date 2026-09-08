from DataAccess.DataAccess import DataAccess as DA

class CategoriesDataAccess:
    def __init__(self):
        self.category_data_access = DA(table_name='categories')

    def get_all_categories(self):
        return self.category_data_access.read_all()
