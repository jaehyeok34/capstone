import json
from typing import Dict, List


class Pseudonymize_Selector:
    @classmethod
    def __get_pseudonymize(cls) -> Dict[str, List[str]]:
        with open("resources/pseudonymize.json", "r", encoding="utf-8") as f:
            return json.load(f)
        

    @classmethod
    def select(cls, columns: List[str]) -> Dict[str, str]:
        pseudonymizes = cls.__get_pseudonymize()

        print("가명처리 기법 목록")
        for key, value in pseudonymizes.items():
            print(f"{key}: {", ".join(value)}")

        selected_pseudonymize: Dict[str, List[str]] = {} # { 가명처리명: [컬럼명, ...] }
        for column in columns:
            print(f"{column}에 적용할 가명처리 기술 선택", end=" ")
            selected = cls.__select_option([item for sublist in pseudonymizes.values() for item in sublist]) # 가명처리명
            selected_pseudonymize.setdefault(selected, []).append(column)

        return selected_pseudonymize
    

    @classmethod
    def __select_option(cls, options: List[str]) -> str:
        while True:
            selected_option = input("> ")
            if selected_option in options:
                return selected_option

            print(f"존재하지 않은 가명처리 기술입니다. 다시 입력해주세요.")