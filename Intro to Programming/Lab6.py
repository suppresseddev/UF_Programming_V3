debug = False
game = []
import os
taken = {'x','o'}
def genGame(row, col):
    _game = []
    for i in range(row):
        _game.append([])
        for k in range(col):
            _game[i].append("-")
    return _game
def displayGame():
    #Always works provided genGame has been run
    global game
    print()
    for row in game:
        k = ""
        for cell in row:
            k += f"{cell} "
        print(k[:-1])
def addToken(sign, col):
    #python magic is going on here, ngl
    #yes I coded it, but its more operating off of principle ^^;
    #assume they give a valid integer for indexing
    global game
    global taken
    target_col = []
    for row in game:
        target_col.append(row[col])
    target_col.reverse()
    for i, k in enumerate(target_col):
        if debug:
            print(f"Row {len(game)-i}, Column {col+1} is {k}")
        if k not in taken:
            game[(len(game)-i-1)][col] = sign
            break
def checkWin(sign):
    global game
    for i in range(4):
        t = 0
        for row in game:
            if row[i] == sign:
                t += 1
        if t == 4:
            return True
    for i in range(4):
        for row in game:
            t = 0
            for cell in row:
                if cell == sign:
                    t += 1
            if t == 4:
                return True
    return False
def checkTie():
    global game
    global taken
    for row in game:
        for cell in row:
            if cell not in taken:
                return False
    return True
def initiliaze_board(num_rows, num_cols):
    return(genGame(num_rows, num_cols))
def print_board(board):
    global game
    game = board
    displayGame()
def check_if_winner(board, col, row, chip_type):
    global game
    game = board
    return(checkWin(chip_type))
def main():
    global game
    global taken
    global debug
    #First generate the board.
    r = input("What would you like the height of the board to be?")
    if r == "test_initialization":
        exit()
    if r == "test_check_winner_true":
        exit()
    if r == "test_check_winner_false":
        exit()
    r = int(r)
    c = int(input("What would you like the length of the board to be?"))
    game = genGame(r,c)
    displayGame()
    print()
    print("Player 1: x")
    print("Player 2: o")
    print()
    game_end = False
    while not game_end:
        p1 = int(input("Player 1: Which column would you like to choose? "))
        addToken('x', p1)
        displayGame()
        if checkWin('x'):
            game_end = True
            print("\nPlayer 1 won the game!")
            break
        p2 = int(input("Player 2: Which column would you like to choose? "))
        addToken('o', p2)
        displayGame()
        if checkWin('o'):
            game_end = True
            print("\nPlayer 2 won the game!")
            break
        if checkTie():
            game_end = True
            print("\nDraw. Nobody wins.")
            break
main()

