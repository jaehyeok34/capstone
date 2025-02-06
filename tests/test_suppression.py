import pandas as pd
from suppression import Suppression as Sup

df = pd.read_csv("resources/datas.csv")
sup = Sup(df)

def test_general():
    print()
    sup.general(["name", "ssn"])
    print(df.head(1))

