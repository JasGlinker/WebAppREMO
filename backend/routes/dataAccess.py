from flask import Blueprint, request, jsonify
from DataAccess.categoriesDataAccess import CategoriesDataAccess
import logging
# Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

#this is for frontend data access to get current categories from db

CatDA = CategoriesDataAccess()

data_page = Blueprint('data', __name__)

@data_page.route('/data', methods=['GET', 'POST'])
def data():
    logger.info('request for category data')
    if request.method == 'GET':
        categories = CatDA.get_all_categories()
        cat_names = []
        for cat in categories:
            cat_names.append(cat['ca_name'])
        logger.debug("in data access got categories: %s" % categories)
        logger.debug("in data access got cat_names: %s" % cat_names)
        return cat_names
