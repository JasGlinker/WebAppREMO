from flask import Blueprint, request, jsonify
from DataAccess.categoriesDataAccess import CategoriesDataAccess

#this is for frontend data access to get current categories from db

CatDA = CategoriesDataAccess()

data_page = Blueprint('data', __name__)

@data_page.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        categories = CatDA.get_all_categories()
        cat_names = []
        for cat in categories:
            cat_names.append(cat['ca_name'])
        print(categories)
        print(cat_names)
        return cat_names
