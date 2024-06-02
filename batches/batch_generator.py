from typing import List
from batches.record import Record
from batches.batch import Batch

MB = 1024 ** 2


class BatchGenerator:
    """
    Creates records from a list of string inputs and splits them into batches.
    """
    def __init__(self):
        self.records: List[Record] = []
        self.batches: List[Batch] = []

    def set_records(self, inputs: List[str]):
        self.records = [Record(text, idx) for idx, text in enumerate(inputs)
                        if len(text.encode('utf-8')) <= Record.max_record_size]

    def create_batches(self):
        current_batch = []
        current_batch_size = 0
        for record in self.records:
            if (current_batch_size + record.size > Batch.max_batch_size) or (
                    len(current_batch) > Batch.max_number_of_records):
                self.batches.append(Batch(current_batch))
                current_batch = []
                current_batch_size = 0
            current_batch.append(record)
            current_batch_size += record.size
        if len(current_batch) > 0:
            self.batches.append(Batch(current_batch))
