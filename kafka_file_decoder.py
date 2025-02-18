#!/usr/bin/env python3
import os
import sys
import json
import base64
from kafka import KafkaConsumer

# 저장 폴더 지정 (loads)
output_dir = "loads"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# KafkaConsumer 설정: 업로드 파일 토픽에서 데이터 수신
consumer = KafkaConsumer(
    'upload_files',
    bootstrap_servers=['localhost:9092'],  # 브로커 주소 환경에 맞게 수정
    auto_offset_reset='earliest',  # 처음부터 읽기
    group_id='python_file_decoder'
)

# 메시지 수신 및 처리
try:
    for message in consumer:
        try:
            payload = message.value.decode('utf-8')
            data = json.loads(payload)
            filename = data.get('filename', 'output_file')
            filedata = data.get('filedata', '')
            if not filedata:
                print("filedata 필드가 없습니다.")
                continue

            # base64 디코딩
            file_bytes = base64.b64decode(filedata)
            file_path = os.path.join(output_dir, filename)

            with open(file_path, 'wb') as f:
                f.write(file_bytes)
            print(f"저장 완료: {file_path}")
        except Exception as err:
            print("메시지 처리 중 오류:", err)
except KeyboardInterrupt:
    print("소비 중단")
    sys.exit(0)
