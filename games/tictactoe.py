import random

def printBoard(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
        
def print_board_nums():
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
        print('| ' + ' | '.join(row) + ' |')


def initiateGame(board):
    print('You have to choose: x or o')
    player = str(input())
    if player == 'x':
        comp = 'o'
        print('You will start')
    elif player == 'o':
        comp = 'x'
        print ('The computer will start')
    else:
        print("That is not an option. Let's start again...\n\n")
        initiateGame(board)
    print_board_nums()
    return player, comp


def available(board):
    pos_player = int(input("\nChoose the position from 0 to 8: "))
    if board[pos_player] != ' ':
        print("Not available.")
        pos_player = available(board)
    return pos_player


def availableComputer(board):
    pos_computer = random.randint(0, 8)
    if board[pos_computer] != ' ':
        pos_computer = availableComputer(board)
    return pos_computer


def game(board, player, comp):
    if player == 'x':
        turn = True
    else:
        turn = False
    gamerunning = True
    games = board.count(' ')
    while gamerunning == True:
        print("\n")
        printBoard(board)
        if turn == True:
            turn = False
            pos_player = available(board)
            board[pos_player] = player
            # winner, gamerunning = winnerGame(board, player)
            winner, gamerunning = winnerGG(pos_player, board, player)
            games = board.count(' ')
            if games == 0:
                gamerunning = False
                winner = "Tie"
        elif turn == False:
            turn = True
            pos_computer = availableComputer(board) 
            board[pos_computer] = comp
            # winner, gamerunning = winnerGame(board, comp)
            winner, gamerunning = winnerGG(pos_computer, board, comp)
            games = board.count(' ')
            if games == 0:
                gamerunning = False
                winner = 'Tie'
    return winner

def winnerGG(position, board, letter):
    gamerunning = True
    winner = None
    # winner if 3 in a row anywhere. First we check the row.
    # Since we have 3 columns, we'll know the row we're at
    # by dividing the position of the player by 3 and rounding it down
    # row will be a list.
    # "if all" means --> if everything in this list is true
    # 1.- Check the rows
    row_index = position // 3
    # Get a list with the complete row
    row = board[row_index*3 : (row_index + 1)*3]
    if all([spot == letter for spot in row]):
        winner = letter
        gamerunning = False
        return winner, gamerunning
    # 2.- Check the columns
    # To get the column divide by 3 and get the leftover
    col_index = position % 3
    column = [board[col_index+i*3] for i in range(3)]
    if all([spot == letter for spot in column]):
        winner = letter
        gamerunning = False
        return winner, gamerunning
    # 3.- Check the diagonals
    # Since the possible positions for diagonals are even numbers (0,2,4,6,8)
    if position % 2 == 0:
        diagonal1 = [board[i] for i in [0, 4, 8]]
        if all ([spot == letter for spot in diagonal1]):
            winner = letter
            gamerunning = False
            return winner, gamerunning
        diagonal2 = [board[i] for i in [0, 4, 6]]
        if all ([spot == letter for spot in diagonal2]):
            winner = letter
            gamerunning = False
            return winner, gamerunning
    # if all this fails
    return winner, gamerunning


if __name__ == '__main__':
    board = [' ' for _ in range(9)]
    print('Lets play Tic Tac Toe!')
    player, comp = initiateGame(board)
    winner = game(board, player, comp)
    printBoard(board)
    print("\nThe winner is: ", winner)