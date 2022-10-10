# Zadanie 1
def greet_user(name: str, surname: str) -> str:
    return 'Czesć {} {}'.format(name, surname)


greeting = greet_user('Karol', 'Stawowski')

print(greeting)

# Zadanie 2


def multiply(num1: int, num2: int) -> int:
    return num1 * num2

# Zadanie 3


def is_even(number: int) -> bool:
    return number % 2 == 0


is_number_even = is_even(3)

print('Liczba parzysta') if is_number_even else print('Liczba nieparzysta')

# Zadanie 4


def check_numbers(num1: int, num2: int, num3: int) -> bool:
    return num1 + num2 >= num3

# Zadanie 5


def includes_value(numbers: list, number: int) -> bool:
    return number in numbers

# Zadanie 6


def do_some_magic_with_lists(numbers1: list, numbers2: list) -> list:
    numbers = numbers1 + numbers2
    numbers = list(set(numbers))
    return [number ** 3 for number in numbers]
