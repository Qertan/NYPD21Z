# Funkcja oblicza wazona srednia dochodow dla jednostek podleglych (lower) danej jednostki (upper)

def weighted_average(lower_tier, upper_tier):
    # Zapobiegniecie zmian argumentow
    lower_tier = lower_tier.copy(deep=True)
    upper_tier = upper_tier.copy(deep=True)
    lower_tier['mult'] = lower_tier['Population'] * lower_tier['average_income']
    # Usuniecie podwojnego liczenia ludzi spowodowanego przez gminy M-W
    lower_tier = lower_tier[-lower_tier.id.str.match('......3')]
    upper_id = list(upper_tier['id'])
    weighted_average = []
    for key in upper_id:
        weighted_average.append(lower_tier[lower_tier.id.str.match(key)]['mult'].sum())

    upper_tier['weighted_sum'] = weighted_average
    upper_tier['weighted_average_income'] = upper_tier["weighted_sum"] / upper_tier["Population"]
    # Usuniecie miast NPP
    upper_tier = upper_tier[upper_tier.weighted_sum != 0]
    upper_tier = upper_tier.drop(columns=['weighted_sum'])
    return upper_tier
