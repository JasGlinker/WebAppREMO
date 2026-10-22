from typing import List

from DataAccess.DataAccess import DataAccess as DA
import logging
# Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DaysDataAccess:
    def __init__(self):
        self.days_data_access = DA(table_name="days")
        logger.info("DaysDataAccess initiated")
    def get_all_by_day(self, weekday: int):
        logger.info("DaysDataAccess.get_all_by_day: %s", weekday)
        conn = self.days_data_access._get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT act_id FROM days WHERE day_nmbr LIKE %s"
        try:
            cursor.execute(query, (weekday,))
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def create_act_days(self, act_id: int, days: List[int]):
        logger.info("DaysDataAccess.create_act_days: act_id: %s, days: %s",act_id, days)
        for day in days:
            value = {'act_id': act_id, 'day_nmbr': day}
            self.days_data_access.create(value)

