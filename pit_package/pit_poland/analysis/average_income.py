from .constants import tax, working_percent
# Funckja oblicza sredni dochod opodatkowany przy powyzszych zalozeniach
def average_income(pit, ppl):
    #Zapobiegniecie zmian argumentow
    pit = pit.copy(deep=True)
    ppl = ppl.copy(deep=True)
    rows1 = pit.shape[0]
    pit = pit[['id', 'Income']].join(ppl.set_index('id'), on='id', how='left', sort=True)
    pit['average_income'] = pit['Income'] / (pit['Population'] * working_percent * tax)
    rows2 = pit.shape[0]
    if rows1 > rows2:
        raise Exception("Nie wszystkie jednostki samorządu terytorialnego z pliku z "
                        "PIT są zawarte w pliku z ludnością.")
    return pit
