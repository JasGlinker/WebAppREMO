from flask import Blueprint, jsonify
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
from DataAccess.daysDataAccess import DaysDataAccess
import datetime as dt
import calendar as cal
import logging
# Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

month_page = Blueprint('monthView', __name__)
actDA = ActivitiesDataAccess()
daysDA = DaysDataAccess()
CAL = cal.Calendar()

@month_page.route('/month', methods=['GET'])
def month():
    logger.info('monthView accessed')
    today = dt.date.today()
    thisMonth = today.month
    thisYear = today.year
    temp_monthdates = CAL.monthdatescalendar(thisYear, thisMonth) ## this month dates parted in weeks
    ## cal.monthcalendar(thisYear, thisMonth) ## this month parted in weeks with numbered days
    wdh_days = []
    for i in range(0, 7):
        wdh_days.append(daysDA.get_all_by_day(i))

    logger.debug('wdh_days in monthView: %s' %wdh_days)

    monthdates = []
    month_ids = []
    activities = []
    for week in range(len(temp_monthdates)):
        monthdates.append([])
        month_ids.append([])
        activities.append({'date': temp_monthdates[week][0].strftime("%Y-%m-%d"), 'acts': []})
        for day in range(0, 7):
            activities[week]['acts'].append([])
            ## parse monthdates to int for db
            monthdates[week].append(int(temp_monthdates[week][day].strftime("%Y%m%d")))
            ## get acts with corresponding date
            day_acts = daysDA.get_all_by_day(monthdates[week][day])
            logger.debug("day_acts onetime in MonthView: %s" %day_acts)
            ## append with wdh acts
            if bool(wdh_days[day]) & bool(day_acts):
                day_acts = [day_acts + wdh_days[day]]
            elif wdh_days[day]:
                day_acts.append(wdh_days[day])
            elif day_acts:
                day_acts = [day_acts]

            logger.debug("day_acts together in MonthView: %s" %day_acts)

            if day_acts:
                month_ids[week].append(day_acts[0])
            else: month_ids[week].append([])

            for id in range(len(month_ids[week][day])):
                if month_ids[week][day][id]:
                    activities[week]['acts'][day].append(actDA.get_by_id(month_ids[week][day][id]['act_id']))
                    logger.debug("activities[week][day] in MonthView: %s" %activities[week]['acts'][day])
                    activities[week]['acts'][day][id]['start_time'] = ((dt.datetime.min
                                                                + activities[week]['acts'][day][id]['start_time'])
                                                               .time()
                                                               .strftime("%H:%M"))
                else:
                    activities[week]['acts'][day].append([])
            logger.debug("activities[week] in MonthView: %s" %activities[week])

    logger.debug('month activities: %s' %activities)
    return jsonify(activities)