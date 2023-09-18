from dateutil.parser import parse as parse_datetime
from datetime import datetime
from dataclasses import dataclass
from typing import Self


@dataclass(order=True)
class LocationDatapoint:
    time: datetime
    lat: float
    lon: float

    @classmethod
    def from_json(cls, loc_json) -> Self:
        return cls(parse_datetime(loc_json['timestamp']),
                                  loc_json['latitudeE7'] / 1e7,
                                  loc_json['longitudeE7'] / 1e7)
