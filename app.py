from flask import Flask, request, jsonify
import os
import shutil
from typing import Dict, List

from pseudonymization_model.pseudonymize_csv import Pseudonymize_CSV

app = Flask(__name__)

@app.route('/pseudonymize/csv', methods=['POST'])
def pseudonymize_csv():
    data: Dict = request.get_json()
    file_paths: List[str] = data.get('filePaths') if data else None
    if not file_paths:
        return jsonify({'error': 'json body에 filePath 필드가 없습니다.'}), 400

    # 가명처리 진행
    Pseudonymize_CSV.run(file_paths=file_paths)

    return '', 200
    

@app.route('/', methods=['GET'])
def home():
    return 'Hello world'
    

if __name__ == '__main__':
    app.run(debug=True, port=3402)