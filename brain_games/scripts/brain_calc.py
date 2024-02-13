import random
import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your Name?\n')
print(f'Hello, {name.capitalize()}!')
print('What is the result of the expression?')


def random_generator():
    return random.randint(1, 100)


def random_operator():
    operator = ["-", "+", "*"]
    return random.choice(operator)


def operator_logic(random_number1, random_number2):
    operator = random_operator()
    if operator == "+":
        result = random_number1 + random_number2
    elif operator == "-":
        result = random_number1 - random_number2
    elif operator == "*":
        result = random_number1 * random_number2

    return result, operator


def main():
    count = 0
    while count <= 3:
        random_number1 = random_generator()
        random_number2 = random_generator()
        result, operator = operator_logic(random_number1, random_number2)
        answer = prompt.string(f'Question: {random_number1} {operator} {random_number2}\n')
        print(f'Your answer is: {answer}')
        if int(answer) == result:
            count += 1
            print('Correct!')
            if count > 2:
                print(f'Congratulations, {name.capitalize()}!')
                break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\n"
                  f"Let's try again, {name.capitalize()}!")
            break


if __name__ == '__main__':
    main()
