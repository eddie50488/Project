import pandas as pd


class Point:

    def __init__(self, row: pd.Series):
        self._index = int(row.iloc[0])
        self._quality = row.iloc[1]
        self._theta = row.iloc[2]
        self._distance = row.iloc[3]
        
    @property 
    def index(self):
        return self._index
    
    @index.setter
    def index(self, index):
        self._index = index
    

