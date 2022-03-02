""" Lotto game """
import random
import typing


def winning_numbers_counter(picked_numbers: typing.Set[int],
                            random_numbers: typing.Set[int]) -> int:
    """ Returns number of numbers that are the same in random number list
    :param picked_numbers: {1,3,22,11,38,40]
    :param random_numbers: [38,22,5,7,8,9]
    :return: 2
    """
    numbers_hit = len(picked_numbers & random_numbers)
    return numbers_hit

def random_numbers_generator():
    return



if __name__ == '__main__':
    how_many_times_played = 0
    cost_of_one_bet = 3
    bet_numbers = {3, 8, 40, 49, 22, 1}
    base_number_table = range(1, 50)
    random_lotto_numbers = []
    while bet_numbers != random_lotto_numbers:
        how_many_times_played += 1
        random_lotto_numbers = set(random.sample(base_number_table, k=6))

    sum_of_money_spent = cost_of_one_bet * how_many_times_played

    print(f'We won after this many games: {how_many_times_played:,}')
    print(f'We lost this amount of money: {sum_of_money_spent:,}')
