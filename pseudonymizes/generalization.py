from typing import Callable, Dict, List

import DIL
import pandas as pd

from pseudonymizes.abc_pseudonymize import ABC_Pseudonymize


class Generalization(ABC_Pseudonymize):
    def __init__(self, df: pd.DataFrame):
        self.df = df

        self.__table: Dict[str, Callable[[List[str]], None]] = {
            "랜덤 라운딩": self.random_rounding
        }

    
    def run(self, pseudonymize: str, columns: List[str]) -> bool:
        if pseudonymize not in self.__table.keys():
            # print(f"[Debug] {pseudonymize}는 범주화 기술이 아님")
            return False

        # 가명처리 적용
        self.__table[pseudonymize](columns)
        return True
        # print(f"[Debug] {pseudonymize} 적용 완료")


    # "랜덤 라운딩", "로컬 일반화", "문자데이터 범주화"
    def random_rounding(self, columns: List[str]) -> None:
        """
        랜덤 라운딩

        Args:
            columns (List[str]): 일반삭제를 적용할 컬럼 리스트
        """

        for column in columns:
            DIL.Rounding().random(self.df, column)