import pandas as pd
from old.selector import Selector
from typing import List, Tuple, Callable

class Pseudonymizer:
    def __init__(self, dataframe: pd.DataFrame):
        self.dataframe = dataframe
        self.columns_dict: dict[str, List[Tuple[str, Callable]]] = {col: [] for col in self.dataframe.columns}

        Selector.run(self.dataframe.columns, self.columns_dict)

        for column, pseudo in self.columns_dict.items():
            for name, function in pseudo:
                print(f"{column} 컬럼에 {name} 가명처리 기법을 적용합니다.")
                function(self.dataframe, column)

        print(self.dataframe)


# 지금 순서
# csv 파일 업로드 > [가명처리 적용 컬럼 선택 > 가명처리 기법 선택] 반복 > 기법 선택 종료 후 적용을 위한 로직 실행(범위, 인덱스 등) > 적용

