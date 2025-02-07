from typing import Callable, Dict, List
import DIL
import pandas as pd

from pseudonymizes.abc_pseudonymize import ABC_Pseudonymize


class Suppression(ABC_Pseudonymize):
    # def __init__(self, pseudonymizes: List[str], df: pd.DataFrame):
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.__table: Dict[str, Callable[[List[str]], None]] = {
            "일반삭제": self.general,
            "부분삭제": self.partial,
            "행 항목 삭제": self.record,
            "로컬삭제": self.local,
            "마스킹": self.masking,
            "주소": self.address
        }


    def run(self, pseudonymize: str, columns: List[str]) -> bool:
        if pseudonymize not in self.__table.keys():
            # print(f"[Debug] {pseudonymize}는 삭제기술이 아님")
            return False

        # 가명처리 적용
        self.__table[pseudonymize](columns)
        # print(f"[Debug] {pseudonymize} 적용 완료")
        return True


    def general(self, columns: List[str]) -> None:
        """
        일반삭제

        Args:
            columns (List[str]): 일반삭제를 적용할 컬럼 리스트
        """

        DIL.Suppression(self.df).general(columns)
    
    
    def partial(self, columns: List[str]) -> None:
        """
        부분삭제

        Args:
            columns (List[str]): 부분삭제를 적용할 컬럼 리스트
        """

        sup = DIL.Suppression(self.df)
        for column in columns:
            scope = Suppression.__get_scope(f"{column} 부분삭제")
            sup.partial(column, scope)

    def record(self, columns: List[str]) -> None:
        """
        행 항목 삭제

        Args:
            columns (List[str]): 행 항목 삭제를 적용할 컬럼 리스트
        """


    def local(self, columns: List[str]) -> None:
        """
        로컬삭제

        Args:
            columns (List[str]): 로컬삭제를 적용할 컬럼 리스트
        """


    def masking(self, columns: List[str]) -> None:
        """
        마스킹

        Args:
            columns (List[str]): 마스킹을 적용할 컬럼 리스트
        """

        sup = DIL.Suppression(self.df)
        for column in columns:
            scope = Suppression.__get_scope(f"{column} 마스킹")
            sup.masking(column, scope)            

    
    def address(self, columns: List[str]) -> None:
        """
        주소축소

        Args:
            column (str): 주소에 해당하는 컬럼
        """
        
        for column in columns:
            while True:
                try:
                    choice = int(input("주소축소 옵션을 선택하세요 (1: 시/도, 2: 시/군/구) > "))
                    if choice not in [1, 2]:
                        raise ValueError
                    
                    break

                except ValueError:
                    print("잘못된 입력입니다. 다시 입력해 주세요.")

            DIL.Suppression(self.df).address(column, choice) 


    @staticmethod
    def __get_scope(option: str) -> List[int]:
        while True:
            try:
                scope = input(f"{option} 범위 입력(예. 1, 5) > ")
                start, end = map(int, scope.split(", "))
                if (start < 0) or (end < 0) or (start >= end):
                    raise ValueError
                
                break

            except ValueError:
                print("잘못된 입력입니다. 다시 입력해 주세요.")

        return [start, end]
            