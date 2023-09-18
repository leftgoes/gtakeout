import cv2
import json
import os

from ..cultureinfo import CultureInfo
from .seriescontainer import LocationSeriesContainer

class GLocation:
    def __init__(self, directory: str, cultureinfo: int = CultureInfo.DE) -> None:
        self.directory = directory
        self._cinfo = cultureinfo

        self.locdata = LocationSeriesContainer()
    
    def read(self) -> None:
        with open(os.path.join(self.directory, 'Records.json'), 'rb') as f:
            jdata = json.load(f)
        self.locdata.add_json(jdata)
    
    def heatmap(self) -> None:
        pass