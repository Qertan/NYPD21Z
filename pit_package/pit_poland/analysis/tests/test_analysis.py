import pandas as pd
from .. import difference_pit, average_income

def test_difference():
    # Dane testowe
    test_data19 = pd.DataFrame({'id': ['01', '02'], 'Name': ['A', 'B'], 'Income': [100, 200]})
    test_data20 = pd.DataFrame({'id': ['01', '02'], 'Name': ['A', 'B'], 'Income': [200, 100]})
    expected_df = pd.DataFrame({'id': ['01', '02'], 'Name19': ['A', 'B'], 'Income19': [100, 200], 'Name20':['A', 'B'],
                                'Income20': [200, 100], 'Difference': [100, -100]})
    # Testowanie funkcji liczacej roznice w dochodach pit
    pd.testing.assert_frame_equal(difference_pit(test_data19, test_data20), expected_df)

def test_avg():
    # Dane testowe
    test_pit = pd.DataFrame({'id': ['01', '02'], 'Name': ['A', 'B'], 'Income': [100, 200]})
    test_ppl = pd.DataFrame({'Name': ['A', 'B'], 'id': ['01', '02'], 'Population': [20, 10]})
    expected_df = pd.DataFrame({'id': ['01', '02'], 'Income': [100, 200], 'Name': ['A', 'B'],
                                'Population': [20, 10], 'average_income': [100/(20*0.57*0.17), 200/(10*0.57*0.17)]})
    # Testowanie funkcji liczacej sredni dochod opodatkowany z uwzglednieniem stałych
    pd.testing.assert_frame_equal(average_income(test_pit, test_ppl), expected_df)