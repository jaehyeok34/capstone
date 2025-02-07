from typing import Tuple
import pandas as pd
from pseudonymizes.suppression import Suppression as Sup

def setup() -> Tuple[pd.DataFrame, Sup]:
    print()
    df = pd.read_csv("resources/datas.csv")
    return (df, Sup(df))


def test_general():
    df, sup = setup()
    sup.general(["name", "ssn"])
    print(df.head(3))


def test_partial():
    df, sup = setup()
    sup.partial(["name", "ssn"])
    print(df.head(3))


def test_record():
    df, sup = setup()
    sup.record()
    print(df.head(3))



def test_local():
    df, sup = setup()
    sup.local(["name", "ssn"])
    print(df.head(3))



def test_masking():
    df, sup = setup()
    sup.masking(["name", "ssn"])
    print(df.head(3))



def test_address():
    df, sup = setup()
    sup.general(["address"])
    print(df.head(3))
