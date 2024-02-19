from random import randint


task = 'What number is missing in the progression?'


def check_task_solution():
    step = randint(1, 10)
    number_progression = randint(1, 100)
    progression = []
    while len(progression) < 10:
        progression.append(number_progression)
        number_progression += step
    missing_progression = randint(1, len(progression) - 1)
    progression[missing_progression] = str('..')
    solution = progression[missing_progression - 1] + step
    progression = ' '.join(str(i) for i in progression)
    return progression, solution
