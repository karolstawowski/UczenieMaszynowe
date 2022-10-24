def print_names(names):
    for name in names:
        print(name)


def multiply_numbers(numbers):
    multiplied_numbers = []
    for number in numbers:
        multiplied_numbers.append(number * 2)

    return multiplied_numbers


def multiply_numbers(numbers):
    return [number * 2 for number in numbers]


def even_numbers(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)


def every_second_number(numbers):
    for i in range(len(numbers)):
        if i % 2 != 0:
            print(numbers[i])
