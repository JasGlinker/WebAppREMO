import mysql.connector
from typing import Dict, List, Any
import json

class DataAccess:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self._load_config()

    def _load_config(self) -> None:
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.db_config = config['database']

    def _get_connection(self) -> mysql.connector.connection.MySQLConnection:
        return mysql.connector.connect(
            host=self.db_config['host'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            database=self.db_config['database']
        )

    #CRUD operations
    def create(self, data: Dict[str, Any]) -> int:
        conn = self._get_connection()
        cursor = conn.cursor()

        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"

        try:
            cursor.execute(query, list(data.values()))
            conn.commit()
            last_id = cursor.lastrowid
            return last_id
        finally:
            cursor.close()
            conn.close()

    def read(self, id: int) -> Dict[str, Any]:
        conn = self._get_connection()
        cursor = conn.cursor(dictionary=True)

        query = f"SELECT * FROM {self.table_name} WHERE id = %s"

        try:
            cursor.execute(query, (id,))
            result = cursor.fetchone()
            return result
        finally:
            cursor.close()
            conn.close()

    def update(self, id: int, data: Dict[str, Any]) -> bool:
        conn = self._get_connection()
        cursor = conn.cursor()

        set_clause = ', '.join([f"{k} = %s" for k in data.keys()])
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = %s"

        try:
            cursor.execute(query, list(data.values()) + [id])
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()

    def delete(self, id: int) -> bool:
        conn = self._get_connection()
        cursor = conn.cursor()

        query = f"DELETE FROM {self.table_name} WHERE id = %s"

        try:
            cursor.execute(query, (id,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()


