def print_board(board):
    for row in board:
        print("I".join(row))
        print("-"*5)

def check_winner(board,player):
    for row in board:
        if all(s==player for s in row):
            return True
        for col in range(3):
            if all(board[row][col] == player for row in range(3)):
                return True
                return False

def is_draw(board):
    return all(board[row][col]!= ''for row in range(3) for col in range(3))

def tic_tac_toe():
    board=[['' for _ in range(3)]for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row=int(input(f"Player{current_player}, enter the column (0,1,2):"))

        if board[row][col]=='':
            board[row][col]=current_player
            if check_winner(board,current_player):
                print_board(board)
                print(f"Player{current_player}wins!")
                break
            current_player='O'if current_player=='X'else'X'

    else:
        print("That spot is already taken, try again.")

tic_tac_toe()
