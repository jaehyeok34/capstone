import json
from typing import Any, Dict, List
import requests


class Agent:

    def __init__(self):
        pass

    # 미들서버에 메타데이터 리스트를 요청하는 코드(GET)
    def request_metadata_list(self) -> List[Dict[str, str]] | None:
        try:
            url = "http://localhost:3000/get-metadata-list"
            response = requests.get(url)

            response.raise_for_status()
            return response.json()
        
        except Exception as e:
            print("예외 발생:", e)
            return None
    
    # 메타에이터명을 기준으로 미들서버에 메타데이터를 요청하는 코드(GET + Parameter)
    def request_metadata_with_name(self, metadata_name: str) -> Dict[str, Any] | None:
        try:
            url = "http://localhost:3000/get-metadata?name=" + metadata_name
            response = requests.get(url)

            response.raise_for_status()
            return response.json()
        
        except Exception as e:
            print("예외 발생:", e)
            return None

    # 인자로 전달된 메타데이터를 파일 시스템에 저장하는 메소드
    def save_metadata(self, metadata: Dict[str, Any]) -> bool:
        file_path = "./metadatas.json"

        try:
            metadatas: List = None
            with open(file_path, "r") as f:
                metadatas = json.load(f)["metadatas"]
                metadatas.append(metadata)

            with open(file_path, "w") as f:
                json.dump({"metadatas": metadatas}, f, indent=4)

            return True

        except Exception as e:
            print("예외 발생:", e)
            return False
