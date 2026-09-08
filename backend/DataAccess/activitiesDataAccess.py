from typing import List

from DataAccess.DataAccess import DataAccess as DA


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

    def get_all_today(self, weekday: int):
        conn = self.activity_data_access._get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM activities WHERE days LIKE %s"
        try:
            cursor.execute(query, (weekday,))
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()


    def create_activity(self, name: str, start_time: str, days: str, esc_steps: int, ca_id: int):
        print("in DA create activity")
        value = {
            'act_name': name,
            'start_time': start_time,
            'days': days,
            'esc_steps': esc_steps,
            'category': ca_id
        }
        return self.activity_data_access.create(value)