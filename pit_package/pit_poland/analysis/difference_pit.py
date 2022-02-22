# Funkcja oblicza roznice w dochodach z PIT dla jst (jezeli jst przestaje istniec lub wlasnie powstala
# to nie ma sensu mowic o jej roznicy w dochodzie z PIT.

def difference_pit(data19, data20):
    # Zapobiegniecie zmian argumentow
    data19 = data19.copy(deep=True)
    rows1 = data19.shape[0]
    data19 = data19.join(data20.set_index('id'), on='id', how='left', lsuffix="19", rsuffix='20', sort=True)
    data19['Difference'] = data19['Income20'] - data19['Income19']
    rows2 = data19.shape[0]
    if rows1 > rows2:
        raise Exception("Nie wszystkie jednostki samorządu terytorialnego z pliku z "
                        "PIT są zawarte w pliku z ludnością.")
    return data19
