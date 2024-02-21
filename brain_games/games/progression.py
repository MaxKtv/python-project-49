from random import randint


TASK = 'What number is missing in the progression?'


def get_progression(number_progression, step):
    progression = []
    while len(progression) < 10:
        progression.append(number_progression)
        number_progression += step
    missing_progression = randint(1, len(progression) - 1)
    progression[missing_progression] = str('..')
    solution = progression[missing_progression - 1] + step
    progression = ' '.join(str(i) for i in progression)
    return progression, solution


def generate_qns():
    number_progression = randint(1, 100)
    step = randint(1, 10)
    question, solution = get_progression(number_progression, step)
    return question, solution
