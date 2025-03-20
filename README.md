# 플랫폼 agent 프로그램

무엇을 개발해야 할까...
1. Middle Server에 Metadata를 요청하는 기능
    1-1. Metadata List를 확인하고, 선택하는 방법(수동)
        - Middle Server에 있는 Metadata List를 전달 받음
        - 원하는 Metadata를 선택함
        - Metadata를 반환 받음3
    
    1-2. 처리 목적을 전달(자동)
        - 프라이빗 데이터 처리 목적과 방법 등을 전달
        - Middle Server는 이에 맞는 Metadata를 반환

2. 전달받은 Metadata를 파일 시스템에 저장
    - 기본적으로 Metadata에 모든 내용 + 현재 상태(컨테이너화 됐는지.. 사용 중인지 등)

3. 컨테이너화


- Web을 통해 "~~한 역할이 필요" 라고 작성 후 "전송" 버튼을 누르면, Agent의 request_metadata를 통해 외부 서버로 요청 됨
- 외부 서버에서 반환 받게 되면, 

metadata에 있는 executionMode에 따라 컨테이너화 후 실행할 지, 일회용인지 등을 결정