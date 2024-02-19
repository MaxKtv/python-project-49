from random import randint

task = 'Find the greatest common divisor of given numbers.'


def right_divisor(random_number1, random_number2):
    if random_number1 == random_number2:
        divisor = random_number1
        return divisor
    elif random_number1 % random_number2 == 0:
        divisor = 1
        return divisor
    else:
        while random_number1 != 0 and random_number2 != 0:
            if random_number1 > random_number2:
                random_number1 %= random_number2
            else:
                random_number2 %= random_number1
        divisor = random_number1 + random_number2
        return divisor


def check_task_solution():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = f'{random_number1} {random_number2}'
    solution = right_divisor(random_number1, random_number2)
    return question, solution
