import json
import os

from . import cultureinfo
from .cultureinfo import CultureInfo
from .series import SeriesContainer

class GoogleFit:
    def __init__(self, directory: str, cultureinfo: int = CultureInfo.DE) -> None:
        self.directory = directory
        self._cinfo = cultureinfo

        self.data = SeriesContainer()

    @property
    def all_sessions_dir(self) -> str:
        return os.path.join(self.directory, cultureinfo.ALL_SESSIONS[self._cinfo])

    def read(self) -> None:
        for filename in os.listdir(self.all_sessions_dir):
            with open(os.path.join(self.all_sessions_dir, filename), 'rb') as f:
                jdata = json.load(f)
            self.data.append(jdata)
        self.data.sort_all()
        print(self.data)
        print(min(self.data.sleep), max(self.data.sleep))

