from __future__ import annotations
import numpy as np
import csv
from dataclasses import dataclass


@dataclass
class StrainData:
    x: np.typing.NDArray[np.float64]
    values: np.typing.NDArray[np.float64]
    name: str | None = None

    @classmethod
    def from_csv(cls, reader: csv.DictReader) -> StrainData:
        x = []
        values = []
        for row in reader:
            x.append(float(row["x"]))
            values.append(float(row["strain"]))
        return cls(x=np.array(x), values=np.array(values))
