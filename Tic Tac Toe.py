board = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]

def print_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board, player):
    # Check for horizontal wins
    for row in board:
        if row.count(player) == 3:
            return True
    
    # Check for vertical wins
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    # Check for diagonal wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

print("Welcome to Tic Tac Toe!")
print_board(board)

player = "X"

while True:
    row = int(input("Player " + player + ", enter row number (1-3): ")) - 1
    col = int(input("Player " + player + ", enter column number (1-3): ")) - 1
    
    if board[row][col] == "_":
        board[row][col] = player
        print_board(board)
        
        if check_win(board, player):
            print("Congratulations, player", player, "has won!")
            break
        
        if "_" not in [cell for row in board for cell in row]:
            print("The game is tied!")
            break
            
        player = "O" if player == "X" else "X"
    else:
        print("That position is already occupied. Please choose a different position.")
        
play_again = input("Do you want to play again? (y/n): ")
if play_again == "y":
    # Start the game again
else:
    print("Thanks for playing!")
