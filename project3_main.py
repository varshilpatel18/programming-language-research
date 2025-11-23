"""
project3_main.py
Practical Project Part 3 main entry point
Author: Varshil Patel
"""

import logging
from db_manager import DBManager
from data_loader import load_csv_to_db
from visualizer import create_pie_chart_from_rows
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

FULL_NAME = "Varshil Patel"
DB_PATH = "project3.db"
TABLE_NAME = "dataset_table"
CSV_PATH = "dataset.csv"

def print_header():
    print("="*80)
    print(f"Practical Project Part 3 — {FULL_NAME}")
    print("="*80)

def run():
    db = DBManager(DB_PATH)
    try:
        db.connect()
        while True:
            print_header()
            print("1) Reload data from CSV into DB (append)")
            print("2) Display all records")
            print("3) Visualize (pie chart by column)")
            print("4) Exit")
            choice = input("Enter choice: ").strip()
            if choice == "1":
                csv_path = input(f"CSV path (default: {CSV_PATH}): ").strip() or CSV_PATH
                if not os.path.exists(csv_path):
                    print("CSV not found at", csv_path)
                    input("Press Enter to continue...")
                    continue
                load_csv_to_db(csv_path, db, TABLE_NAME)
                print("Reload complete.")
                input("Press Enter to continue...")
            elif choice == "2":
                rows = db.fetch_all(TABLE_NAME)
                for r in rows:
                    print(dict(r))
                input("Press Enter to continue...")
            elif choice == "3":
                col = input("Enter categorical column for pie chart: ")
                rows = db.fetch_all(TABLE_NAME)
                if not rows:
                    print("No rows found. Load CSV first.")
                else:
                    path = create_pie_chart_from_rows(rows, col, output_path="piechart.png", title=f"{col} distribution")
                    print(f"Pie chart saved: {path}")
                input("Press Enter to continue...")
            elif choice == "4":
                break
            else:
                print("Invalid choice.")
    finally:
        db.close()
        print("Exiting.")

if __name__ == "__main__":
    run()
