"""
Programmer: Varshil Patel
File: record.py
Description: Record model representing one row of the bear/mammal dataset.
"""


class Record:
    """
    Represents a single dataset record.

    Columns (from CSV):
    - Site identification
    - Camera set date-time
    - Camera check date-time
    - Lure type
    - Species common name
    - Count of individuals
    - Observation date-time
    """

    def __init__(
        self,
        site_identification: int,
        camera_set_datetime: str,
        camera_check_datetime: str,
        lure_type: str,
        species_common_name: str,
        count_of_individuals: int,
        observation_datetime: str,
    ):
        # Convert numeric fields to int
        self.site_identification = int(site_identification)
        self.camera_set_datetime = camera_set_datetime
        self.camera_check_datetime = camera_check_datetime
        self.lure_type = lure_type
        self.species_common_name = species_common_name
        self.count_of_individuals = int(count_of_individuals)
        self.observation_datetime = observation_datetime

    def __str__(self) -> str:
        return (
            f"Site {self.site_identification} | "
            f"Set: {self.camera_set_datetime} | "
            f"Check: {self.camera_check_datetime} | "
            f"Lure: {self.lure_type} | "
            f"Species: {self.species_common_name} | "
            f"Count: {self.count_of_individuals} | "
            f"Observed: {self.observation_datetime}"
        )
