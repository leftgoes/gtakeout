import os

from .gfit import GoogleFit

class Takeout:
    def __init__(self, directory: str) -> None:
        self.directory = directory
    
    def read_googlefit(self) -> GoogleFit:
        googlefit = GoogleFit(os.path.join(self.directory, 'Takeout', 'Google Fit'))
        googlefit.read()
        return googlefit