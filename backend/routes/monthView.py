from flask import Blueprint, jsonify
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
from DataAccess.daysDataAccess import DaysDataAccess
import datetime as dt
import calendar as cal

month_page = Blueprint('monthView', __name__)
actDA = ActivitiesDataAccess()
daysDA = DaysDataAccess()
CAL = cal.Calendar()

@month_page.route('/month', methods=['GET'])
def month():
    today = dt.date.today()
    thisMonth = today.month
    thisYear = today.year
    temp_monthdates = CAL.monthdatescalendar(thisYear, thisMonth) ## this month dates parted in weeks
    ## cal.monthcalendar(thisYear, thisMonth) ## this month parted in weeks with numbered days
    wdh_days = []
    for i in range(0, 7):
        wdh_days.append(daysDA.get_all_by_day(i))

    ## parse monthdates to int for db
    monthdates = []
    month_ids = []
    activities = []
    for week in range(len(temp_monthdates)):
        monthdates.append([])
        month_ids.append([])
        activities.append([])
        for day in range(len(temp_monthdates[week])):
            activities[week].append([])
            day_nmbr = day % 7
            monthdates[week].append(int(temp_monthdates[week][day].strftime("%Y%m%d")))
            month_ids[week].append(daysDA.get_all_by_day(monthdates[week][day]))
            month_ids[week].append(daysDA.get_all_by_day(day_nmbr))
            print("month_ids", month_ids[week])
            print(month_ids[week][day])
            if month_ids[week][day]:
                for id in range(len(month_ids[week][day])):
                    activities[week][day].append(actDA.get_by_id(month_ids[week][day][id]['act_id']))
                    activities[week][day][id]['start_time'] = (dt.datetime.min + activities[week][day][id]['start_time']).time().strftime("%H:%M")

    print("month activities:", activities)
    return jsonify(activities)