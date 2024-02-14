from random import randint, choice


task = 'What is the result of the expression?'


def random_operator():
    operator = ["-", "+", "*"]
    return choice(operator)


def operator_logic(random_number1, random_number2):
    operator = random_operator()
    if operator == "+":
        result = random_number1 + random_number2
    elif operator == "-":
        result = random_number1 - random_number2
    elif operator == "*":
        result = random_number1 * random_number2
    return result, operator


def check_task_solution():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    solution, operator = operator_logic(random_number1, random_number2)
    question = f'{random_number1} {operator} {random_number2}'
    return question, solution
