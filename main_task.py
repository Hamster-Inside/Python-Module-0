""" Lotto game """
import random
import typing


def number_table_generator(number: int = 10) -> typing.List[int]:
    """ Generate table of numbers
    :param number: 10
    :return: [1,2,3,4,5,6,7,8,9,10]
    """
    number_table = []
    for i in range(number):
        number_table.append(i + 1)
    return number_table


def random_number_table_generator(table_of_numbers: typing.List[int]) -> typing.List[int]:
    """ Generator of 6 random numbers to be compared with given numbers
    :param table_of_numbers: [1,2,4,5,...,49] -> or any other table to be mixed
    :return: [3,9,1,2,10,33] -> random number list of 6
    """
    randomly_mixed_numbers = []
    for _ in range(6):
        random_number = random.choice(table_of_numbers)
        randomly_mixed_numbers.append(random_number)
        table_of_numbers.remove(random_number)
    return randomly_mixed_numbers


def winning_numbers_counter(picked_numbers: typing.List[int],
                            random_numbers: typing.List[int]) -> int:
    """ Returns number of numbers that are the same in random number list
    :param picked_numbers: [1,3,22,11,38,40]
    :param random_numbers: [38,22,5,7,8,9]
    :return: 2
    """
    numbers_hit = len((set(picked_numbers)) & (set(random_numbers)))
    return numbers_hit


how_many_times_played = 0
cost_of_one_bet = 3
bet_numbers = [3, 8, 40, 49, 22, 1]
base_number_table = number_table_generator(49)

while True:
    how_many_times_played += 1
    random_lotto_numbers = random_number_table_generator(base_number_table.copy())
    if winning_numbers_counter(bet_numbers, random_lotto_numbers) == 6:
        break

sum_of_money_spent = cost_of_one_bet * how_many_times_played

print(f'We won after this many games: {how_many_times_played:,}')
print(f'We lost this amount of money: {sum_of_money_spent:,}')
