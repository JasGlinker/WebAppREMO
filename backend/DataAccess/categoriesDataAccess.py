from DataAccess.DataAccess import DataAccess as DA
import logging
# Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class CategoriesDataAccess:
    def __init__(self):
        self.category_data_access = DA(table_name='categories')
        logger.info("CategoriesDataAccess initialized")

    def get_all_categories(self):
        logger.info("CategoriesDataAccess.get_all_categories")
        return self.category_data_access.read_all()

    def get_category_by_name(self, name:str):
        logger.debug("In get_category_by_name: %s", name)
        conn = self.category_data_access._get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM categories WHERE ca_name = %s"
        try:
            cursor.execute(query, (name,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()