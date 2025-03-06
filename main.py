import time
from typing import Dict
import requests
import docker as docker_module

# def get_metadata() -> dict | None:
#     url = "http://localhost:3000/get-metadata"
#     try:
#         # HTTP GET 요청을 보내고 응답 수신
#         response = requests.get(url)

#         # HTTP 요청 실패 시 예외 발생
#         response.raise_for_status()

#         # 응답 데이터 JSON 형식으로 파싱
#         return response.json()
    
#     except requests.RequestException as e:
#         print("HTTP 요청 중 예외 발생:", e)
#         return None

def get_metadata() -> Dict:
    return {
        "imageName": "ubuntu:latest",
        "containerName": "test-container"
    }


if __name__ == "__main__": 
    metadata = get_metadata()
    print("metadata:", metadata)

    # metadata를 기반으로 docker container 생성
    if metadata:
        client = docker_module.from_env()
        try:
            # 이미지가 로컬에 없으면 Docker Hub에서 이미지 다운로드
            client.images.pull(metadata["imageName"])
            print(f"이미지 {metadata['imageName']} 다운로드 완료")
        except docker_module.errors.ImageNotFound:
            print(f"이미지 {metadata['imageName']}를 찾을 수 없습니다.")
        except docker_module.errors.APIError as e:
            print(f"이미지 다운로드 중 API 오류 발생: {e}")
        except Exception as e:
            print("???")

        try:
            container = client.containers.run(
                image=metadata["imageName"],
                name=metadata["containerName"],
                detach=True
            )
            print("container:", container)
        except Exception as e:
            print("Docker 예외 발생:")


    time.sleep(30)