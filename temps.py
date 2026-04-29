def get_temperature():
    temperature = float(input("What is the temperature? "))
    return temperature

def get_unit_type():
    while True:
        unit_type = input("What is the unit type? (k, f, c) ")
        if unit_type.lower() == "k" or unit_type.lower() == "f" or unit_type.lower() == "c":
            return unit_type.lower()

def convert_temperature_to_celcius(temperature, unit_type):
    if unit_type == "c":
        return temperature
    elif unit_type == "k":
        pass
    else:
        pass