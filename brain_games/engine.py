import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n').capitalize()
    print(f'Hello, {name}!')
    count = 3
    print(game.TASK)
    while count > 0:
        question, solution = game.generate_qns()
        answer = prompt.string(f'Question: {question}\n'
                               f'Your answer: ')
        if answer == str(solution):
            print('Correct!')
            count -= 1
            if count == 0:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is a wrong answer ;(. "
                  f"Correct answer was '{solution}'.\n"
                  f"Let's try again, {name}!")
            count -= 3
