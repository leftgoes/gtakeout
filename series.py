from dateutil.parser import parse as parse_datetime

from .datapoint import BasicDatapoint, StepsDatapoint, DistDatapoint
from .datapoint import BASIC_ACTIVITY, DISTANCE_ACTIVITY, STEPS_ACTIVITY


class Series(list):
    def __init__(self, dtype: type) -> None:
        self.dtype = dtype
        return super().__init__()

    def append(self, datapoint) -> None:
        if not isinstance(datapoint, self.dtype):
            raise TypeError(f'datapoint must be type {self.dtype!r}, not {type(datapoint)!r}')
        super().append(datapoint)


class SeriesContainer:
    def __init__(self) -> None:
        self.sleep = Series(BasicDatapoint)
        self.walking = Series(StepsDatapoint)
        self.biking = Series(DistDatapoint)
        self.running = Series(StepsDatapoint)
        self.calisthenics = Series(BasicDatapoint)

    def __repr__(self) -> str:
        return f'SeriesContainer(n_sleep={len(self.sleep)}, n_walking={len(self.walking)}, n_biking={len(self.biking)}, n_running={len(self.running)}, n_calisthenics={len(self.calisthenics)})'

    def append(self, json_data: dict) -> None:
        if json_data['fitnessActivity'] in BASIC_ACTIVITY:
            dpoint = self.parse_basic(json_data)
        elif json_data['fitnessActivity'] in DISTANCE_ACTIVITY:
            dpoint = self.parse_distance(json_data)
        elif json_data['fitnessActivity'] in STEPS_ACTIVITY:
            dpoint = self.parse_steps(json_data)

        if dpoint:
            self.__getattribute__(json_data['fitnessActivity']).append(dpoint)
    
    def sort_all(self) -> None:
        self.sleep.sort()
        self.walking.sort()
        self.biking.sort()
        self.running.sort()
        self.calisthenics.sort()

    def parse_basic(self, json_data: dict) -> BasicDatapoint:
        return BasicDatapoint(parse_datetime(json_data['startTime']),
                              parse_datetime(json_data['endTime']))
    
    def parse_distance(self, json_data: dict) -> DistDatapoint | None:
        for elem in json_data['aggregate']:
            if elem['metricName'] == 'com.google.distance.delta':
                distance: float = elem['floatValue']
                return DistDatapoint(parse_datetime(json_data['startTime']),
                                     parse_datetime(json_data['endTime']),
                                     distance)

    def parse_steps(self, json_data: dict) -> StepsDatapoint:
        for elem in json_data['aggregate']:
            if elem['metricName'] == 'com.google.step_count.delta':
                stepspoint: int = elem['intValue']
            elif elem['metricName'] == 'com.google.distance.delta':
                distance: float = elem['floatValue']
        
        return StepsDatapoint(parse_datetime(json_data['startTime']),
                              parse_datetime(json_data['endTime']),
                              distance,
                              stepspoint)
