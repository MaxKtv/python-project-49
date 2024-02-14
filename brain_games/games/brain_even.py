from random import randint


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_number_even(number):
    return number % 2 == 0


def check_task_solution():
    random_number = randint(1, 100)
    if is_number_even(random_number) is True:
        solution = 'yes'
    else:
        solution = 'no'
    return random_number, solution
