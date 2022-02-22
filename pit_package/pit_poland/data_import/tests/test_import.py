import pandas as pd
from .. import gminy_import_pit, powiaty_import_pit, wojewodztwa_import_pit
from .. import gminy_import_ppl, powiaty_import_ppl, wojewodztwa_import_ppl

def test_import_pit():
    # Sprawdzenie blednej sciezki
    expected_df = pd.DataFrame()
    pd.testing.assert_frame_equal(gminy_import_pit("not even a path"), expected_df, check_column_type=True)
    pd.testing.assert_frame_equal(powiaty_import_pit("not even a path", "not even a path too"), expected_df, check_column_type=True)
    pd.testing.assert_frame_equal(wojewodztwa_import_pit("not even a path"), expected_df, check_column_type=True)

    # Sprawdzenie poprawnej formy importu
    # expected_gminy = pd.DataFrame({'id': ['0201011', '0201022', '0201032', '0201043', '0201052'],
    #                                'Name': ['BOLESŁAWIEC', 'BOLESŁAWIEC', 'GROMADKA', 'NOWOGRODZIEC', 'OSIECZNICA'],
    #                                'Income': [40456699, 13789712, 3573540, 9553744, 5844560]})


def test_import_ppl():
    # Sprawdzenie blednej sciezki
    expected_df = pd.DataFrame()
    pd.testing.assert_frame_equal(gminy_import_ppl("not even a path"), expected_df, check_column_type=True)
    pd.testing.assert_frame_equal(powiaty_import_ppl("not even a path"), expected_df,
                                  check_column_type=True)
    pd.testing.assert_frame_equal(wojewodztwa_import_ppl("not even a path"), expected_df, check_column_type=True)
