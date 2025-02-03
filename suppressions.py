import DIL
import pandas as pd



class Suppressions:
    # "general", "partial", "record", "sup_local", "masking", "address"
    @classmethod
    def __get_scope(cls) -> list:
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
    def __get_index(cls) -> int:
        while True:
            try:
                index = int(input("인덱스 입력 > "))
                if index < 0:
                    raise ValueError()
                
                return index
                
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
