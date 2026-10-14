import datetime

from flask import Blueprint, jsonify
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
from DataAccess.daysDataAccess import DaysDataAccess
import datetime as dt


week_page = Blueprint('weekView', __name__)
actDA = ActivitiesDataAccess()
daysDA = DaysDataAccess()

@week_page.route('/weekView', methods=['GET'])
def weekView():
    today = dt.date.today()

    ids = []
    for i in range(0, 7):
        temp_ids = daysDA.get_all_by_day(i)
        temp_dt = int((today + datetime.timedelta(days = (-today.weekday() + i))).strftime("%Y%m%d"))
        temp_ids.append(daysDA.get_all_by_day(temp_dt))
        print("week temp_ids", temp_ids)
        act_ids = []
        for temp_id in temp_ids:
            if temp_id:
                act_ids.append(temp_id['act_id'])
        ids.append(act_ids)

    activities = []
    for i in range(0, 7):
        activities.append([])
        for id in ids[i]:
            activities[i].append(actDA.get_by_id(id))

        for activity in activities[i]:
            activity['start_time'] = (dt.datetime.min + activity['start_time']).time().strftime("%H:%M")

    print("weekids:", ids)
    print("weekacts: ", activities)

    return jsonify(activities)


