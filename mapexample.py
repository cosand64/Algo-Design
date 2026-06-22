

def convert_farenheit_to_celcius(f):
    c = (f - 32) * 5 / 9
    return c

def map_data(map_function, data):
    mapped_data = []
    for d in data:
        mapped_data.append(map_function(d))

    return mapped_data

def filter_function():
    pass

def main():
    temperatures = [-43, -23, 0, 32, 85, 100, 212]
    celsius_temperatures = map_data(convert_farenheit_to_celcius, temperatures)

    print(celsius_temperatures)

    odd_values = list(filter (lambda n : n % 2, list(range(0, 1000) )))
    print(odd_values)

main()