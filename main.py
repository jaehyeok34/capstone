from pseudonymizer import Pseudonymizer as Pseudo
from csv_loader import CSV_Loader

if __name__ == "__main__":
    dataframe = CSV_Loader.load()
    pseudo = Pseudo(dataframe)