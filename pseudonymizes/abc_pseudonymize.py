from abc import ABC, abstractmethod
from typing import List

class ABC_Pseudonymize(ABC):

    @abstractmethod
    def run(self, pseudonymize: str, columns: List[str]) -> bool:
        """
        해당하는 가명처리 진행

        Args:
            pseudonymize (str): 가명처리명(소분류)
            colums (List[str]): 가명처리를 적용할 컬럼 리스트

        Returns:
            bool: 성공 여부
        """