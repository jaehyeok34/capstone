import tkinter
from tkinter import filedialog
import pandas as pd


class CSV_Loader:
    @staticmethod
    def load() -> pd.DataFrame:
        # GUI를 통해 CSV 파일을 선택할 수 있는 Dialog 창 띄우기
        root = tkinter.Tk()
        root.withdraw()  # Tkinter 창을 숨김

        file_path = filedialog.askopenfilename(
            title="Select a CSV file",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )

        if not file_path:
            raise ValueError("No file selected")
        
        # 파일 로드 성공
        return pd.read_csv(file_path)