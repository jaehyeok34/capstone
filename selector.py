from suppressions import Suppressions

class Selector:
    pseudo_dict = {
        "Suppression": {
            "general": ("suppression-general", Suppressions.general),
            "partial": ("suppression-partial", Suppressions.partial),
            "record": ("suppression-record", Suppressions.record),
        }
        # "Suppression": ["general", "partial", "record", "sup_local", "masking", "address"], # 삭제 기법
        # "Rounding": ["off", "up", "down", "random"], # 라운딩 기법
        # "Generalization": ["gen_local", "categorizion"], # 범주화 기법
        # "Aggregation": ["mean", "max", "min", "mode", "median", ], # 총계처리 기법
        # "MicroAggregation": ["micro_mean", "micro_max", "micro_min", "micro_mode", "micro_median"], # 부분총계처리 기법
    }


    @classmethod
    def run(cls, columns: list, columns_dict: dict[str, list]):
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
    def __append(cls, columns: list, columns_dict: dict[str, list]) -> None:
        print("가명처리 적용 컬럼 선택")
        selected_column = cls.__select_column(columns)

        print("가명처리 기법 선택(중분류)")
        selected_middle = cls.__select_middle()
        
        print("가명처리 기법 선택(소분류)")
        selected_small = cls.__select_small(selected_middle)

        # 중복된 값이 있는지 확인
        if selected_small in columns_dict[selected_column]:
            print(f"{selected_column} 컬럼에 이미 {selected_small} 가명처리 기법이 적용되어 있습니다.")
            return

        # 가명처리 기법 추가
        columns_dict[selected_column].append(selected_small)


    @classmethod
    def __remove(cls, columns: list, columns_dict: dict[str, list]) -> None:
        print("가명처리 제거 컬럼 선택")
        selected_column = cls.__select_column(columns)

        if not columns_dict[selected_column]:
            print(f"{selected_column} 컬럼에 적용된 가명처리 기법이 없습니다.")
            return

        print("제거할 가명처리 기법 선택")
        selected_small = cls.__select_option(columns_dict[selected_column], "소분류")

        # 가명처리 기법 제거
        columns_dict[selected_column].remove(selected_small)


    @classmethod
    def __search(cls, columns: list, columns_dict: dict[str, list]) -> None:
        for column, techniques in columns_dict.items():
            print(f"{column}: ", end="")
            if techniques:
                print(f"{', '.join(techniques)}")
            else:
                print("None")

        print(columns_dict)


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