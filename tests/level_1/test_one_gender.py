from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize("Петров", "Петрова", "male") == "Петров"
    assert genderalize("Петров", "Петрова", "female") == "Петрова"
    assert genderalize("Петров", "Петрова", "male") != "Петрова"
