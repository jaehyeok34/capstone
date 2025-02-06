from typing import Dict
import pandas as pd


class Pseudonymizer:
    def __init__(self, df: pd.DataFrame, pseudonymize_dict: Dict[str, str]):
        self.df = df
        self.pseudonymize_dict = pseudonymize_dict # 컬럼에 적용할 가명처리 기술

    def run(self):
        # self.pseudonymize_dict에 있는 가명처리 기술명을 기반으로...
        
        pass