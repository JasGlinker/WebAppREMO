from flask import Blueprint
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
import datetime

day_page = Blueprint('dayView', __name__)
actDA = ActivitiesDataAccess()

@day_page.route('/dayView', methods=['GET'])
def dayView():
    today = datetime.date.today().weekday()
    activities = actDA.get_all_today(today)
