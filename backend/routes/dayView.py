from flask import Blueprint, request
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
from DataAccess.daysDataAccess import DaysDataAccess
import datetime as dt

day_page = Blueprint('dayView', __name__)
actDA = ActivitiesDataAccess()
daysDA = DaysDataAccess()

@day_page.route('/dayView', methods=['GET'])
def dayView():

    today_wd = dt.date.today().weekday()
    print(today_wd)
    today = int(dt.datetime.today().strftime("%Y%m%d"))
    temp_act_ids = daysDA.get_all_by_day(today_wd)
    temp_act_ids.append(daysDA.get_all_by_day(today))
    print("temp_ids", temp_act_ids)
    act_ids = []
    for temp_id in temp_act_ids:
        if temp_id:
            act_ids.append(temp_id['act_id'])
    print("act_ids:", act_ids)

    activities = []
    for act_id in act_ids:
        activities.append(actDA.get_by_id(act_id))

    print("activities: ",activities)

    for activity in activities:
        # parse time in string for json
        activity['start_time'] = (dt.datetime.min + activity['start_time']).time().strftime("%H:%M")
        print(activity['start_time'])
    print(activities)
    if request.method == 'GET':
        return activities
