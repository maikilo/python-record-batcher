from functools import reduce
import unittest
from batches import Record, BatchGenerator
from utils import generate_test_data


class BatchGeneratorTest(unittest.TestCase):
    def test_order_of_records_in_batches(self):
        # Create records of set sizes, some of which are above the allowed record size
        sizes = [640090, 203344, 610234, 391603, 522468, 120141, 944229, 769660, 767049, 958785,
                 Record.max_record_size + 5, Record.max_record_size + 10,
                 349660, 736045, 128300, 881606, 621108, 381280, 794228, 612287, 733143, 1039295,
                 Record.max_record_size + 1, Record.max_record_size + 2,
                 496889, 1014280, 178484, 609908, 75718, 111373, 279367, 420249, 9173, 618049, 566]
        records = generate_test_data(sizes)

        # Split records into batches - this will create four batches
        generator = BatchGenerator()
        generator.set_records(records)
        generator.create_batches()

        # Retrieve order of records in batches
        batches = generator.batches
        indexes_by_batch = [[record.index for record in batch.records] for batch in batches]
        record_indexes = reduce(lambda x, y: x + y, indexes_by_batch)
        self.assertEqual(record_indexes, sorted(record_indexes))


if __name__ == '__main__':
    unittest.main()
