

def get_number():
    """Obtain a positive integer from the user"""
    return 123

def convert_to_binary(number):
    """Recieves a number in decimal and converts it to a binary string"""
    return "0b11011"

def convert_to_octal(number):
    """Recieves a number in decimal and converts it to a octal string"""
    return "0o357"

def convert_to_hex(number):
    """Recieves a number in decimal and converts it to a hex string"""
    return "0bEF"

def convert(number):
    """Call functions to convert number to binary, octal and hexadecimal"""
    binary = convert_to_binary(number)
    octal = convert_to_octal(number)
    hex = convert_to_hex(number)

    return binary, octal, hex

def display(number, binary, octal, hex):
    """display number and its conversions"""
    print(f"decimal: {number}, binary: {binary}, octal: {octal}, hex: {hex}")

def test_binary():
    """run tests to ensure convert_to_binary() is working"""
    pass 

def test_octal():
    """run tests to ensure convert_to_octal() is working"""
    pass 

def test_hex():
    """run tests to ensure convert_to_hex() is working"""
    pass 

def test_running():
   test_binary()
   test_octal()
   test_hex()

def main():
    """run the program"""
    number = get_number()
    binary, octal, hex = convert(number)
    display(number, binary, octal, hex)

main()