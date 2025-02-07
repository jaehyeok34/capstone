from typing import List


class Util:

    @staticmethod
    def get_scope(option: str) -> List[int]:
        while True:
            try:
                scope = input(f"{option} 범위 입력(예. 1, 5) > ")
                start, end = map(int, scope.split(", "))
                if (start < 0) or (end < 0) or (start >= end):
                    raise ValueError
                
                break

            except ValueError:
                print("잘못된 입력입니다. 다시 입력해 주세요.")

        return [start, end]
    

    @staticmethod
    def get_indexes(option: str = "가명처리") -> List[int]:
        while True:
            try:
                indexes = input(f"{option}을/를 적용할 인덱스를 입력하세요 (예. 1, 2, 3) > ")
                index_list = list(map(int, indexes.split(", ")))
                if any(index < 0 for index in index_list):
                    raise ValueError
                
                break

            except ValueError:
                print("잘못된 입력입니다. 다시 입력해 주세요.")

        return index_list