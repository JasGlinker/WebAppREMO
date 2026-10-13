from flask import Blueprint
from DataAccess.activitiesDataAccess import ActivitiesDataAccess
import datetime as dt

week_page = Blueprint('weekView', __name__)
ActDA = ActivitiesDataAccess()

@week_page.route('/weekView')
def weekView():



