def greet_user(name: str, surname: str) -> str:
    return 'Czesć {} {}'.format(name, surname)


greeting = greet_user('Karol', 'Stawowski')

print(greeting)
