import prompt


def welcome_user():
    name = prompt.string('May I have your Name? ')
    print(f'Hello, {name.capitalize()}!')
