from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert (build_url("http://localhost", "main", {'short': 'dict', 'long': 'dictionary'}) ==
            'http://localhost/main?short=dict&long=dictionary')
    assert build_url("http://localhost", "main") == 'http://localhost/main'
