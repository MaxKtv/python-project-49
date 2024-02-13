import random
import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your Name?\n')
print(f'Hello, {name.capitalize()}!')
print('Answer "yes" if given number is prime. Otherwise answer "no".')


def random_generator():
    return random.randint(1, 100)


def is_prime():
    number = random_generator()
    step = 2
    while number % step != 0:
        step += 1
        if number == 1:
            return True, number
    return step == number, number


def main():
    count = 0
    while count <= 3:
        result, random_number = is_prime()
        answer = prompt.string(f'Question: {random_number}\n')
        print(f'Your answer is: {answer}')
        if (result is True and answer == 'yes') or (result is False and answer == 'no'):
            print('Correct!')
            count += 1
            if count > 2:
                print(f'Congratulations, {name.capitalize()}!')
                break
        elif result is True and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name.capitalize()}!")
            break
        elif result is False and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name.capitalize()}!")
            break


if __name__ == '__main__':
    main()
