import datetime
from typing import List

from flask import Blueprint, request, jsonify
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
from DataAccess.categoriesDataAccess import CategoriesDataAccess

import logging
# Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')



actDA = ActivitiesDataAccess()
CatDA = CategoriesDataAccess()
create_page = Blueprint('create', __name__, static_folder='../frontend/src', template_folder='../frontend/public')

@create_page.route('/create', methods=['GET','POST'])
def create():
    logger.info("in create")
    if request.method == 'POST':
        logger.info("in create post")
        try:
            logger.debug("request formdata %s" %request.form)
            name = request.form['name']
            logger.debug("request form name %s" %name)
            act_time = request.form['start_time']+":00"
            logger.debug("request form parsed act_time %s" %act_time)
            category = request.form['category']
            ## get category id from name
            ca_id = CatDA.get_category_by_name(category)[0]
            logger.debug("ca_id from category name: %s" %ca_id)
            esc_steps = request.form['esc_steps']
            wdh = request.form['wdh']
            date = request.form['date']
            logger.debug("request form date: %s" %date)
            if wdh == "true":
                temp_days = [request.form['0'], request.form['1'], request.form['2'], request.form['3'], request.form['4'], request.form['5'], request.form['6']]
                days: List[int] = []
                for i in range(0, len(temp_days)):
                    if temp_days[i] == 'true':
                        days.append(i)
            elif date:
                days = [int(date.replace('-', ''))]
            else:
                days = [int(datetime.date.today().strftime("%Y%m%d"))]
            logger.debug("request form parsed days: %s" %days)
            logger.debug("request form parsed esc_steps: %s" %int(esc_steps))
            actDA.create_activity(name=name, start_time=act_time, esc_steps=int(esc_steps), ca_id=ca_id, days=days)
            return jsonify(success=True)
        except ValueError as e:
            return str(e), 400
        except Exception as e:
            return str(e), 500
    return jsonify(success=False)