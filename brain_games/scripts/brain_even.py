#!/usr/bin/env python3
import random
import prompt

name = prompt.string('May I have your Name?\n')


def welcome_user():
    print(f'Hello, {name.capitalize()}!')


welcome_user()

print('Answer "yes" if the number is even, otherwise answer "no".')


def random_generator():
    return random.randint(1, 100)


def is_number_even(number):
    return number % 2 == 0


def main():
    count = 0
    while count <= 3:
        random_number = random_generator()
        answer = prompt.string(f'Question: {random_number}\n')
        if ((is_number_even(random_number) is True and answer == 'yes') or
                (is_number_even(random_number) is False and answer == 'no')):
            print('Correct!')
            count += 1
            if count > 2:
                print(f'Congratulations, {name.capitalize()}!')
                break
        elif is_number_even(random_number) is True and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name.capitalize()}!")
            break
        elif is_number_even(random_number) is False and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name.capitalize()}!")
            break


if __name__ == '__main__':
    main()
