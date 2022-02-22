import pandas as pd
import os


# Funkcja wczytuje do dataframe plik excel z dochodami z PIT, znajdujący się pod podaną ściezka. (jeżeli istnieje)
def powiaty_import_pit(data_powiaty_pit_path, data_powiaty_NPP_pit_path):
    if not (os.path.exists(data_powiaty_pit_path) and os.path.exists(data_powiaty_NPP_pit_path)):
        return pd.DataFrame()
    else:
        #Powiaty
        data_powiaty_pit = pd.read_excel(data_powiaty_pit_path, header=None,
                                         names=['WK', 'PK', 'Name', 'Partition', 'Income'], usecols=[0, 1, 4, 8, 11],
                                         dtype={0: str, 1: str, 2: str}, engine='openpyxl',
                                         skiprows=list(range(7))).dropna(how='any')
        #Stworzenie id
        data_powiaty_pit.drop(labels="Partition", axis=1, inplace=True)
        data_powiaty_pit['id'] = data_powiaty_pit['WK'] + data_powiaty_pit['PK']
        id = data_powiaty_pit.pop('id')
        data_powiaty_pit = data_powiaty_pit.drop(['WK', 'PK'], axis=1)
        data_powiaty_pit.insert(0, 'id', id)
        #NPP
        data_powiaty_NPP_pit = pd.read_excel(data_powiaty_NPP_pit_path, header=None,
                                         names=['WK', 'PK', 'Name', 'Partition', 'Income'], usecols=[0, 1, 4, 8, 11],
                                         dtype={0: str, 1: str, 2: str}, engine='openpyxl',
                                         skiprows=list(range(7))).dropna(how='any')
        # Usuniecie rozdzialu 75622 w powiatach NPP i kolumny rozdzial
        data_powiaty_NPP_pit.drop_duplicates(subset=["WK", "PK"], ignore_index=True, inplace=True)
        data_powiaty_NPP_pit.drop(labels="Partition", axis=1, inplace=True)
        # Stworzenie id
        data_powiaty_NPP_pit['id'] = data_powiaty_NPP_pit['WK'] + data_powiaty_NPP_pit['PK']
        id = data_powiaty_NPP_pit.pop('id')
        data_powiaty_NPP_pit = data_powiaty_NPP_pit.drop(['WK', 'PK'], axis=1)
        data_powiaty_NPP_pit.insert(0, 'id', id)
        #Polaczenie i sortowanie data frame'ow
        data_powiaty_pit = pd.concat([data_powiaty_pit, data_powiaty_NPP_pit], ignore_index=True)
        data_powiaty_pit = data_powiaty_pit.sort_values(by=['id'], ignore_index=True)
    return data_powiaty_pit

# Funkcja wczytuje do dataframe plik excel z ludnoscia, znajdujący się pod podaną ściezka. (jeżeli istnieje)
def powiaty_import_ppl(data_powiaty_ppl_path):
    if not os.path.exists(data_powiaty_ppl_path):
        return pd.DataFrame()
    else:
        data_powiaty_ppl = pd.read_excel(data_powiaty_ppl_path, header=None,
                                       names=['Name', 'id', 'Population'], usecols=[0, 1, 2],
                                       dtype={0: str, 1: str}, engine='xlrd',
                                       skiprows=list(range(8))).dropna(how='any')
    return data_powiaty_ppl