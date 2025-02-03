import pandas as pd
from selector import Selector

class Pseudonymizer:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
        self.columns_dict = {col: [] for col in self.dataframe.columns}

        Selector.run(self.dataframe.columns, self.columns_dict)
