from typing import Dict, List


class Pseudonymize_Selector:
    pseudonymizes = {
        "삭제기술": ("일반삭제", "부분삭제", "행 항목 삭제", "로컬삭제", "마스킹", "주소"),
        "통계도구": ("총계처리", "부분총계"),
        "범주화 기술": ("일반 라운딩", "랜덤 라운딩", "로컬 일반화", "문자데이터 범주화"),
    }
    

    @classmethod
    def select(cls, columns: List[str]) -> Dict[str, str]:
        print("가명처리 기법 목록")
        for key, value in cls.pseudonymizes.items():
            print(f"{key}: {", ".join(value)}")

        selected_pseudonymize = {}
        for column in columns:
            print(f"{column}에 적용할 가명처리 기술 선택", end=" ")
            selected = cls.__select_option([item for sublist in cls.pseudonymizes.values() for item in sublist])
            selected_pseudonymize[column] = selected


    @classmethod
    def __select_option(cls, options: List[str]) -> str:
        while True:
            selected_option = input("> ")
            if selected_option in options:
                return selected_option

            print(f"존재하지 않은 가명처리 기술입니다. 다시 입력해주세요.")