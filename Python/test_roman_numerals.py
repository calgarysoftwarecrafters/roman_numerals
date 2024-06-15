import pytest

from roman_numerals import global_answer

test_parameters = [(1, "I"), (2, "II"), (3, "III"), (4, "IV"), (5, "V"), (6, "VI"), (7, "VII")]
test_parameters += [(8, "VIII"), (9, "IX"), (10, "X"), (11, "XI"), (12, "XII"), (13, "XIII"), (14, "XIV")]
test_parameters += [(15, "XV"), (16, "XVI"), (17, "XVII"), (18, "XVIII"), (19, "XIX"), (20, "XX"), (21, "XXI")]
test_parameters += [(22, "XXII"), (23, "XXIII"), (24, "XXIV"), (25, "XXV"), (26, "XXVI"), (27, "XXVII"), (28, "XXVIII")]
test_parameters += [(29, "XXIX"), (30, "XXX"), (31, "XXXI"), (32, "XXXII"), (33, "XXXIII"), (34, "XXXIV"), (35, "XXXV")]
test_parameters += [(36, "XXXVI"), (37, "XXXVII"), (38, "XXXVIII"), (39, "XXXIX"), (40, "XL"), (41, "XLI"), (42, "XLII")]
test_parameters += [(100, "C"), (200, "CC"), (300, "CCC"), (400, "CD"), (500, "D"), (600, "DC"), (700, "DCC")]
test_parameters += [(1100, "MC"), (1200, "MCC"), (1300, "MCCC"), (1400, "MCD"), (1500, "MD"), (1600, "MDC"), (1700, "MDCC")]
test_parameters += [(1000, "M"), (2000, "MM"), (3000, "MMM"), (4000, "MMMM"), (5000, "MMMMM"), (6000, "MMMMMM"), (7000, "MMMMMMM")]

@pytest.mark.parametrize("test_input,expected", test_parameters)
def test_global_function(test_input, expected):
    assert global_answer(test_input) == expected
