# Zadanie a
def print_names (names):
    for name in names:
        print(name)

print('\nZadanie a')
print_names(['Ania', 'Bartek', 'Szymon', 'Adam', 'Staszek'])

# Zadanie b
def multiply_numbers (numbers):
    multiplied_numbers = []
    for number in numbers:
        multiplied_numbers.append(number * 2)
        
    return multiplied_numbers

print('\nZadanie b1')
print(multiply_numbers([4.2, 2.1, 6, 40, 0.51]))

def multiply_numbers (numbers):
    return [number * 2 for number in numbers]

print('\nZadanie b2')
print(multiply_numbers([4.2, 2.1, 6, 40, 0.51]))
        
# Zadanie c
def even_numbers (numbers):
    for i in numbers:
        if(i % 2 == 0):
            print(i)
       
print('\nZadanie c')
even_numbers(range(0,10))

# Zadanie d
def every_second_number (numbers):
    for i in range(len(numbers)):
        if(i % 2 != 0):
            print(numbers[i])
    
print('\nZadanie d')
every_second_number(range(0,10))