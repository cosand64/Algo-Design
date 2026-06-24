

# def convert_farenheit_to_celcius(f):
#     c = (f - 32) * 5 / 9
#     return c

# def map_data(map_function, data):
#     mapped_data = []
#     for d in data:
#         mapped_data.append(map_function(d))

#     return mapped_data

# def filter_function():
#     pass


# def main():
    # temperatures = [-43, -23, 0, 32, 85, 100, 212]
    # celsius_temperatures = map_data(convert_farenheit_to_celcius, temperatures)

    # print(celsius_temperatures)

    # odd_values = list(filter (lambda n : n % 2, list(range(0, 1000) )))
    # print(odd_values)

divisible_by_three = list(map(lambda n : n % 3 == 0, list(range(100))))

for i in range(100):
    print(f'{i} : {divisible_by_three[i]}')

# all prime numbers between two numbers, 100 and 200
import math
def is_prime(number):
    for n in range(2, int(math.sqrt(number) + 1)):
        if number % n == 0:
            return False
        
    return True

prime_list = list(filter(is_prime, list(range(100, 201))))
print(prime_list)

import functools

# Summation of a list of numbers

numbers = list(range(10))

summation = functools.reduce(lambda total, current : total + current, numbers)
print(summation)

factorial = functools.reduce(lambda total, current : total * current, numbers)
print(factorial)
