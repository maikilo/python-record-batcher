from dataclasses import dataclass, field
from typing import ClassVar, Optional

MB = 1024 ** 2


@dataclass
class Record:
    """
    Represents a record which is a string with a max size of 1 MB and an optional index attribute
    to track the order of records.
    """
    record: str
    index: Optional[int] = field(default=None)
    size: int = field(init=False)
    max_record_size: ClassVar[int] = MB

    def __post_init__(self):
        self.size = len(self.record.encode('utf-8'))
        if self.size > Record.max_record_size:
            raise ValueError(f'Record size cannot exceed {round(Record.max_record_size/MB, 1)} MB')

    def __str__(self):
        return self.record

    def __len__(self):
        return self.size
