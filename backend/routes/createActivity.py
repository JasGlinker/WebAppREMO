from flask import Blueprint, render_template, request, jsonify
from DataAccess.activitiesDataAccess import ActivitiesDataAccess


actDA = ActivitiesDataAccess()
create_page = Blueprint('create', __name__)

@create_page.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        try:
            name = request.form['name']
            days = request.form['days']
            category = request.form['category']
            act_time = request.form['act_time']
            esc_steps = request.form['esc_steps']

            actDA.create_activity(name, act_time, days, esc_steps, category)
            return jsonify(success=True)
        except ValueError as e:
            return str(e), 400
        except Exception as e:
            return str(e), 500
    return jsonify(success=False)