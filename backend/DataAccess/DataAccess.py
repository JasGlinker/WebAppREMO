import mysql.connector
from typing import Dict, List, Any
import json
import logging
# Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataAccess:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self._load_config()
        logger.info("DataAccess initialized")

    def _load_config(self) -> None:
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.db_config = config['database']
        logger.info("DataAccess config read")

    def _get_connection(self) -> mysql.connector.connection.MySQLConnection:
        logger.debug("In DataAccess to get connection")
        return mysql.connector.connect(
            host=self.db_config['host'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            database=self.db_config['database']
        )

    #CRUD operations
    def create(self, data: Dict[str, Any]) -> int:
        logger.debug("In DataAccess.create: data: %s", data)
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
        logger.debug("In DataAccess.read: id: %s", id)
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

    def read_all(self) -> Dict[str, Any]:
        logger.debug("In DataAccess.read_all")
        conn = self._get_connection()
        cursor = conn.cursor(dictionary=True)

        query = f"SELECT * FROM {self.table_name}"
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()
            conn.close()

    def update(self, id: int, data: Dict[str, Any]) -> bool:
        logger.debug("In DataAccess.update: id: %s data: %s", id, data)
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
        logger.debug("In DataAccess.delete: id: %s", id)
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


