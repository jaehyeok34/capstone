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

try:
    for message in consumer:
        try:
            filename = message.key.decode('utf-8') if message.key else 'output_file'
            b64_string = message.value.decode('utf-8')
            file_bytes = base64.b64decode(b64_string)
            file_path = os.path.join(output_dir, filename)

            with open(file_path, 'wb') as f:
                f.write(file_bytes)

            print(f"Saved: {file_path}")

        except Exception as err:
            print("Error processing message:", err)

except KeyboardInterrupt:
    print("Consumer interrupted")
    sys.exit(0)
