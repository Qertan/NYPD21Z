from .constants import tax, working_percent
# Funckja oblicza sredni dochod opodatkowany przy powyzszych zalozeniach
def average_income(pit, ppl):
    #Zapobiegniecie zmian argumentow
    pit = pit.copy(deep=True)
    ppl = ppl.copy(deep=True)
    pit = pit[['id', 'Income']].join(ppl.set_index('id'), on='id', how='left', sort=True)
    pit['average_income'] = pit['Income'] / (pit['Population'] * working_percent * tax)
    return pit
