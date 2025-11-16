"""
Programmer: Varshil Patel
File: repository.py
Description: Handles File I/O for loading and saving dataset records.
"""

import csv
import uuid
from pathlib import Path
from model.record import Record

# Path to your dataset file (in the data/ folder)
DATA_FILE = Path("data/dataset.csv")


def load_records(max_records: int = 100) -> list[Record]:
    """
    Loads up to max_records records from the CSV dataset.
    Uses try/except to handle missing file errors.
    Uses latin1 encoding to safely handle special characters.
    """
    records: list[Record] = []

    try:
        with DATA_FILE.open("r", encoding="latin1", newline="") as f:
            reader = csv.reader(f)

            # Skip header row (column names)
            header = next(reader, None)

            for i, row in enumerate(reader):
                if i >= max_records:
                    break

                # Expecting 7 columns based on the dataset
                if len(row) < 7:
                    continue

                site_identification = row[0]
                camera_set_datetime = row[1]
                camera_check_datetime = row[2]
                lure_type = row[3]
                species_common_name = row[4]
                count_of_individuals = row[5]
                observation_datetime = row[6]

                try:
                    rec = Record(
                        site_identification,
                        camera_set_datetime,
                        camera_check_datetime,
                        lure_type,
                        species_common_name,
                        count_of_individuals,
                        observation_datetime,
                    )
                    records.append(rec)
                except ValueError:
                    # If conversion to int fails (bad data), skip that row
                    continue

    except FileNotFoundError:
        print(f"ERROR: Dataset file {DATA_FILE} not found.")

    return records


def save_records(records: list[Record]) -> Path:
    """
    Saves the current list of records to a CSV file using a UUID filename.
    Demonstrates use of the uuid API.
    """
    output_name = f"output_{uuid.uuid4()}.csv"
    output_path = Path("data") / output_name

    with output_path.open("w", newline="", encoding="latin1") as f:
        writer = csv.writer(f)

        # Write header row that matches the dataset
        writer.writerow([
            "Site identification",
            "Camera set date-time",
            "Camera check date-time",
            "Lure type",
            "Species common name",
            "Count of individuals",
            "Observation date-time",
        ])

        # Write each record
        for r in records:
            writer.writerow([
                r.site_identification,
                r.camera_set_datetime,
                r.camera_check_datetime,
                r.lure_type,
                r.species_common_name,
                r.count_of_individuals,
                r.observation_datetime,
            ])

    return output_path
