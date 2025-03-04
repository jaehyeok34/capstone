import os
from typing import List

import pandas as pd


class Pseudonymize_CSV:
    @staticmethod
    def run(file_paths: List[str]) -> bool:
        for file_path in file_paths:
            print(file_path)
            
            # if not os.path.exists(file_path):
            #     return False
            
            # data_frame = pd.read_csv(file_path).copy()

            # columns_to_remove = [
            #     '이름', '성명', 'name', 
            #     '주민등록번호', '주민번호', 'ssn', 
            #     '전화번호', 'phone_number', 
            #     '주소', 'address'
            # ]
            
            # # 민감정보에 해당하는 컬럼 삭제
            # data_frame.drop(columns=[col for col in data_frame.columns if col in columns_to_remove], inplace=True, errors='ignore')
                        
            # # csv 파일로 저장
            # data_frame.to_csv(f"pseudonymized-{file_path}", index=False)

