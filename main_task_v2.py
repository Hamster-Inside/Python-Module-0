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


def random_numbers_generator() -> typing.Set[int]:
    """

    :return: set -> collection of 6 random numbers from 1 to 49
    """
    base_number_table = range(1, 50)
    random_numbers = set(random.sample(base_number_table, k=6))
    return random_numbers


if __name__ == '__main__':
    HOW_MANY_TIMES_PLAYED = 0
    COST_OF_ONE_BET = 3
    bet_numbers = random_numbers_generator()
    HIT_3 = 0
    HIT_4 = 0
    HIT_5 = 0
    random_lotto_numbers = {}
    while bet_numbers != random_lotto_numbers:

        HOW_MANY_TIMES_PLAYED += 1
        random_lotto_numbers = random_numbers_generator()
        match (winning_numbers_counter(bet_numbers, random_lotto_numbers)):
            case 3:
                HIT_3 += 1
            case 4:
                HIT_4 += 1
            case 5:
                HIT_5 += 1

    SUM_OF_MONEY_SPENT = COST_OF_ONE_BET * HOW_MANY_TIMES_PLAYED

    print(f'We won after this many games: {HOW_MANY_TIMES_PLAYED:,}')
    print(f'We lost this amount of money: {SUM_OF_MONEY_SPENT:,}')
    print(f'How many times hit 3 nums: {HIT_3:,}')
    print(f'How many times hit 4 nums: {HIT_4:,}')
    print(f'How many times hit 5 nums: {HIT_5:,}')
