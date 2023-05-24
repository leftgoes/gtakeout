from datetime import datetime
from dataclasses import dataclass
from typing import Self

BASIC_ACTIVITY: set[str] = {'calisthenics', 'sleep'}
DISTANCE_ACTIVITY: set[str] = {'biking'}
STEPS_ACTIVITY: set[str] = {'running', 'walking'}


@dataclass(order=True)
class BasicDatapoint:
    start: datetime
    end: datetime

@dataclass
class DistDatapoint(BasicDatapoint):
    distance: float

@dataclass
class StepsDatapoint(BasicDatapoint):
    distance: float
    steps: int