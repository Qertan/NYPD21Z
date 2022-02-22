import pandas as pd
import os


# Funkcja wczytuje do dataframe plik excel z dochodami z PIT, znajdujący się pod podaną ściezka. (jeżeli istnieje)
def gminy_import_pit(data_gminy_pit_path):
    if not os.path.exists(data_gminy_pit_path):
        return pd.DataFrame()
    else:
        data_gminy_pit = pd.read_excel(data_gminy_pit_path, header=None,
                                       names=['WK', 'PK', 'GK', 'GT', 'Name', 'Income'], usecols=[0, 1, 2, 3, 4, 11],
                                       dtype={0: str, 1: str, 2: str, 3: str, 4: str}, engine='openpyxl',
                                       skiprows=list(range(7))).dropna(how='all')
        # Stworzenie id
        data_gminy_pit['id']=data_gminy_pit['WK']+data_gminy_pit['PK']+data_gminy_pit['GK']+data_gminy_pit['GT']
        id=data_gminy_pit.pop('id')
        data_gminy_pit=data_gminy_pit.drop(['WK', 'PK', 'GK', 'GT'], axis=1)
        data_gminy_pit.insert(0,'id',id)
    return data_gminy_pit

#print(gminy_import_pit("Z:/Kuba/Studia/uw/III rok/nypd/pit_2020/20210215_Gminy_2_za_2020.xlsx"))

# Funkcja wczytuje do dataframe plik excel z ludnoscia, znajdujący się pod podaną ściezka. (jeżeli istnieje)
def gminy_import_ppl(data_gminy_ppl_path):
    if not os.path.exists(data_gminy_ppl_path):
        return pd.DataFrame()
    else:
        data_gminy_ppl = pd.read_excel(data_gminy_ppl_path, header=None,
                                       names=['Name', 'id', 'Population'], usecols=[0, 1, 2],
                                       dtype={0: str, 1: str}, engine='xlrd',
                                       skiprows=list(range(8))).dropna(how='any')
    return data_gminy_ppl
# df=gminy_import_ppl("C:/Users/48791/PycharmProjects/dane/ludnosc/Tabela_IV.xls")
# print(df.head)