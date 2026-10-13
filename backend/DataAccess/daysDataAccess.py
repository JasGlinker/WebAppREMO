from typing import List

from DataAccess.DataAccess import DataAccess as DA

class DaysDataAccess:
    def __init__(self):
        self.days_data_access = DA(table_name="days")
    def get_all_by_day(self, weekday: int):
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
        for day in days:
            value = {'act_id': act_id, 'day_nmbr': day}
            self.days_data_access.create(value)

