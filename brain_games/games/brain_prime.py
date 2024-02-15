from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    step = 2
    while number % step != 0:
        step += 1
        if number == 1:
            return True, number
    return step == number


def check_task_solution():
    random_number = randint(1, 100)
    if is_prime_number(random_number) is True:
        solution = 'yes'
    else:
        solution = 'no'
    return random_number, solution
