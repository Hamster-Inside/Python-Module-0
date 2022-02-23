from main_task import number_table_generator


def test_generating_number_table():
    table = number_table_generator(5)
    assert table == [1, 2, 3, 4, 5]
