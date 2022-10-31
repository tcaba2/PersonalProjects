from random import randrange

print("Hello dear user! This is a Tic-Tac-Toe game, the computer is playing first and plays X, you play by entering the number of the square you want to play.")

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print(" +-------+-------+-------+ \n |       |       |       | \n")
    print(" |  ", board[0][0], "  |   ", board[0][1], " |   ", board[0][2], " |   ")
    print(" |       |       |       | \n +-------+-------+-------+ \n |       |       |       | \n")
    print(" |  ", board[1][0], "  |   ", board[1][1], " |   ", board[1][2], " |   ")
    print(" |       |       |       | \n +-------+-------+-------+ \n |       |       |       | \n")
    print(" |  ", board[2][0], "  |   ", board[2][1], " |   ", board[2][2], " |   ")
    print(" |       |       |       | \n +-------+-------+-------+ \n |       |       |       | \n")
    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    r = True
    while r:
        try:
            o = int(input("Enter your first move: "))
        except ValueError:
            print("Not a valid play")
            o = int(input("Enter your first move: "))
        if o <= 0 or o >= 10:
            print("Not a valid play")
            o = int(input("Enter your first move: "))
        else:
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == o and (i,j) in free:
                        board[i][j] = "o"
                        r = False           

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    global free
    for i in range(len(board)):
            for j in range(len(board)):
                if type(board[i][j]) == int:
                    free.append((i, j))

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        return False

def draw_move(board):
    # The function draws the computer's move and updates the board
    r = True
    while r:
        x = randrange(10)
        for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == x and (i,j) in free:
                        board[i][j] = "x"
                        r = False

board = [[1, 2, 3],
        [4, "x", 6],
        [7, 8, 9]]

free = []

while True:
    display_board(board)
    make_list_of_free_fields(board)
    if len(free) == 36:
        print("It's a draw. Play again.")
        break
    enter_move(board)
    if victory_for(board, "o") == True:
        display_board(board)
        print("You've won!")
        break
    make_list_of_free_fields(board)
    draw_move(board)
    if victory_for(board, "x") == True:
        display_board(board)
        print("You've lost. Better luck next time!")
        break


    







