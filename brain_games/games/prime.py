from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number):
    step = 2
    while number % step != 0:
        step += 1
        if number == 1:
            return True
    return step == number


def generate_qns():
    random_number = randint(1, 100)
    if is_prime_number(random_number):
        solution = 'yes'
    else:
        solution = 'no'
    return random_number, solution
