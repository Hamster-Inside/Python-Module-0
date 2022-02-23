from main_task import number_table_generator
from main_task import winning_numbers_counter


def test_generating_number_table():
    table = number_table_generator(5)
    assert table == [1, 2, 3, 4, 5]


def test_winning_numbers_counter_01():
    my_table = [1, 2, 3, 4, 5, 6]
    random_table = [2, 4, 6, 33, 22, 18]
    assert test_winning_numbers_counter(my_table, random_table) == 3
