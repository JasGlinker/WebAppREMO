from flask import Blueprint, request
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
from DataAccess.daysDataAccess import DaysDataAccess
import datetime as dt
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
day_page = Blueprint('dayView', __name__)
actDA = ActivitiesDataAccess()
daysDA = DaysDataAccess()

@day_page.route('/dayView', methods=['GET'])
def dayView():
    logger.info('dayView accessed')

    today_wd = dt.date.today().weekday()
    today = int(dt.datetime.today().strftime("%Y%m%d"))
    wdh_act_ids = daysDA.get_all_by_day(today_wd)
    logger.debug("wdh_act_ids in get dayview %s" %wdh_act_ids)
    act_ids = daysDA.get_all_by_day(today)

    if bool(wdh_act_ids) & bool(act_ids):
        act_ids = [act_ids + wdh_act_ids]
    elif wdh_act_ids:
        act_ids.append(wdh_act_ids)
    elif act_ids:
        act_ids = [act_ids]


    logger.debug(msg="act_ids in get dayview: %s" %act_ids)


    activities = []
    if act_ids:
        for act_id in act_ids[0]:
            activities.append(actDA.get_by_id(act_id['act_id']))

    logger.debug("activities in dayView before parse: %s" %activities)

    for activity in activities:
        # parse time in string for json
        activity['start_time'] = ((dt.datetime.min
                                  + activity['start_time'])
                                  .time()
                                  .strftime("%H:%M"))
        logger.debug('activity start time: %s' %activity['start_time'])

    logger.debug("activities from dayView: %s" %activities)
    if request.method == 'GET':
        return activities
