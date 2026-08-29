# Filename - App.py

# Import flask and datetime module for showing date and time
from flask import Flask, request, jsonify
from DataAccess.activitiesDataAccess import ActivitiesDataAccess as actDA
import datetime as dt
# Initializing flask app
app = Flask(__name__)
act = actDA()


@app.route('/create_activity', methods=['GET', 'POST'])
def create_activity():
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


# Running app
if __name__ == '__main__':
    app.run(debug=True)