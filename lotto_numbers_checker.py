""" lotto multi-multi numbers checker - check if you won"""
"""
Input:
Lotto numbers of the day
Plus number
Percent of additional winning (50 = 50%)
Your numbers (with PLUS or NORMAL)
write GO to finalize

Input example:
1 4 7 16 29 30 33 36 38 39 54 58 62 66 71 72 73 74 77 80
7
50
PLUS
25 27 31 46 47 63 65 72 76
8 9 10 36 37 39 50 59 69
4 14 15 25 26 36 37 47 48
NORMAL
8 9 17 26 35 44 53 62 71
PLUS
25 27 31 46 47 63 65 72 76
8 9 10 36 37 39 50 59 69
NORMAL
4 14 15 25 26 36 37 47 48
GO
"""
WINNINGS_WITHOUT_PLUS = [
    [4],
    [0, 16],
    [0, 2, 54],
    [0, 2, 8, 84],
    [0, 0, 4, 20, 700],
    [0, 0, 2, 8, 120, 1300],
    [0, 0, 2, 4, 20, 200, 6000],
    [0, 0, 0, 4, 20, 60, 600, 22000],
    [0, 0, 0, 2, 8, 42, 300, 2000, 70000],
    [0, 0, 0, 2, 4, 12, 140, 520, 10000, 250000]
]
WINNINGS_WITH_PLUS = [
    [88],
    [24, 120],
    [18, 28, 214],
    [16, 16, 48, 384],
    [14, 10, 20, 80, 1800],
    [14, 10, 12, 20, 320, 4300],
    [14, 8, 8, 14, 70, 700, 22000],
    [14, 4, 4, 14, 48, 180, 1800, 130000],
    [14, 4, 4, 6, 22, 122, 900, 10000, 300000],
    [10, 4, 4, 6, 12, 36, 380, 1520, 50000, 2500000]
]
COST_OF_NORMAL_BET = 2.5
COST_OF_PLUS_BET = 5


def hit_numbers_counter(chosen_numbers, given_lotto_numbers):
    return len(chosen_numbers & given_lotto_numbers)


def check_if_plus_hit(chosen_numbers, plus_number_from_lotto):
    if plus_number_from_lotto in chosen_numbers:
        return "PLUS"
    else:
        return ""


def generate_int_set_from_given_list(given_list):
    numbers = []
    for num in given_list:
        if num.isdigit():
            numbers.append(int(num))
    return set(numbers)


print('Paste: \nLotto numbers\nPlus number\nPercent added to winnings\nNumbers separated by enter')
line_lotto = input()
lotto_numbers = generate_int_set_from_given_list(line_lotto.strip().split(' '))
plus_number = int(input())
percent_addition = int(input()) / 100
is_normal = False
total_cost_of_bets = 0
total_winning_money = 0
hits_list = []
i = 0
add_to_win = []
while True:
    my_numbers = {}
    line = input().strip()
    if line == 'GO':
        break
    if line.upper() == 'NORMAL':
        is_normal = True
        continue
    elif line.upper() == 'PLUS':
        is_normal = False
        continue
    else:
        nums = line.split()
        my_numbers = generate_int_set_from_given_list(nums)
    hits_list.append(hit_numbers_counter(my_numbers, lotto_numbers))
    number_of_chosen_numbers = len(my_numbers)
    if is_normal:
        total_cost_of_bets += COST_OF_NORMAL_BET
    else:
        total_cost_of_bets += COST_OF_PLUS_BET
    won_value = 0
    if hits_list[i] > 0:
        if plus_number in my_numbers and not is_normal:
            won_value = WINNINGS_WITH_PLUS[number_of_chosen_numbers - 1][hits_list[i] - 1]
        else:
            won_value = WINNINGS_WITHOUT_PLUS[number_of_chosen_numbers - 1][hits_list[i] - 1]
        won_value += won_value * percent_addition
    add_to_win.append(won_value)
    total_winning_money += add_to_win[i]
    i += 1
print(f'Total cost of bets: {total_cost_of_bets} PLN')
print(f'Total winnings: {total_winning_money} PLN')
print('RESULTS:')
pos = 0
for hits in hits_list:
    print(f'{pos + 1}. {hits_list[pos]} hits --> won {add_to_win[pos]} PLN')
    pos += 1
