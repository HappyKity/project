from test_001 import count_num


def test_num():
    assert count_num(12) == 144
    assert count_num('5') == -1
