def main(): # main function
    player = next_player("") # set player to next player
    board = create_board() # create board
    while not (has_winner(board) or is_a_draw(board)): # while there is no winner or draw
        display_board(board) # display board
        make_move(player, board) # make move
        player = next_player(player) # set player to next player
    display_board(board) # display board
    print("Good game. Thanks for playing!")  # print good game

def create_board():     # create board
    board = []         # create empty list
    for square in range(9): # for each square
        board.append(square + 1) # append square + 1 to board
    return board    # return board

    # [1,2,3,4,5,6,7,8,9]

def display_board(board): # display board
    print() # print new line
    print(f"{board[0]}|{board[1]}|{board[2]}") # print board
    print('-+-+-') # print line
    print(f"{board[3]}|{board[4]}|{board[5]}")  # print board
    print('-+-+-') # print line
    print(f"{board[6]}|{board[7]}|{board[8]}") # print board
    print() # print new line

    # 1|2|3
    # -+-+-
    # 4|5|6
    # -+-+-
    # 7|8|9
    
def is_a_draw(board): # is a draw
    for square in range(9): # for each square
        if board[square] != "x" and board[square] != "o": # if square is not x or o
            return False # return false
    return True  # return true
    
def has_winner(board): # has winner
    return (board[0] == board[1] == board[2] or # vertical 1
            board[3] == board[4] == board[5] or # vertical 2
            board[6] == board[7] == board[8] or # vertical 3
            board[0] == board[3] == board[6] or # horizontal 1
            board[1] == board[4] == board[7] or # horizontal 2
            board[2] == board[5] == board[8] or # horizontal 3
            board[0] == board[4] == board[8] or # diagonal 1
            board[2] == board[4] == board[6])   # diagonal 2

def make_move(player, board): # make move
    square = int(input(f"{player}'s turn to choose a square (1-9): ")) # input square
    board[square - 1] = player # set board to player
 
def next_player(current): # next player
    if current == "" or current == "o": # if current is empty or o
        return "x" # return x
    elif current == "x": # if current is x
        return "o" # return o
 
if __name__ == "__main__": # if name is main
    main() # call main
