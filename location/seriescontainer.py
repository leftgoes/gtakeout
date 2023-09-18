from .datapoint import LocationDatapoint

from ..series import Series


class LocationSeriesContainer:
    def __init__(self) -> None:
        self.locations = Series(LocationDatapoint)
    
    def add_json(self, json_data: dict) -> None:
        for location in json_data['locations']:
            locpoint = LocationDatapoint.from_json(location)
            self.locations.append(locpoint)
        self.locations.sort()