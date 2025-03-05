import requests

def get_metadata() -> dict | None:
    url = "http://localhost:3000/get-metadata"
    try:
        # HTTP GET 요청을 보내고 응답 수신
        response = requests.get(url)

        # HTTP 요청 실패 시 예외 발생
        response.raise_for_status()

        # 응답 데이터 JSON 형식으로 파싱
        return response.json()
    
    except requests.RequestException as e:
        print("HTTP 요청 중 예외 발생:", e)
        return None

if __name__ == "__main__": 
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future1 = executor.submit(get_metadata)
        future2 = executor.submit(get_metadata)
        m1 = future1.result()
        m2 = future2.result()
        
    print("m1:", m1)
    print("m2:", m2)