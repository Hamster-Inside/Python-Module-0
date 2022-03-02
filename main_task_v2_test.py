from main_task_v2 import winning_numbers_counter


def test_winning_numbers_counter_01():
    my_table = {1, 2, 3, 4, 5, 6}
    random_table = {2, 4, 6, 33, 22, 18}
    assert winning_numbers_counter(my_table, random_table) == 3
