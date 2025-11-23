import os
import unittest
from db_manager import DBManager
from visualizer import create_pie_chart_from_rows

class DBVisualTest(unittest.TestCase):
    DB_PATH = "test_project3.db"
    TABLE = "test_table"

    def setUp(self):
        self.db = DBManager(self.DB_PATH)
        self.db.connect()
        header = ["Category", "Value"]
        self.db.create_table_from_header(self.TABLE, header)
        self.db.insert_record(self.TABLE, {"Category": "A", "Value": "10"})
        self.db.insert_record(self.TABLE, {"Category": "B", "Value": "20"})
        self.db.insert_record(self.TABLE, {"Category": "A", "Value": "5"})

    def tearDown(self):
        self.db.close()
        if os.path.exists(self.DB_PATH):
            os.remove(self.DB_PATH)
        if os.path.exists("test_pie.png"):
            os.remove("test_pie.png")

    def test_pie_chart_created_and_db_rows_correct_count(self):
        rows = self.db.fetch_all(self.TABLE)
        self.assertEqual(len(rows), 3)
        path = create_pie_chart_from_rows(rows, "Category", output_path="test_pie.png")
        self.assertTrue(os.path.exists(path))

if __name__ == "__main__":
    unittest.main()
