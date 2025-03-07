import json

import pandas as pd
from pseudonymizes.pseudonymizer import Pseudonymizer
from pseudonymizes.generalization import Generalization

with open("resources/pseudonymize.json", "r", encoding="utf-8") as f:
    pseudonymizes = json.load(f)

df = pd.read_csv("resources/datas.csv")


def test_run():
    print()
    pseudonymizer = Pseudonymizer(
        df=df, 
        pseudonymize_dict={
        "일반삭제": ["name", "ssn", "phone_number", "email"],
        "랜덤 라운딩": ["income", "monthly_spending"],
        "주소": ["address"]
        }
    )

    pseudonymizer.run()
    print(df.head(3))


def test_abc():
    print()
    generalization = Generalization(
        pseudonymizes=pseudonymizes["범주화기술"],
        df=df
    )

