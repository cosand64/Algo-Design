# 1. Name:
#      Connor Sanderson
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program will take a year and a month input from the user. With the month and
#      the year the program will then be able to produce what the calendar looked like 
#      for that given month.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was making sure that the call table was correct 
#      and that each function worked while getting called apon. I was not too sure how the 
#      display table function worked so I had to spend some time trying to understand it so 
#      that I could properly incorperate it into my program.
# 5. How long did it take for you to complete the assignment?
#      This took me 2hrs and 30 min

def get_month():
    '''Prompt the user for a valid month number between 1-12.'''
    while True:
        try:
            month = int(input("Enter a month number: "))
            if 1 <= month <= 12:
                return month
            else:
                print("Month must be between 1 and 12.")
        except ValueError:
            print("Month must be an integer.")

def get_year():
    '''Prompt the user for a year >= 1753. '''
    while True:
        try:
            year = int(input("Enter year: "))
            if year >= 1753:
                return year
            else:
                print("Year must be 1753 or later.")
        except ValueError:
            print("Year must be an integer.")

def is_leap_year(year):
    '''Checks to see if current year is a leap year. '''
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def number_days_in_month(month, year):
    '''Determines the number of days in a given month. '''
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
        
def compute_offset(end_month, end_year):
    '''
    This function will calculate the day of the week
    that a given month will start on. It will return
    0 for Sunday, 1 for monday and so on until it 
    6 for saturday.
    '''
    total_days = 0
    
    # count full years
    for year in range(1753, end_year):
        if is_leap_year(year):
            total_days += 366
        else:
            total_days += 365
            
    # count full months
    for month in range(1, end_month):
        days_in_month = number_days_in_month(month, end_year)
        total_days += days_in_month
        
    # determine offset
    offset = (total_days + 1) % 7
    return offset

def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline


def display_calendar(month, year):
    '''
    Calls the helper functions to determine the number of days
    in the month and the neccessary offset. Then produces 
    the calendar
    '''
    # find the number of days in the given month
    days_in_month = number_days_in_month(month, year)
    
    # determine the offset to find the starting day of the week
    offset = compute_offset(month, year)
    
    # display the calendar
    display_table(offset, days_in_month)


def main():
    month = get_month()
    year = get_year()
    display_calendar(month, year)

if __name__ == "__main__":
    main()