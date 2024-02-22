from random import randint, choice


TASK = 'What is the result of the expression?'
FROM_NUMBER, TO_NUMBER = 1, 100


def get_operator_n_result(random_number1, random_number2):
    operator = choice(["-", "+", "*"])
    if operator == "+":
        result = random_number1 + random_number2
    elif operator == "-":
        result = random_number1 - random_number2
    elif operator == "*":
        result = random_number1 * random_number2
    return result, operator


def generate_qns():
    random_number1 = randint(FROM_NUMBER, TO_NUMBER)
    random_number2 = randint(FROM_NUMBER, TO_NUMBER)
    solution, operator = get_operator_n_result(random_number1, random_number2)
    question = f'{random_number1} {operator} {random_number2}'
    return question, solution
