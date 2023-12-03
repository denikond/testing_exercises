from unittest import mock
import datetime
from functions.level_1.two_date_parser import compose_datetime_from

@mock.patch('functions.level_1.two_date_parser.datetime.date')
def test_compose_datetime_from(mock_date):
    mock_date.today.return_value = datetime.datetime(2012, 1, 1)

    assert compose_datetime_from("", time_str="18:12") == datetime.datetime(2012, 1, 1, 18, 12)
    assert compose_datetime_from("tomorrow", time_str="18:12") == datetime.datetime(2012, 1, 2, 18, 12)

    mock_date.today.return_value = datetime.datetime(1912, 1, 1)
    assert compose_datetime_from("", time_str="18:12") == datetime.datetime(1912, 1, 1, 18, 12)
    assert compose_datetime_from("tomorrow", time_str="18:12") == datetime.datetime(1912, 1, 2, 18, 12)

    mock_date.today.return_value = datetime.datetime(3912, 1, 1)
    assert compose_datetime_from("", time_str="18:12") == datetime.datetime(3912, 1, 1, 18, 12)
    assert compose_datetime_from("tomorrow", time_str="18:12") == datetime.datetime(3912, 1, 2, 18, 12)