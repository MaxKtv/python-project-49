from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    return number % 2 == 0


def generate_qns():
    random_number = randint(1, 100)
    if is_number_even(random_number):
        solution = 'yes'
    else:
        solution = 'no'
    return random_number, solution
