import requests
import json

url = "http://localhost:3001/metadata/upload"
data = {
    "imageName": "ubuntu:latest",
    "containerName": "test-container",
    "executionMode": "command",
    "command": ["echo", "hello"],
    "outputType": "csv",
    "description": "echo hello"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.text)