# Funkcja oblicza wariancje dochodow w jednostkach podleglych

def variance_income(lower_tier, upper_tier):
    # Zapobiegniecie zmian argumentow
    lower_tier = lower_tier.copy(deep=True)
    upper_tier = upper_tier.copy(deep=True)
    # Usuniecie podwojnego liczenia ludzi spowodowanego przez gminy M-W
    lower_tier = lower_tier[-lower_tier.id.str.match('......3')]
    upper_id = list(upper_tier['id'])
    variance_income = []
    for key in upper_id:
        variance_income.append(lower_tier[lower_tier.id.str.match(key)]['average_income'].var())

    upper_tier['variance_income'] = variance_income
    # Usuniecie miast NPP
    upper_tier = upper_tier[upper_tier.variance_income != 0]
    return upper_tier
