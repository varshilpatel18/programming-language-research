"""
Programmer: Varshil Patel
File: test_service.py
Description: Unit test for service layer (proof of concept).
"""

import unittest
from business import service
from model.record import Record


class TestService(unittest.TestCase):
    """
    Test cases for the business.service module.
    """

    def test_add_record_increases_length(self):
        """
        Reloads data, adds a new record, and verifies
        that the number of records increased by 1.
        """
        # Arrange
        service.reload_data()
        original_len = len(service.get_all_records())

        # Act
        rec = Record(
            site_identification=9999,
            camera_set_datetime="01/01/2016 10:00",
            camera_check_datetime="01/01/2016 11:00",
            lure_type="test lure",
            species_common_name="Test Species",
            count_of_individuals=1,
            observation_datetime="01/01/2016 10:30",
        )
        service.add_record(rec)
        new_len = len(service.get_all_records())

        # Assert
        self.assertEqual(original_len + 1, new_len)


if __name__ == "__main__":
    unittest.main()
