""" Lotto game """
import random
import typing


def number_table_generator(number: int = 10) -> typing.List[int]:
    """ Generate table of numbers
    :param number: 10
    :return: {1,2,3,4,5,6,7,8,9,10}
    """
    number_table = []
    for i in range(number):
        number_table.append(i + 1)
    return number_table


def lotto_machine_mixer(numbers: typing.List[int], table_of_numbers: typing.List[int]) -> int:
    """ Generator of 6 random numbers to be compared with given numbers
    :param table_of_numbers: [1,2,4,5,...,49] -> or any other table to be mixed
    :param numbers: [4,8,12,5,10,22] -> numbers we want to bet
    :return: number of the same numbers from given nums and lotto machine
    """
    randomly_mixed_numbers = []
    for _ in range(6):
        random_number = random.choice(table_of_numbers)
        randomly_mixed_numbers.append(random_number)
        table_of_numbers.remove(random_number)
    numbers_hit = len((set(numbers)) & (set(randomly_mixed_numbers)))
    return numbers_hit


how_many_times_played = 0
cost_of_one_bet = 3
bet_numbers = [3, 8, 40, 49, 22, 1]
base_number_table = number_table_generator(49)

while True:
    how_many_times_played += 1
    if lotto_machine_mixer(bet_numbers, base_number_table.copy()) == 6:
        break

sum_of_money_spent = cost_of_one_bet * how_many_times_played

print(f'We won after this many games: {how_many_times_played:,}')
print(f'We lost this amount of money: {sum_of_money_spent:,}')
