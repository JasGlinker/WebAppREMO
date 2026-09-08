from DataAccess.DataAccess import DataAccess as DA

class CategoriesDataAccess:
    def __init__(self):
        self.category_data_access = DA(table_name='categories')

    def get_all_categories(self):
        return self.category_data_access.read_all()

    def get_category_by_name(self, name:str):
        print('get category by name', name)
        conn = self.category_data_access._get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM categories WHERE ca_name = %s"
        try:
            cursor.execute(query, (name,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()