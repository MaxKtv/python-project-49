from random import randint


TASK = 'What number is missing in the progression?'
DESIRED_LENGTH_PROGRESSION = 10
FROM_NUMBER, TO_NUMBER = 1, 100
STEP_FROM, STEP_TO = 1, 10


def get_progression(number_progression, step):
    progression = []
    while len(progression) < DESIRED_LENGTH_PROGRESSION:
        progression.append(number_progression)
        number_progression += step
    missing_progression = randint(1, len(progression) - 1)
    progression[missing_progression] = str('..')
    solution = progression[missing_progression - 1] + step
    progression = ' '.join(str(i) for i in progression)
    return progression, solution


def generate_qns():
    number_progression = randint(FROM_NUMBER, TO_NUMBER)
    step = randint(STEP_FROM, STEP_TO)
    question, solution = get_progression(number_progression, step)
    return question, solution
