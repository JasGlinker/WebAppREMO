import datetime
from typing import List

from flask import Blueprint, render_template, request, jsonify
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
from DataAccess.categoriesDataAccess import CategoriesDataAccess



actDA = ActivitiesDataAccess()
CatDA = CategoriesDataAccess()
create_page = Blueprint('create', __name__, static_folder='../frontend/src', template_folder='../frontend/public')

@create_page.route('/create', methods=['GET','POST'])
def create():
    print("in create")
    if request.method == 'POST':
        print("in post")
        try:
            print(request.form)
            name = request.form['name']
            print(name)
            act_time = request.form['start_time']+":00"
            print(act_time)
            category = request.form['category']
            ## get category id from name
            ca_id = CatDA.get_category_by_name(category)[0]
            print(ca_id)
            esc_steps = request.form['esc_steps']
            temp_days = [request.form['0'], request.form['1'], request.form['2'], request.form['3'], request.form['4'], request.form['5'], request.form['6']]
            days: List[int] = []
            for i in range(0, len(temp_days)-1):
                if temp_days[i] == 'true':
                    days.append(i)
            if not days:
                days = [int(datetime.date.today().strftime("%Y%m%d"))]
            print(days)
            print(int(esc_steps))
            actDA.create_activity(name=name, start_time=act_time, esc_steps=int(esc_steps), ca_id=ca_id, days=days)
            return jsonify(success=True)
        except ValueError as e:
            return str(e), 400
        except Exception as e:
            return str(e), 500
    return jsonify(success=False)