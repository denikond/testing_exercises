from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime
import decimal
import dataclasses

def test_parse_ineco_expense():
    sms_amount_sum = '1000.89'
    sms_something1 = 'something'
    sms_card_number = '1234123412341234'
    sms_spent_at_strict_format = "12.11.21 15:30"
    sms_spent_in: str = "something long string"
    sms_authcode_strict_format_separator = "authcode"
    sms_authcode_nonstrict = "something"
    spent_at_datetime_format = datetime.datetime.strptime(sms_spent_at_strict_format, '%d.%m.%y %H:%M')
    ms_v_card = BankCard(last_digits="1234", owner="Ms V")
    mr_v_card = BankCard(last_digits="3412", owner="Mr V")
    cards = [ms_v_card, mr_v_card]
    author = "John Smith"

    sms: str = "{0} {1}, {2} {3} {4} {5} {6}".format(sms_amount_sum, sms_something1, sms_card_number,
                                                sms_spent_at_strict_format, sms_spent_in,
                                                sms_authcode_strict_format_separator, sms_authcode_nonstrict)

    assert (parse_ineco_expense(
        SmsMessage(sms, author, datetime.datetime(2023, 1, 1)), cards) ==
            Expense(amount=decimal.Decimal(sms_amount_sum), card=ms_v_card, spent_in=sms_spent_in,
                    spent_at=spent_at_datetime_format))
