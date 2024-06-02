import random
import string
import unittest
from batches import Record


class TestRecord(unittest.TestCase):
    def test_valid_record_content(self):
        record_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(100))
        record = Record(record_str)
        self.assertEqual(str(record), record_str)

    def test_invalid_record(self):
        length = Record.max_record_size + 1
        record_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        with self.assertRaises(ValueError):
            Record(record_str)

    def test_records_with_same_content_but_different_index_are_not_equal(self):
        record_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        self.assertNotEqual(Record(record_str, 1), Record(record_str, 2))

    def test_records_with_same_content_and_no_index_are_equal(self):
        record_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))
        self.assertEqual(Record(record_str), Record(record_str))


if __name__ == '__main__':
    unittest.main()
