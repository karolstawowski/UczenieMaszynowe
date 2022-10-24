def is_even(number: int) -> bool:
    return number % 2 == 0


is_number_even = is_even(3)

print('Liczba parzysta') if is_number_even else print('Liczba nieparzysta')
