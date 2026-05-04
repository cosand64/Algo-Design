

# def get_name():
#     name = input('What is your name? ')
#     return name

# def get_gender():
#     gender = input('Are you male or female (m/f)? ')
#     return gender.lower()

# def get_prefix(gender):
#     return ('Mr.' if gender == 'm' else 'Mrs')
    
# def main():
#     name = get_name()
#     gender = get_gender()
#     prefix = get_prefix(gender)

#####################################################################

# import datetime
# year = 2026

# def years_old():
#     date_of_birth = int(input('When were you born? (yyyy) '))
#     years_old = year - date_of_birth
#     print(f'You will turn {years_old}')

# years_old()

# test = "xxx"

# print(test.count("x"))

#########################################################################

password = "drowssap"
secret = "Silly Goose"

user_password = input("what is the password? ")

if password == user_password:
    print(secret)
else:
    print("dummy")