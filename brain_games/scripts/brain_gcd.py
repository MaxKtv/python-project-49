import random
import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your Name?\n')
print(f'Hello, {name.capitalize()}!')
print('Find the greatest common divisor of given numbers.')


def random_generator():
    return random.randint(1, 100)


def right_divisor(random_number1, random_number2):
    if random_number1 % random_number2 == 0:
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


def main():
    count = 0
    while count <= 3:
        random_number1 = random_generator()
        random_number2 = random_generator()
        divisor = right_divisor(random_number1, random_number2)
        answer = prompt.string(f'Question: {random_number1} {random_number2}\n')
        print(f'Your answer is: {answer}')
        if int(answer) == divisor:
            count += 1
            print('Correct!')
            if count > 2:
                print(f'Congratulations, {name.capitalize()}!')
                break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{divisor}'.\n"
                  f"Let's try again, {name.capitalize()}!")
            break


if __name__ == '__main__':
    main()
