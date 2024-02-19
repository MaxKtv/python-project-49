import prompt


def greet_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n').capitalize()
    print(f'Hello, {name}!')
    return name


def run_game(game):
    name = greet_user()
    count = 0
    print(game.task)
    while count <= 2:
        question, solution = game.check_task_solution()
        answer = prompt.string(f'Question: {question}\n'
                               f'Your answer: ')
        if answer == str(solution):
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
        else:
            print(f"'{answer}' is a wrong answer ;(. "
                  f"Correct answer was '{solution}'.\n"
                  f"Let's try again, {name}!")
            break
