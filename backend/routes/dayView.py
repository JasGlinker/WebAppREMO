from xml.etree.ElementTree import tostring

from flask import Blueprint, request
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
import datetime as dt

day_page = Blueprint('dayView', __name__)
actDA = ActivitiesDataAccess()

@day_page.route('/dayView', methods=['GET'])
def dayView():

    today = dt.date.today().weekday()
    print(today)
    activities = actDA.get_all_today(today)
    tempdays = ""
    for activity in activities:
        # make days in string for json
        for day in activity['days']:
            tempdays = tempdays + str(day)
        activity['days'] = tempdays
        # parse time in string for json
        activity['start_time'] = (dt.datetime.min + activity['start_time']).time().strftime("%H:%M")
        print(activity['start_time'])
    print(activities)
    if request.method == 'GET':
        return activities
