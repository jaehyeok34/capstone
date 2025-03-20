import json
from typing import Any, Dict, List
import docker


class Agent:

    def __init__(self, directory_path: str):
        if directory_path is None:
            raise ValueError("directory_path is None")
        
        self.directory_path = directory_path

    # 메타데이터를 전달받아, executeMode에 따른 동작을 수행하는 메소드
    def execute(self, metadata: Dict[str, Any]) -> bool:
        if metadata is None:
            raise ValueError("metadata is None")
        
        # 메타데이터에서 실행 모드 추출
        execute_mode = metadata.get("executeMode")
        if execute_mode is None:
            raise ValueError("executeMode is None")
        
        # 실행 모드 별 동작 수행
        if execute_mode == "command":
            pass

        elif execute_mode == "api":
            pass
    
    # 실행 모드가 command일 때, 수행하는 메소드
    def execute_command(self, metadata: Dict[str, Any]) -> bool:
        if metadata is None:
            raise ValueError("metadata is None")
        
        # 메타데이터에서 이미지명 추출
        image_name = metadata.get("imageName")
        if image_name is None:
            raise ValueError("imageName is None")
        
        # 도커 이미지 다운로드
        ok = self.pull_image(image_name)
        if not ok:
            print("[Debug]execute_command 도커 이미지 다운로드 실패")
            return False
        
        # 명령 실행
        command: List[str] = metadata.get("command")
        if command is None:
            raise ValueError("command is None")
        
        # TODO: command를 통해 docker container화 후에 커맨드 실행하기
        return True

    # metadata에서 imageName을 추출하여 도커 이미지를 다운로드하는 메소드
    def pull_image(self, image_name: str) -> bool:
        if image_name is None:
            raise ValueError("image_name is None")

        try:
            client = docker.from_env()

            # 로컬에 이미지가 존재하는지 확인
            local_images = client.images.list(name=image_name)
            if len(local_images) == 0:
                client.images.pull(image_name)

            print("[Debug]pull_image 이미지 준비 완료")
            return True
        
        except Exception as e:
            print("[Debug]pull_image 예외 발생:", e)
            return False
    
        
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
            print("[Debug]save_metadata 예외 발생:", e)
            return False
        
    #     # 미들서버에 메타데이터 리스트를 요청하는 코드(GET)
    # def request_metadata_list(self) -> List[Dict[str, str]] | None:
    #     try:
    #         url = "http://localhost:3000/get-metadata-list"
    #         response = requests.get(url)

    #         response.raise_for_status()
    #         return response.json()
        
    #     except Exception as e:
    #         print("예외 발생:", e)
    #         return None
    
    # # 메타에이터명을 기준으로 미들서버에 메타데이터를 요청하는 코드(GET + Parameter)
    # def request_metadata_with_name(self, metadata_name: str) -> Dict[str, Any] | None:
    #     try:
    #         url = "http://localhost:3000/get-metadata?name=" + metadata_name
    #         response = requests.get(url)

    #         response.raise_for_status()
    #         return response.json()
        
    #     except Exception as e:
    #         print("예외 발생:", e)
    #         return None