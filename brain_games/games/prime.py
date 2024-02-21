from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    step = 2
    if number <= 1:
        return 'no'
    while step < number:
        if number % step == 0:
            return 'no'
        step += 1
    return 'yes'


def generate_qns():
    random_number = randint(1, 100)
    solution = is_prime_number(random_number)
    return random_number, solution
