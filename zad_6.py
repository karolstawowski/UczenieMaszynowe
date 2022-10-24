def do_some_magic_with_lists(numbers1: list, numbers2: list) -> list:
    numbers = numbers1 + numbers2
    numbers = list(set(numbers))
    return [number ** 3 for number in numbers]
