import math
import random


# Randomly choose the cells where the bombs are hidden.
# If the player selects a cell with a bomb he/she loses.
# If not, all the places where zeros were hidden, are discovered.

# 1.- Print the board. The board we created is a list of lists. Each list is a row.
# Draw the grid and numbers so it's easier to play. Start with 4 x 4.
# We should print a different board of the one created each game, so the player only
# sees the digged spots.
def printBoard(board, size):
    # Print the first line of numbers:
    print()
    line = " " # 3 blank spots
    for i in range(size):
        line = line + "  " + str(i)
    print(line)   

    for row in range(size):
        # First line of "_" to separate numbers with game's spots
        line = "___"
        if row == 0:
            for col in range(size):
                line = line + "___" 
            print(line)

        # Print game spots
        line = str(row)
        for col in range(size):
            line = line + " |" + str(board[row][col])
        print(line + " |") 

    print()

# 2.- Initialize a set to keep track of the spots we've uncovered and print each time the board.
# The tuples will be: (row, col)
def uncovered(game_board, player_board, xpos_player, ypos_player):
    unc = set()
    if game_board[xpos_player][ypos_player] != "*" and player_board[xpos_player][ypos_player] == ' ':
        unc.add(xpos_player,ypos_player)
    else:
        print("That's not a valid spot. Try again")
        uncovered(game_board, player_board)
    printBoard(player_board)

# 3.- Create a board with bombs
def add_bombs(game_board, size, num_bombs):
    bombs = 0
    while bombs < num_bombs:
        bomb_loc = random.randint(0, size**2 - 1)
        row = bomb_loc // size
        col = bomb_loc % size
        if game_board[row][col] == '*':
            continue
        else:
            game_board[row][col] = '*'
            bombs += 1
    return game_board  

# 4.- Assign the nums to the board's empty spaces (0-8)
def add_numbers(game_board, size):
    num = 0
    for row in range(size):
        for col in range(size):
            if game_board[row][col] == '*':
                continue
            game_board[row][col] = countNearBombs(row, col, game_board, size)
            
    return game_board

def countNearBombs(row, col, game_board, size):
    num = 0
    for r in range(max(0, row-1), min(((row+1)+1), size)):
        for c in range(max(0, col-1), min(((col+1)+1), size)):
            if r == row and c == col:
                continue
            elif game_board[r][c] == "*":
                num += 1
    return num


# 5.- Dig at location, return True if valid dig or False if bomb found.
     # If True, dig neighbours until another bomb is found.
def dig(xpos_player, ypos_player, game_board, flag):
    if game_board[xpos_player][ypos_player] == "*" and flag != 'f':
        return False
    else:
        return True

# 6.- Recursive digging to play the game if we didn't find a bomb
def rec_dig(xpos_player, ypos_player, flag, game_board, player_board, size):
    # if our position it's equal to 0, copy that spot into players board,
    # and keep on digging around.
    if game_board[xpos_player][ypos_player] == 0:
        # Start digging around. Be carefull with index errors. Use max and min for that.
        for r in range(max(0, xpos_player-1), min(((xpos_player+1)+1), size)):
            for c in range(max(0, ypos_player-1), min(((ypos_player+1)+1), size)):
                if r == xpos_player and c == ypos_player:
                    continue
                elif game_board[r][c] == 0 and player_board[r][c] != game_board[r][c]:
                    # uncovered(game_board, player_board, xpos_player, ypos_player)
                    player_board[r][c] = game_board[r][c]
                    rec_dig(r, c, flag, game_board, player_board, size)
                else:
                    # uncovered(game_board, player_board, xpos_player, ypos_player)
                    player_board[r][c] = game_board[r][c]
    # if our position is different to 0, copy that spot into players board,
    # print it and keep on playing/asking the player to choose new positions.       
    elif game_board[xpos_player][ypos_player] != 0:
        player_board[xpos_player][ypos_player] = game_board[xpos_player][ypos_player]    

# 7.- Show victory if no more digging options
def victory(game_board, player_board, num_bombs):
    num = 0
    for row in range(size):
        for col in range(size):
            if game_board[row][col] == '*' and player_board[row][col] == 'f':
                num += 1
    if num == num_bombs:
        print('\nYOU WON!!!!!')  
        return True
    else:
        return False


# 8.- Main
if __name__=="__main__":
    size = 4
    num_bombs = 4
    # This creates an array of smaller arrays to represent a 2D Matrix.
    # Player board is the board that the player is gonna see
    player_board = [[' ' for y in range(size)] for x in range(size)]
    # Game board is the board created at the beginning
    game_board = [[' ' for y in range(size)] for x in range(size)]
    game_board = add_bombs(game_board, size, num_bombs)
    game_board = add_numbers(game_board, size)
    
    printBoard(game_board, size)
    digging = True
    vic = False
    while digging and not vic:
        printBoard(player_board, size)
        xpos_player = int(input("Write x position: "))
        ypos_player = int(input("Write y position: "))
        flag = input("Write f for flag, rest will be ignored: ")
        digging = dig(xpos_player, ypos_player, game_board, flag)
        if flag == 'f':
            player_board[xpos_player][ypos_player] = 'f'
            vic = victory(game_board, player_board, num_bombs)
            continue
        else:
            rec_dig(xpos_player, ypos_player, flag, game_board, player_board, size)
            vic = victory(game_board, player_board, num_bombs)
    if vic == False:
        print("\n\nYou lost!!!")
    printBoard(game_board, size)