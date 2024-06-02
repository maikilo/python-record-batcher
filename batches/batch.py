from dataclasses import dataclass, field
from typing import ClassVar, List
from batches.record import Record

MB = 1024 ** 2


@dataclass
class Batch:
    """
    A batch of records stored in an array that has at most 500 records and a size of 5 MB.
    """
    records: List[Record]
    batch_size: int = field(init=False)
    number_of_records: int = field(init=False)
    max_batch_size: ClassVar[int] = 5 * MB
    max_number_of_records: ClassVar[int] = 500

    def __post_init__(self):
        self.batch_size = sum(record.size for record in self.records)
        self.number_of_records = len(self.records)
        if self.batch_size > self.__class__.max_batch_size:
            raise ValueError(f'Batch size cannot exceed {round(self.__class__.max_batch_size/MB, 1)} MB')
        if self.number_of_records > self.__class__.max_number_of_records:
            raise ValueError(f'Batch can contain at most {self.__class__.max_number_of_records} records')

    def __str__(self):
        return [str(record) for record in self.records]

    def __len__(self):
        return self.number_of_records
