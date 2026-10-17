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

    monthdates = []
    month_ids = []
    activities = []
    for week in range(len(temp_monthdates)):
        monthdates.append([])
        month_ids.append([])
        activities.append([])
        for day in range(0, 7):
            activities[week].append([])
            ## parse monthdates to int for db
            monthdates[week].append(int(temp_monthdates[week][day].strftime("%Y%m%d")))
            ## get acts with corresponding date
            day_acts = daysDA.get_all_by_day(monthdates[week][day])
            print("day_acts onetime:", day_acts)
            ## append with wdh acts
            if bool(wdh_days[day]) & bool(day_acts):
                day_acts = [day_acts + wdh_days[day]]
            elif wdh_days[day]:
                day_acts.append(wdh_days[day])
            elif day_acts:
                day_acts = [day_acts]

            print("day_acts together:", day_acts)
            if day_acts:
                month_ids[week].append(day_acts[0])
            else: month_ids[week].append([])
            ##month_ids[week].append(daysDA.get_all_by_day(day))
            ##print("month_id week day:", month_ids[week][day])
            ##print("month_ids week", month_ids[week])

            for id in range(len(month_ids[week][day])):
                if month_ids[week][day][id]:
                    activities[week][day].append(actDA.get_by_id(month_ids[week][day][id]['act_id']))
                    print("activities[week][day]: ", activities[week][day])
                    activities[week][day][id]['start_time'] = ((dt.datetime.min
                                                                + activities[week][day][id]['start_time'])
                                                               .time()
                                                               .strftime("%H:%M"))
                else:
                    activities[week][day].append([])
            print("activities[week]: ", activities[week])

    print("month activities:", activities)
    return jsonify(activities)