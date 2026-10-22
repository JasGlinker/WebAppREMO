from flask import Blueprint, jsonify
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
from DataAccess.daysDataAccess import DaysDataAccess
import datetime as dt
import logging
# Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

week_page = Blueprint('weekView', __name__)
actDA = ActivitiesDataAccess()
daysDA = DaysDataAccess()

@week_page.route('/weekView', methods=['GET'])
def weekView():
    logger.info('weekView accessed')
    today = dt.date.today()
    wdh_days = []
    ids = []
    activities = []
    for day in range(0, 7):
        activities.append([])
        wdh_days.append(daysDA.get_all_by_day(day))
        date = int((today + dt.timedelta(days=(-today.weekday() + day))).strftime("%Y%m%d"))
        ## get acts with corresponding date
        day_acts = daysDA.get_all_by_day(date)
        ## append with wdh acts
        if bool(wdh_days[day]) & bool(day_acts):
            day_acts = [day_acts + wdh_days[day]]
        elif wdh_days[day]:
            day_acts.append(wdh_days[day])
        elif day_acts:
            day_acts = [day_acts]

        if day_acts:
            ids.append(day_acts[0])
        else:
            ids.append([])

        for act_id in range(len(ids[day])):
            activities[day].append(actDA.get_by_id(ids[day][act_id]['act_id']))
            activities[day][act_id]['start_time'] = ((dt.datetime.min
                                                      + activities[day][act_id]['start_time'])
                                                     .time()
                                                     .strftime("%H:%M"))




    logger.debug('weekacts %s' % activities)

    return jsonify(activities)


