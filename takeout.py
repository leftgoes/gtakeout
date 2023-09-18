import os

from . import cultureinfo as cinfo
from .cultureinfo import CultureInfo
from .fitness.gfit import GFit
from .location.glocation import GLocation

class Takeout:
    def __init__(self, directory: str, *, cultureinfo: int = CultureInfo.DE) -> None:
        self.directory = directory
        self.gfit: GFit | None = None
        self.glocation: GLocation | None = None

        self._cinfo = cultureinfo

    def read_googlefit(self) -> None:
        self.gfit = GFit(os.path.join(self.directory, cinfo.TAKEOUT[self._cinfo], cinfo.GOOGLE_FIT[self._cinfo]))
        self.gfit.read()
    
    def read_location_history(self) -> None:
        self.glocation = GLocation(os.path.join(self.directory, cinfo.TAKEOUT[self._cinfo], cinfo.LOCATION_HISTORY[self._cinfo]))
        self.glocation.read()