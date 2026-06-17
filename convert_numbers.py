

def get_number():
    """Obtain a positive integer from the user"""
    
    while True:
        try:
            integer = int(input("Please enter a positive integer. "))
            if integer > 0:
                return integer
            else:
                print("Please try again. ")
        except ValueError:
            print("Must input a number.")
    

def convert_to_binary(number):
    """Recieves a number in decimal and converts it to a binary string"""
    binary_digits = []
    while number > 0:
        binary_digits.append(number % 2)
        number = number // 2
    
    binary_string = ""
    for i in range(len(binary_digits)-1, -1, -1):
        binary_string = binary_string + str(binary_digits[i])
    return binary_string

def convert_to_octal(number):
    """Recieves a number in decimal and converts it to a octal string"""
    octal_digits = []
    while number > 0:
        octal_digits.append(number % 8)
        number = number // 8
    
    octal_string = ""
    for i in range(len(octal_digits)-1, -1, -1):
        octal_string = octal_string + str(octal_digits[i])
    return octal_string

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
    
    assert convert_to_binary(1) == '1'
    assert convert_to_binary(10) == '1010'
    assert convert_to_binary(13) == '1101'
    assert convert_to_binary(14) == '1110'
    assert convert_to_binary(15) == '1111'
    assert convert_to_binary(16) == '10000'
    assert convert_to_binary(255) == '11111111'
    assert convert_to_binary(256) == '100000000'
    
    print('all binary tests passed')

def test_octal():
    """run tests to ensure convert_to_octal() is working"""
    assert convert_to_octal(1) == '1' 
    assert convert_to_octal(10) == '12' 
    assert convert_to_octal(11) == '13' 
    assert convert_to_octal(12) == '14' 
    assert convert_to_octal(800) == '1440'

    print('all octal tests have passed') 

def test_hex():
    """run tests to ensure convert_to_hex() is working"""
    pass 

def test_running():
   test_binary()
   test_octal()
   test_hex()

def main():
    """run the program"""
    test_binary()
    test_octal()

    number = get_number()

    binary_number = convert_to_binary(number)
    octal_number = convert_to_octal(number)

    print(number)
    print(binary_number)
    print(octal_number)
  

main()