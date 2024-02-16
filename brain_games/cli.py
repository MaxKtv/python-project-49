import prompt


def welcome_user():
    name = prompt.string('May I have your Name?\n')
    print(f'Hello, {name.capitalize()}!')
