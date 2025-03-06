def initialize_board(num_rows, num_cols):
    return [['-' for _ in range(num_cols)] for _ in range(num_rows)]


def print_board(board):
    for row in reversed(board):
        print(" ".join(row))


def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row
    return -1  # This shouldn't happen given the assumptions


def check_if_winner(board, col, row, chip_type):
    num_rows, num_cols = len(board), len(board[0])

    # Check vertical
    count = 1
    for i in range(1, 4):
        if row - i >= 0 and board[row - i][col] == chip_type:
            count += 1
        else:
            break
    if count >= 4:
        return True

    # Check horizontal
    count = 1
    for direction in (-1, 1):  # Left and right
        step = 1
        while 0 <= col + step * direction < num_cols and board[row][col + step * direction] == chip_type:
            count += 1
            step += 1
            if count >= 4:
                return True

    return False


def play_game():
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))

    board = initialize_board(height, length)
    print_board(board)

    print("Player 1: x")
    print("Player 2: o")

    turn = 0
    while True:
        player = "x" if turn % 2 == 0 else "o"
        col = int(input(f"Player {1 if player == 'x' else 2}: Which column would you like to choose? "))
        row = insert_chip(board, col, player)
        print_board(board)

        if check_if_winner(board, col, row, player):
            print(f"Player {1 if player == 'x' else 2} won the game!")
            return

        if all(board[r][c] != '-' for r in range(height) for c in range(length)):
            print("Draw. Nobody wins.")
            return

        turn += 1


if __name__ == "__main__":
    play_game()
