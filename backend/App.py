from flask import Flask, request, jsonify
from routes.createActivity import create_page
from routes.dataAccess import data_page
from routes.dayView import day_page
from routes.weekView import week_page
from routes.monthView import month_page
# Initializing flask app
app = Flask(__name__)
app.register_blueprint(create_page)
app.register_blueprint(data_page)
app.register_blueprint(day_page)
app.register_blueprint(week_page)
app.register_blueprint(month_page)

# Running app
if __name__ == '__main__':
    app.run(debug=True)