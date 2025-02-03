import tkinter
from tkinter import filedialog
import DIL
import DIL.statistics as Statistics
import pandas as pd


class Pseudonymizer:
    def __init__(self):
        self.df = self.__get_csv()
        self.suppression = DIL.Suppression(self.df)
        self.rounding = DIL.Rounding()
        self.generalization = DIL.Generalization(self.df)
        self.aggregation = Statistics.Aggregation(self.df)
        self.microAggregation = Statistics.MicroAggregation(self.df)

        self.pseudo_dict = {
            "Suppression": {
                "general": self.suppression.general,
                "partial": self.__suppression_partial,
                "record": self.__suppression_record
            }
        }

    def __suppression_record(self, column: str) -> None:
        # 레코드 삭제를 위한 특정 값을 입력 받음
        print("Enter a value to delete: ", end="")
        user_input = input()

        self.suppression.record(column, user_input)

    def __suppression_partial(self, column: str) -> None:
        # 두 개의 정수(범위) 입력 받음
        print("Enter two integers separated by space (e.g., 1 2): ", end="")
        user_input = input().split()
        if len(user_input) != 2:
            raise ValueError("You must enter exactly two integers.")
        start, end = map(int, user_input)
        scope = (start, end)

        self.suppression.partial(column, scope)

    def __get_csv(self) -> pd.DataFrame:
        # GUI를 통해 CSV 파일을 선택할 수 있는 Dialog 창 띄우기
        root = tkinter.Tk()
        root.withdraw()  # Tkinter 창을 숨김

        file_path = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )

        if not file_path: # 해당 조건이 만족하면, 실패 아니면 성공
            raise ValueError("No file selected")

        # 파일 로드 성공
        return pd.read_csv(file_path)


    def select_column(self) -> None:
        # 컬럼 목록 출력
        columns_dict = {}
        columns_str_list = []
        for i, col in enumerate(self.df.columns):
            columns_dict[i+1] = col
            columns_str_list.append(f"{i+1}. {col}")

        columns_str = ", ".join(columns_str_list)
        print("Columns:", columns_str)
        print("select(ex: 1) > ", end="")

        # 사용자 입력을 받아 선택된 컬럼 출력
        selected_column = int(input())
        print(columns_dict[selected_column]) 
        print(self.df[columns_dict[selected_column]])

    