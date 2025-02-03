import pandas as pd
from selector import Selector
from typing import List, Tuple, Callable

class Pseudonymizer:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
        self.columns_dict: dict[str, List[Tuple[str, Callable]]] = {col: [] for col in self.dataframe.columns}

        Selector.run(self.dataframe.columns, self.columns_dict)
            