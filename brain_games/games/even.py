from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
FROM_NUMBER, TO_NUMBER = 1, 100


def is_number_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def generate_qns():
    random_number = randint(FROM_NUMBER, TO_NUMBER)
    solution = is_number_even(random_number)
    return random_number, solution
