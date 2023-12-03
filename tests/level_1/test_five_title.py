from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    assert change_copy_item("ЦБ может повысить", 5) == "ЦБ может повысить"
    assert change_copy_item("ЦБ может повысить ключевую ставку", 5000) == "Copy of ЦБ может повысить ключевую ставку"
    assert change_copy_item("Copy of ЦБ может повысить ключевую ставку", 5000) == "Copy of ЦБ может повысить ключевую ставку (2)"
    assert change_copy_item("Copy of ЦБ может повысить ключевую ставку (2)", 5000) == "Copy of ЦБ может повысить ключевую ставку (3)"
    assert change_copy_item("Copy of ЦБ может повысить ключевую ставку калябаля(2)", 5000) == "Copy of ЦБ может повысить ключевую ставку (3)"
    assert change_copy_item("Copy of ЦБ может повысить(2) ключевую ставку (2)калябаля", 5000) == "Copy of ЦБ может повысить(2) ключевую ставку (3)" #WTF ?
    assert change_copy_item("Copy of Copy of ЦБ может повысить ключевую ставку", 5000) == "Copy of Copy of ЦБ может повысить ключевую ставку (2)"
    base_sting = "ЦБ может повысить"
    for i in range(10):
        base_sting = change_copy_item(base_sting, 5000) #return 'ЦБ может повысить'
        assert base_sting == "Copy of ЦБ может повысить" + '' if i == 0 else ' (' + str(i) + ')'
