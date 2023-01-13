
from datetime import datetime, timedelta

class Bed:
    def __init__(self, name='', length=0, width=0, depth=0, sun='', drainage='', ffd='05/01/2023', pfd='07/20/2022', finfd='09/15/2023'):
        self.name = name
        self.length = length
        self.width = width
        self.depth = depth
        self.sun = sun
        self.drainage = drainage
        self.ffd = datetime.strptime(ffd, '%m/%d/%Y')
        self.pfd = datetime.strptime(pfd, '%m/%d/%Y')
        self.finfd = datetime.strptime(finfd, '%m/%d/%Y')
 
    def __str__(self):
        return f'Bed Name: {self.name}, Length: {self.length}, Width: {self.width}, Depth: {self.depth}, Sun: {self.sun}, Drainage: {self.drainage}, Ffd: {self.ffd.strftime("%m/%d/%Y")}, Pfd: {self.pfd.strftime("%m/%d/%Y")}, Finfd: {self.finfd.strftime("%m/%d/%Y")}'