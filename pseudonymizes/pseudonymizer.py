from typing import Dict, List, Tuple
import pandas as pd

from pseudonymizes.abc_pseudonymize import ABC_Pseudonymize
from pseudonymizes.suppression import Suppression
from pseudonymizes.generalization import Generalization


class Pseudonymizer:
    def __init__(self, df: pd.DataFrame, pseudonymize_dict: Dict[str, List[str]]):
        """
        가명처리 클래스

        Args:
            df (pandas.DataFrame): 원본 데이터
            pseudonymize_dict (Dict[str, List[str]]): 실제 적용할 가명처리 항목
        """

        self.df = df
        self.pseudonymize_dict = pseudonymize_dict # { 가명처리: [컬럼, ...] }

        # 가명처리 기술 클래스 생성
        self.__models: Tuple[ABC_Pseudonymize] = (
            Suppression(self.df),
            Generalization(self.df)
        )


    def run(self):
        for pseudonymize, columns in self.pseudonymize_dict.items():
            for model in self.__models:
                if model.run(pseudonymize, columns):
                    break
                