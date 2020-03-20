#If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

#Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

#[[0, 0, 1],
# [0, 1, 2],
# [2, 1, 0]]
#We want our function to return:

#-1 if the board is not yet finished (there are empty spots),
#1 if "X" won,
#2 if "O" won,
#0 if it's a cat's game (i.e. a draw).
#You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

def is_solved(board):
    # Check who won the rows.
    for i in range(3):
        if all([board[i][j]==1 for j in range(3)]):
            return 1
            break
        elif all([board[i][j]==2 for j in range(3)]):
            return 2
            break
    # Check who won the columns.
    for j in range(3):
        if all([board[i][j]==1 for i in range(3)]):
            return 1
            break
        elif all([board[i][j]==2 for i in range(3)]):
            return 2
            break
    # Check who won the diagonal.
    if all([board[i][i]==1 for i in range(3)]):
        return 1
    elif all([board[i][i]==2 for i in range(3)]):
        return 2
    # If the board is not yet finished, then return -1, otherwise it's a cat.
    if (0 in board[0]) or (0 in board[1]) or (0 in board[2]):
        return -1
    else:
        return 0
