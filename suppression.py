from typing import List
import DIL
import pandas as pd


class Suppression:
    def __init__(self, df: pd.DataFrame):
        self.df = df


    def general(self, columns: List[str]) -> bool:
        """
        일반삭제

        Args:
            columns (List[str]): 일반삭제를 적용할 컬럼명 리스트

        Returns:
            bool: 성공 시 true, 실패 시 false
        """

        return DIL.Suppression(self.df).general(columns)
    
    
    def partial(self, columns: List[str]) -> bool:
        """
        부분삭제

        Args:
            columns (List[str]): 부분삭제를 적용할 컬럼명 리스트

        Returns:
            bool: 성공 시 true, 실패 시 false
        """

        sup = DIL.Suppression(self.df)
        for column in columns:
            while True:
                try:
                    scope = input(f"{column} 부분삭제 범위 입력(예. 1, 2) > ")

                    start, end = map(int, scope.split(", "))
                    if (start < 0) or (end < 0) or (start >= end):
                        raise ValueError
                    
                    break

                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해 주세요.")