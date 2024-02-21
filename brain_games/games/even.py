from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_qns():
    random_number = randint(1, 100)
    solution = is_number_even(random_number)
    return random_number, solution
