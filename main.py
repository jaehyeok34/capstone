import json
from pseudonymizes.pseudonymizer import Pseudonymizer
from utils.csv_loader import CSV_Loader
from utils.pseudonymize_selector import Pseudonymize_Selector
from utils.role_selector import Role_Selector


if __name__ == "__main__":
    # 1-1. CSV 파일 로드
    dataframe = CSV_Loader.load() 

    # 1-2. 가명처리 목록(json) 파일 로드
    with open("resources/pseudonymize.json", "r", encoding="utf-8") as f:
        pseudonymizes = json.load(f)

    # 2-1. 컬럼별 역할 선택
    role_dict = Role_Selector.select(dataframe.columns)

    # 2-2. 식별자, 비민감정보 -> 삭제
    for column, role in role_dict.items():
        if role == "식별자" or role == "비민감정보":
            del dataframe[column]

    # 3. 남은 컬럼(준식별자, 민감정보)에 적용할 가명처리 선택
    pseudonymize_dict = Pseudonymize_Selector.select(pseudonymizes, dataframe.columns) # { 가명처리: [컬럼, ...] }
    
    # 4. 가명처리 적용
    pseudonymizer = Pseudonymizer(dataframe, pseudonymize_dict)
    pseudonymizer.run()

    print("[Debug] 결과")
    print(dataframe.head(5))
