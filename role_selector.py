from typing import List, Dict


class Role_Selector:
    role = ("식별자", "준식별자", "민감정보", "비민감정보")

    @classmethod
    def select(cls, columns: List[str]) -> Dict[str, str]:
        print(f"역할 목록: {", ".join(cls.role)}")

        selected_roles = {}
        for column in columns: 
            while True:
                selected_role = input(f"{column} > ")
                if selected_role not in cls.role:
                    print("잘못된 역할입니다. 다시 입력해주세요.")
                    continue

                selected_roles[column] = selected_role
                break
        
        return selected_roles