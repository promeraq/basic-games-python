def printBoard(board):
    # First line of "_" to separate numbers with game's spots
    for row in range(6):
        line = "+--+--+--+--+--+--+--+"
        if row == 0:
            print(line)
        # Print game spots
        line = ''
        for col in range(7):
            line = line + "| " + str(board[row][col])
        print(line + "|")
    
    # The board is almost finished.
    # We only need to print one last line of "-" and the numbers
    # of each column after that.
    for row in range(6):
        if row == 0:
            line = "+--+--+--+--+--+--+--+" 
            print(line)
        line = ''
        # Second row we print at the end, of pos_nums
        if row == 1:
            for col in range(7):
                line = line + "  " + str(col)
            print(line + " ")
            break
    print("\n")


def initiateGame(board):
    print('You have to choose: x or o')
    player1 = str(input())
    if player1 == 'x':
        player2 = 'o'
        print('Player 1 will start with x')
    elif player1 == 'o':
        player2 = 'x'
        print ('Player 2 will start with x')
    else:
        print("That is not an option. Let's start again...\n\n")
        initiateGame(board)
    return player1, player2

def ask_user():
    col = int(input(" choose the column from 0 to 6: "))
    return col

def available(board, row, col_player):
    # Last possible recursion case: row=0
    position = [row, col_player]
    if board[0][col_player] != ' ':
        print("Not available,", end='')
        col_player = ask_user()
        row = 5
        position = available(board, row, col_player)
    elif board[row][col_player] != ' ':
        position = available(board, row-1, col_player)
    return position

def game(board, player1, player2):
    if player1 == 'x':
        turn = True
    else:
        turn = False
    gamerunning = True
    while gamerunning == True:
        print(gamerunning)
        print("\n")
        printBoard(board)
        if turn == True:
            turn = False
            last_row = 5
            print("PLAYER1")
            col = ask_user()
            position = available(board, last_row, col)
            row = position[0]
            col = position[1]
            board[row][col] = player1
            winner, gamerunning = games_left(board)
            winner, gamerunning = winnerGG(row, col, board, player1)            
        elif turn == False:
            turn = True
            last_row = 5
            print("PLAYER2")
            col = ask_user()
            position = available(board, last_row, col)
            row = position[0]
            col = position[1]
            board[row][col] = player2
            winner, gamerunning = games_left(board)
            winner, gamerunning = winnerGG(row, col, board, player2)
            print(winner, gamerunning)
    return winner


def games_left(board):
    games = 0
    gamerunning = True
    winner = None
    for i in range(6):           
        games += board[i].count(' ')
    if games == 0:
        gamerunning = False
        winner = "Tie"
    return winner, gamerunning


def winnerGG(row, col, board, letter):
    gamerunning = True
    winner = None
    # winner if 4 in same row, column or diagonal anywhere. 
    # 1.- First we check the row.
    count = 0
    complete_row = board[row]
    for spot in complete_row:
        if spot == letter:
            count += 1
    if count >= 4:
        winner = letter
        gamerunning = False
        return winner, gamerunning

    # 2.- Check the column
    # To get the column divide by 3 and get the leftover
    complete_col = []
    count = 0
    for i in range(row):
        complete_col.append(board[i][col])
    for spot in complete_col:
        if spot == letter:
            count += 1
    if count >= 4:
        winner = letter
        gamerunning = False
        return winner, gamerunning
    
    # 3.- Check the diagonals
    # If we take a spot in the board, and do: x = 5 and y = row + col - 5
    # we get the starting point of one diagonal that goes throw that spot.
    count1 = 0
    start_point1 = row + col
    if start_point1 <= 5:
        try:
            for i in range(6):
                init = board[start_point1-i][0+i]
                if init == letter:
                    count1 += 1
        except IndexError:
            pass
    else:
        try:
            for i in range(6):
                init = board[5-i][start_point1-5+i]
                if init == letter:
                    count1 += 1
        except IndexError:
            pass

    # To get the other diagonal we need another formula:
    # if row - col < 0 then x = 0 and y = row - col
    # if row - col > 0 then x = row - col and y = 0
    count2 = 0
    start_point2 = row - col
    if start_point2 > 0:
        try:
            for i in range(6):
                init = board[start_point2+i][0+i]
                if init == letter:
                    count2 += 1
        except IndexError:
            pass
    else:
        try:
            for i in range(6):
                init = board[0+i][start_point2+i]
                if init == letter:
                    count2 += 1
        except IndexError:
            pass

    if count1 >= 4 or count2 >= 4:
        winner = letter
        gamerunning = False
        return winner, gamerunning
    # if all this fails
    return winner, gamerunning


if __name__ == '__main__':
    board = [[' ' for y in range(7)] for x in range(6)]
    print("\nLET'S PLAY CONNECT FOUR!\n")
    player1, player2 = initiateGame(board)
    winner = game(board, player1, player2)
    printBoard(board)
    print("THE WINNER IS.....: ", winner)