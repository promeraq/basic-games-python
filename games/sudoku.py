import random

# Print the game board
def printBoard(board, size):
    # First line of "_" to separate numbers with game's spots
    for row in range(size):
        line = "+--------+"
        if row == 0 or row == 3 or row == 6:
            for col in range(size//4):
                line = line + "--------+" 
            print(line)

        # Print game spots
        line = ''
        for col in range(size):
            line = line + "| " + str(board[row][col])
        print(line + "|")
    
    # First line of "_" to separate numbers with game's spots
    for row in range(size//3):
        line = "+--------+"
        if row == 0:
            for col in range(size//4):
                line = line + "--------+" 
            print(line)
    print()


# See if there are empty spaces yet
def space(board, size):
    for x in range(size):
        for y in range(size):
            if board[x][y] == 0:
                return x, y
    # If all the board is full
    return None, None
  

# First constraint that we must respect: Each number appears only once in each square (3x3)
def constraint_square(board, num, row, col):
    # If we divide by 3 and throw away the remainder:
    # we'll get 0 for square1, 1 for square2 and 2 for square3.
    # Multiplying by 3 we get first row and col of each square.
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for x in range(start_row, start_row + 3):
        for y in range(start_col, start_col + 3):
            if board[x][y] == num:
                return False
    return True


# Second constraint that we must respect: Each number appears only once in each line (1x9)
def constraint_line(board, new_number, row, col):
    # Safe all numbers of a row in a list. If our num it's inside, it isn't valid.
    row_values = board[row]
    if new_number in row_values:
        return False

    # For columns, it's different. 
    # We have to move along each row, using same index (col) in it.
    col_values = []
    for r in range(9):
        col_values.append(board[r][col])
    # Same with list comprehension    
    # col_values = [board[r][col] for r in range(9)]
    if new_number in col_values:
        return False
        
    return True


def sudoku(board, size):
    # First of all, find empty spaces to play
    row, col = space(board, size)
    # If there's not a free space, we are finished, return True
    if row is None:
        return True
    
    # Otherwise...we have to add a number. We iterate over all possible numbers
    for num in range(1, 10):
        # Is this number valid? For that it has to pass 2 constraints
        const1 = constraint_square(board, num, row, col)
        const2 = constraint_line(board, num, row, col)
        if const1 == True and const2 == True:
            # if it IS valid, add it and check recursively if sudoke is solved,
            # and if it isn't solved, it will keep on solving.
            board[row][col] = num
            if sudoku(board, size):
                return True
        
        # if num ISN'T valid, overwrite with 0
        board[row][col] = 0
    
    return False


if __name__== '__main__':
    size = 9
    board = [[0 for y in range(size)] for x in range(size)]
    game_board = [
        [5, 3, 0,  0, 7, 0,  0, 0, 0],
        [6, 0, 0,  1, 9, 5,  0, 0, 0],
        [0, 9, 8,  0, 0, 0,  0, 6, 0],

        [8, 0, 0,  0, 6, 0,  0, 0, 3],
        [4, 0, 0,  8, 0, 3,  0, 0, 1],
        [7, 0, 0,  0, 2, 0,  0, 0, 6],
        
        [0, 6, 0,  0, 0, 0,  2, 8, 0],
        [0, 0, 0,  4, 1, 9,  0, 0, 5],
        [0, 0, 0,  0, 8, 0,  0, 7, 9]
        ]

    print(sudoku(board, size))
    printBoard(board, size)    
    

    # In case you wanna solve another sudoku:
    print("Let's solve that sudoku!")
    print("Add all the numbers of the matrix, from left to right, if you don't have that number write 0")
    for row in range(9):
        print("Write all the numbers of row " + str(row) + ":")
        for col in range(9):
            num = int(input())
            board[row][col] = num
    print(sudoku(board, size))
    printBoard(board, size)