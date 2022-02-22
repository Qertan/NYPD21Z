import pandas as pd
import os


# Funkcja wczytuje do dataframe plik excel z dochodami z PIT, znajdujący się pod podaną ściezka. (jeżeli istnieje)
def wojewodztwa_import_pit(data_wojewodztwa_pit_path):
    if not os.path.exists(data_wojewodztwa_pit_path):
        return pd.DataFrame()
    else:
        data_wojewodztwa_pit = pd.read_excel(data_wojewodztwa_pit_path, header=None,
                                       names=['WK', 'Name', 'Income'], usecols=[0, 4, 11],
                                       dtype={0: str, 1: str}, engine='openpyxl',
                                       skiprows=list(range(7))).dropna(how='all')
        # Stworzenie id
        data_wojewodztwa_pit['id'] = data_wojewodztwa_pit['WK']
        id = data_wojewodztwa_pit.pop('id')
        data_wojewodztwa_pit = data_wojewodztwa_pit.drop(['WK'], axis=1)
        data_wojewodztwa_pit.insert(0, 'id', id)
    return data_wojewodztwa_pit


# Funkcja wczytuje do dataframe plik excel z ludnoscia, znajdujący się pod podaną ściezka. (jeżeli istnieje)
def wojewodztwa_import_ppl(data_wojewodztwa_ppl_path):
    if not os.path.exists(data_wojewodztwa_ppl_path):
        return pd.DataFrame()
    else:
        data_wojewodztwa_ppl = pd.read_excel(data_wojewodztwa_ppl_path, header=None,
                                       names=['Name', 'Population'], usecols=[0, 1],
                                       dtype={0: str}, engine='xlrd',
                                       skiprows=list(range(8)), nrows=16)
        id = ['02', '04', '06', '08', '10', '12', '14', '16', '18', '20', '22', '24', '26', '28', '30', '32']
        data_wojewodztwa_ppl.insert(loc=0, column="id", value=id)
    return data_wojewodztwa_ppl
# df=wojewodztwa_import_ppl("C:/Users/48791/PycharmProjects/dane/ludnosc/Tabela_IV.xls")
# print(df.head)