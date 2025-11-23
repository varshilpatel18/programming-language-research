"""
data_loader.py
Load CSV dataset and populate DB using DBManager.
"""

import csv
import logging
from db_manager import DBManager

logger = logging.getLogger(__name__)

def load_csv_to_db(csv_path: str, db: DBManager, table_name: str):
    try:
        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            db.create_table_from_header(table_name, header)
            for row in reader:
                row = row[:len(header)] + ['']*(max(0, len(header)-len(row)))
                record = {header[i]: row[i] for i in range(len(header))}
                db.insert_record(table_name, record)
        logger.info("CSV loaded into DB from %s", csv_path)
    except FileNotFoundError:
        logger.exception("CSV file not found: %s", csv_path)
        raise
    except Exception:
        logger.exception("Failed to load CSV to DB.")
        raise
