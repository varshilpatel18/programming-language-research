"""
db_manager.py
Handles DB connection, schema creation from CSV header, and CRUD operations.
Author: Varshil Patel
Student ID: 041142255
Course: CST8002

"""

import sqlite3
import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class DBManager:
    def __init__(self, db_path="project3.db"):
        self.db_path = db_path
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.conn.row_factory = sqlite3.Row
            logger.info("Connected to SQLite DB at %s", self.db_path)
        except Exception as e:
            logger.exception("DB connect failed: %s", e)
            raise

    def close(self):
        if self.conn:
            self.conn.close()
            logger.info("DB connection closed.")

    def create_table_from_header(self, table_name: str, header: List[str]):
        cols = ", ".join([f'"{col}" TEXT' for col in header])
        sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({cols});'
        try:
            self.conn.execute(sql)
            self.conn.commit()
            logger.info("Table %s ensured with cols: %s", table_name, header)
        except Exception:
            logger.exception("Failed creating table %s", table_name)
            raise

    def insert_record(self, table_name: str, record: Dict[str, Any]):
        keys = list(record.keys())
        placeholders = ", ".join("?" for _ in keys)
        cols = ", ".join(f'"{k}"' for k in keys)
        sql = f'INSERT INTO "{table_name}" ({cols}) VALUES ({placeholders})'
        try:
            self.conn.execute(sql, tuple(record[k] for k in keys))
            self.conn.commit()
        except Exception:
            logger.exception("Insert failed for record %s", record)
            raise

    def fetch_all(self, table_name: str):
        sql = f'SELECT * FROM "{table_name}"'
        cur = self.conn.execute(sql)
        rows = cur.fetchall()
        return rows

    def fetch_by_id(self, table_name: str, id_col: str, id_val: Any):
        sql = f'SELECT * FROM "{table_name}" WHERE "{id_col}" = ?'
        cur = self.conn.execute(sql, (id_val,))
        return cur.fetchone()

    def update_record(self, table_name: str, id_col: str, id_val: Any, updates: Dict[str, Any]):
        assignments = ", ".join(f'"{k}" = ?' for k in updates.keys())
        sql = f'UPDATE "{table_name}" SET {assignments} WHERE "{id_col}" = ?'
        try:
            self.conn.execute(sql, tuple(updates[k] for k in updates.keys()) + (id_val,))
            self.conn.commit()
        except Exception:
            logger.exception("Update failed for id %s", id_val)
            raise

    def delete_record(self, table_name: str, id_col: str, id_val: Any):
        sql = f'DELETE FROM "{table_name}" WHERE "{id_col}" = ?'
        try:
            self.conn.execute(sql, (id_val,))
            self.conn.commit()
        except Exception:
            logger.exception("Delete failed for id %s", id_val)
            raise
