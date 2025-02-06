from old.suppressions import Suppressions
from typing import Tuple, List, Callable

class Selector:
    pseudo_dict = {
        "Suppression": {
            "general": ("suppression-general", Suppressions.general),
            "partial": ("suppression-partial", Suppressions.partial),
            "record": ("suppression-record", Suppressions.record),
            "local": ("suppression-local", Suppressions.local),
            "masking": ("suppression-masking", Suppressions.masking),
            "address": ("suppression-address", Suppressions.address),
        }
        
        # "Suppression": ["general", "partial", "record", "sup_local", "masking", "address"], # 삭제 기법
        # "Rounding": ["off", "up", "down", "random"], # 라운딩 기법
        # "Generalization": ["gen_local", "categorizion"], # 범주화 기법
        # "Aggregation": ["mean", "max", "min", "mode", "median", ], # 총계처리 기법
        # "MicroAggregation": ["micro_mean", "micro_max", "micro_min", "micro_mode", "micro_median"], # 부분총계처리 기법
    }


    @classmethod
    def run(cls, columns: List, columns_dict: dict[str, List[Tuple[str, Callable]]]) -> None:
        actions = {
            "추가": cls.__append,
            "제거": cls.__remove,
            "조회": cls.__search
        }

        while True:
            action = cls.__select_option(["추가", "제거", "조회", "종료"], "작업")

            if action == "종료":
                print("작업을 종료합니다.")
                break

            if action in actions:
                actions[action](columns, columns_dict)
    

    @classmethod
    def __append(cls, columns: list, columns_dict: dict[str, List[Tuple[str, Callable]]]) -> None:
        print("-----가명처리 적용 컬럼 선택-----")
        selected_column = cls.__select_column(columns)

        print("-----가명처리 기법 선택(중분류)-----")
        selected_middle = cls.__select_middle() # 중분류 key 값
        
        print("-----가명처리 기법 선택(소분류)-----")
        selected_small = cls.__select_small(selected_middle) # 소분류 key 값

        selected_pseudo: Tuple[str, Callable] = cls.pseudo_dict[selected_middle][selected_small] # 선택된 가명처리 기법(튜플)
        if selected_pseudo[0] in [v[0] for v in columns_dict[selected_column]]: # 튜플 중 첫 번째(가명처리 기법 이름)가 이미 존재하는지 확인
            print(f"{selected_column} 컬럼에 이미 {selected_small} 가명처리 기법이 적용되어 있습니다.")
            return

        # 가명처리 기법 추가
        columns_dict[selected_column].append(selected_pseudo)


    @classmethod
    def __remove(cls, columns: list, columns_dict: dict[str, List[Tuple[str, Callable]]]) -> None:
        print("-----가명처리 제거 컬럼 선택-----")
        selected_column = cls.__select_column(columns)

        if not columns_dict[selected_column]: # 가명처리 기법이 존재하지 않을 때(리스트가 비어 있을 때)
            print(f"{selected_column} 컬럼에 적용된 가명처리 기법이 없습니다.")
            return

        print("제거할 가명처리 기법 선택")
        selected_small = cls.__select_option([v[0] for v in columns_dict[selected_column]], "소분류")

        # 가명처리 기법 제거(튜플 중 첫 번째(가명처리 기법 이름)가 선택된 가명처리 기법과 같은 것을 제외한 새로운 리스트 생성)
        columns_dict[selected_column] = [pseudo for pseudo in columns_dict[selected_column] if pseudo[0] != selected_small]


    @classmethod
    def __search(cls, columns: list, columns_dict: dict[str, List[Tuple[str, Callable]]]) -> None:
        for key, value in columns_dict.items():
            print(f"{key}: ", end="")
            if value:
                print(f"{', '.join([pseudo[0] for pseudo in value])}") # Tuple의 첫 번째 요소(가명처리 기법 이름)만 출력
            else:
                print("None")


    @classmethod
    def __select_option(cls, options: list, prompt: str) -> str:
        while True:
            print(", ".join(options), "> ", end="")
            selected_option = input()
            if selected_option in options:
                return selected_option

            print(f"존재하지 않은 {prompt}입니다. 다시 입력해주세요.")


    @classmethod
    def __select_column(cls, columns: list) -> str:
        return cls.__select_option(columns, "컬럼명")


    @classmethod
    def __select_middle(cls) -> str:
        return cls.__select_option(cls.pseudo_dict.keys(), "중분류")


    @classmethod
    def __select_small(cls, selected_middle: str) -> str:
        return cls.__select_option(cls.pseudo_dict[selected_middle].keys(), "소분류")