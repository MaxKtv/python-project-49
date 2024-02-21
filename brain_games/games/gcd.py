from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def get_right_divisor(random_number1, random_number2):
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 > random_number2:
            random_number1 %= random_number2
        else:
            random_number2 %= random_number1
    divisor = random_number1 + random_number2
    return divisor


def generate_qns():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = f'{random_number1} {random_number2}'
    solution = get_right_divisor(random_number1, random_number2)
    return question, solution