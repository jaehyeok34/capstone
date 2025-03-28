import os
import sys
import pandas as pd

def process_file(file_path: str) -> None:
    try:
        df = pd.read_csv(file_path).copy()

        # 식별자 삭제
        identifier = [
            '주민등록번호', '주민번호', 'ssn', 
            '전화번호', '번호', 'phone_number', 'phone number', 
            '이메일', 'email', 'e-mail'
        ]

        df.drop(columns=[col for col in identifier if col in df.columns], inplace=True)
 
        # 준식별자 가명처리
        
        

        # 결과 출력(5개)
        print(df.head(5))
        
    except pd.errors.ParserError as e:
        print(f"Error processing {file_path}: {e}")
        return


def process_directory(dir_path: str) -> None:
    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            process_file(file_path)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main_auto.py {file path or dir path}")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isfile(path):
        process_file(path)

    elif os.path.isdir(path):
        process_directory(path)

    else:
        print(f"Invalid path: {path}")
        sys.exit(1)


if __name__ == "__main__":
    main()