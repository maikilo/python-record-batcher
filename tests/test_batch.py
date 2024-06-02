import unittest
from batches import Record, Batch
from utils import generate_random_sizes, generate_test_data

MB = 1024 ** 2


class BatchTest(unittest.TestCase):
    def test_too_many_records_in_batch_fails(self):
        sizes = [1] * (Batch.max_number_of_records + 1)
        text_data = generate_test_data(sizes)
        records = [Record(text) for text in text_data]
        with self.assertRaisesRegex(ValueError, f'Batch can contain at most 500 records'):
            Batch(records)

    def test_too_large_batch_size_fails(self):
        sizes = [MB] * 5 + [1]
        text_data = generate_test_data(sizes)
        records = [Record(text) for text in text_data]
        with self.assertRaisesRegex(ValueError, f'Batch size cannot exceed 5.0 MB'):
            Batch(records)

    def test_order_of_records_is_preserved_in_batch(self):
        sizes = generate_random_sizes(10, MB)
        test_data = generate_test_data(sizes)
        records = [Record(text, idx) for idx, text in enumerate(test_data)]
        record_indexes = [record.index for record in records]
        self.assertEqual(record_indexes, sorted(record_indexes))


if __name__ == '__main__':
    unittest.main()
