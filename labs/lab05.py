# 1. Name:
#      Connor sanderson
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-
import json

def load_board(filename):
    try:
        with open(filename, 'rt') as file:
            data = json.load(file)
            if 'board' in data:
                return data['board']
            return data
    except FileNotFoundError:
        print(f'error: {filename} not found')
        return None
    
def display_board(board):
    """ Displays the current board """
    print("   A B C D E F G H I")
    for i in range(9):
        if i == 3 or i == 6:
            print("   -----+-----+-----")
        row_number = f"{i + 1}  "
        
        for j in range(9):
            value = board[i][j]
            value_string = str(value) if value != 0 else ' '
            row_number += value_string

            if j == 2 or j == 5:
                row_number += '|'
            elif j == 8:
                row_number += ' '

        print(row_number)

def save_board(filename, board):
    """ Saves the current board """
    with open(filename, 'w') as file:
        json.dump({"board": board}, file)
    print(f"Board successfully saved to {filename}")

def get_user_input():
    """ Prompts the user for a coordinate. """
    return input("Specify a coordinate to edit or 'Q' to save and quit\n> ")

def parse_coordinates(coordinate_string):
    """
    Parses the user input ('B8') into integer row and column indices (0-8).
    Returns 'Q' if the user wants to quit, or False if invalid.
    """
    coordinate = coordinate_string.strip().upper()
    
    if coordinate == 'Q':
        return 'Q'
        
    if len(coordinate) != 2:
        return False
        
    column_character = coordinate[0]
    row_number = coordinate[1]
    
    if not ('A' <= column_character <= 'I') or not ('1' <= row_number <= '9'):
        column_character = coordinate[1]
        row_number = coordinate[0]
        
    column = ord(column_character) - ord('A')
    row = int(row_number) - 1
    
    return row, column

def is_square_filled(board, row, column):
    """ Checks if a square is already filled """
    return board[row][column] != 0

def validate_move(board, row, col, value):
    """ Checks if a move is valid """
    # Check if the target cell is filled
    if is_square_filled(board, row, col):
        return False

    # Check the row
    for col in range(9):
        if board[row][col] == value:
            return False

    # Check the column
    for r in range(9):
        if board[r][col] == value:
            return False

    # Check the 3x3
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3

    for r in range(box_start_row, box_start_row + 3):
        for col in range(box_start_col, box_start_col + 3):
            if board[r][col] == value:
                return False

    # If all checks passed
    return True

def play_game(board):
    """ Main game loop """
    while True:
        display_board(board)
        user_input = get_user_input()
        parsed = parse_coordinates(user_input)
        
        if parsed == 'Q':
            break
        elif parsed is False:
            print("ERROR: Invalid coordinate format. Please use format like 'A1' or 'B8'.")
            continue
            
        row, col = parsed
        
        # Prompt for a number to place
        val_str = input(f"What number goes in {user_input.strip().upper()}? ")
        try:
            val = int(val_str)
            if not (1 <= val <= 9):
                print("ERROR: Value must be a number between 1 and 9.")
                continue
        except ValueError:
            print("ERROR: Invalid number.")
            continue
            
        # validate move
        is_legal = validate_move(board, row, col, val)
        
        if not is_legal:
            print("This move is not valid.")
        
        board[row][col] = val

def main():
    filename = input("Enter the filename of the Sudoku: ")
    board = load_board(filename)
    
    if board is not None:
        play_game(board)
        
        save_filename = input("Enter filename to save the board (or press Enter to overwrite): ")
        if save_filename.strip() == "":
            save_filename = filename
            
        save_board(save_filename, board)


main()