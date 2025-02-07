import json
import pandas as pd
from pseudonymizes.suppression import Suppression as Sup

df = pd.read_csv("resources/datas.csv")

with open("resources/pseudonymize.json", "r", encoding="utf-8") as f:
    pseudonymizes = json.load(f)

sup = Sup(pseudonymizes, df)

def test_general():
    print()
    sup.general(["name", "ssn"])
    print(df.head(1))


def test_partial():
    print()
    sup.partial(["name", "ssn"])
    print(df.head(3))


def test_masking():
    print()
    sup.masking(["name", "ssn"])
    print(df.head(3))


def test_address():
    print()
    sup.address(["address"])
    print(df.head(3))