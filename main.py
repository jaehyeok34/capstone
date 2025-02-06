from csv_loader import CSV_Loader
from pseudonymize_selector import Pseudonymize_Selector
from role_selector import Role_Selector


if __name__ == "__main__":
    # 1. CSV 파일 로드
    dataframe = CSV_Loader.load() 

    # 2. 컬럼별 역할 선택
    role_dict = Role_Selector.select(dataframe.columns)

    # 3. 식별자, 비민감정보 -> 삭제
    for column, role in role_dict.items():
        if role == "식별자" or role == "비민감정보":
            del dataframe[column]

    # 4. 남은 컬럼(준식별자, 민감정보)에 적용할 가명처리 선택
    pseudonymize_dict = Pseudonymize_Selector.select(dataframe.columns) # { column: pseudonymize }
    
    # 5. 가명처리 적용
    # TODO: 가명처리 적용 기능 구현
    # 레벨별로 가명처리 적용
    print(pseudonymize_dict)

# 고민..
# 마스킹, 부분삭제, 주소 등의 경우 범위를 선택해야 함 ...
# 범위 선택을 필요로 하는 가명처리 기술의 경우는 어떻게 해야할까 ..


# 레벨 조정 가능한 요소

# 삭제기술
# 일반삭제 X
# 부분삭제 O
# 행 항목 삭제 X
# 로컬삭제 X
# 마스킹 O
# 주소 O

# 통계도구
# 총계처리(평균, 최대값, 최소값, 최빈값, 중간값) X
# 부분총계 X

# 라운딩 X