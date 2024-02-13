import random
import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your Name?\n')
print(f'Hello, {name.capitalize()}!')
print('What number is missing in the progression?')


def random_generator():
    return random.randint(1, 100)


def build_progression():
    step = random.randint(1, 10)
    number_progression = random_generator()
    progression = []
    while len(progression) < 10:
        progression.append(number_progression)
        number_progression += step
    progression[random.randint(2, len(progression) - 1)] = '. .'
    return progression, step


def main():
    count = 0
    while count <= 3:
        progression, step = build_progression()
        answer = prompt.string(f'Question: {progression}\n')
        print(f'Your answer is: {answer}')
        if int(answer) == step:
            count += 1
            print('Correct!')
            if count > 2:
                print(f'Congratulations, {name.capitalize()}!')
                break
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{step}'.\n"
                  f"Let's try again, {name.capitalize()}!")
            break


if __name__ == '__main__':
    main()
