import sys

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        try:
            row, col = map(int, input(f"Player {current_player}, enter the row and column (1-3) to place your mark: ").split())
            if board[row - 1][col - 1] != " ":
                raise ValueError("Cell already occupied")
            board[row - 1][col - 1] = current_player
        except (ValueError, IndexError) as e:
            print(e)
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            sys.exit(0)
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            sys.exit(0)

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
