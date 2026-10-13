from typing import List

from DataAccess.DataAccess import DataAccess as DA
from DataAccess.daysDataAccess import DaysDataAccess

DaysDA = DaysDataAccess()
class ActivitiesDataAccess:
    def __init__(self):
        self.activity_data_access = DA(table_name='activities')
    def get_by_name(self, name: str):
        conn = self.activity_data_access._get_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM activities WHERE name = %s"

        try:
            cursor.execute(query, (name,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def get_by_id(self, id: int):
        conn = self.activity_data_access._get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM activities WHERE act_id = %s"
        try:
            cursor.execute(query, (id,))
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def create_activity(self, name: str, start_time: str, esc_steps: int, ca_id: int, days: List[int]):
        print("in DA create activity")
        value = {
            'act_name': name,
            'start_time': start_time,
            'esc_steps': esc_steps,
            'category': ca_id
        }
        act_id = self.activity_data_access.create(value)
        DaysDA.create_act_days(act_id, days)

