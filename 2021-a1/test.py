import a1
import unittest

class Test(unittest.TestCase):
    def test_get_hours(self):
        time = 3800
        expected = 1
        result = a1.get_hours(time)
        self.assertEqual(expected, result)

    def test_get_minutes(self):
        time = 5789
        expected = 36
        result = a1.get_minutes(time)
        self.assertEqual(expected, result)

    def test_get_seconds(self):
        time = 60
        expected = 0
        result = a1.get_seconds(time)
        self.assertEqual(expected, result)
    
    def test_time_to_utc(self):
        utc_offset = +1
        time = 24.0
        expected = 23.0
        result = a1.time_to_utc(utc_offset, time)
        self.assertEqual(expected, result)

    def test_time_from_utc(self):
        utc_offset = +1
        time = 24.0
        expected = 1.0
        result = a1.time_from_utc(utc_offset, time)
        self.assertEqual(expected, result)

unittest.main()