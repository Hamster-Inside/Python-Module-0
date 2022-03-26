from main_task_v2 import winning_numbers_counter
from main_task_v2 import random_numbers_generator


def test_winning_numbers_counter_01():
    my_table = {1, 2, 3, 4, 5, 6}
    random_table = {2, 4, 6, 33, 22, 18}
    assert winning_numbers_counter(my_table, random_table) == 3


def test_random_numbers_range():
    random_numbers = random_numbers_generator()
    random_numbers = sorted(list(random_numbers))
    assert random_numbers[0] >= 1
    assert random_numbers[-1] <= 49
    assert len(random_numbers) == 6
