from csv_loader import CSV_Loader
from pseudonymize_selector import Pseudonymize_Selector
from role_selector import Role_Selector

if __name__ == "__main__":
    # 1. CSV 파일 로드
    dataframe = CSV_Loader.load() 

    # 2. 컬럼별 역할 선택
    roles = Role_Selector.select(dataframe.columns)

    # 3. 식별자, 비민감정보 -> 삭제
    for column, role in roles.items():
        if role == "식별자" or role == "비민감정보":
            del dataframe[column]

    # 4. 남은 컬럼(준식별자, 민감정보)에 적용할 가명처리 선택
    pseudonymizes = Pseudonymize_Selector.select(dataframe.columns)

    