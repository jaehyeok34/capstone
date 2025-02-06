import DIL
import pandas as pd
from typing import List


class Suppressions:
    # "general", "partial", "record", "sup_local", "masking", "address"
    @classmethod
    def __get_scope(cls) -> List[int]:
        while True:
            try:
                range_input = input("범위 입력(예시. 1 2) > ")
                range_list = list(map(int, range_input.split()))
                if (len(range_list) != 2) or (range_list[0] > range_list[1]):
                    raise ValueError()
                
                return range_list
                
            except ValueError:
                        print("올바른 범위를 입력해 주세요.")

    @classmethod
    def __get_index(cls) -> List[int]:
        while True:
            try:
                index_input = input("인덱스 입력(예시. 1, 2, 3) > ")
                index_list = list(map(int, index_input.split(', ')))
                if any(index < 0 for index in index_list):
                    raise ValueError()
            
                return index_list
            
            except ValueError:
                print("올바른 인덱스를 입력해 주세요.")

    @classmethod
    def general(dataframe: pd.DataFrame, column: str) -> bool:
        return DIL.Suppression(dataframe).general(column)
    

    @classmethod
    def partial(cls, dataframe: pd.DataFrame, column: str) -> bool:
        return DIL.Suppression(dataframe).partial(column, cls.__get_scope())
    

    @classmethod
    def record(cls, dataframe: pd.DataFrame, column: str) -> bool:
        return DIL.Suppression(dataframe).record(cls.__get_index())
    
    
    @classmethod
    def local(cls, dataframe: pd.DataFrame, column: str) -> bool:
        return DIL.Suppression(dataframe).local(column, cls.__get_index())
    

    @classmethod
    def masking(cls, dataframe: pd.DataFrame, column: str) -> bool:
        return DIL.Suppression(dataframe).masking(column, cls.__get_scope())
    

    @classmethod    
    def address(cls, dataframe: pd.DataFrame, column: str) -> bool:
        # 모드 선택
        while True:
            try:
                mode = int(input("1. 도 단위 / 2. 시 단위 (선택) > "))
                break 

            except ValueError:
                print("숫자를 입력해 주세요.")
                continue

        return DIL.Suppression(dataframe).address(column, mode)