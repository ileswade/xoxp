def checkForWin(board):
    # Given a string of 9 characters representing a tic-tac-toe board, determin if any
    # lines win.  A winning line is a series of three matchign letters (X or O) in a 
    # column, row or on one of the two diagonals.
    # Return the letter of the player who wone or, if no one has wone, a empty string
    #
    # Advanced: 
    # Return the specific line that the player has won. The WinLine is a letter between
    # A and G.  
    # A indicate the player has won along the TOP row, 
    # B is a win on the middle row, and 
    # C is a win on the bottom row.
    # D is a win down the first column,
    # E is a win down the middle column
    # F is a win down the last column
    # G is a win along the diagonal from the top left to the bottom right, and
    # H is a win along the diagonal from the top right to the bottom left

    # A indicate the player has won along the TOP row, 
    if board[0]==board[1] and board[1]==board[2] and (board[0] in "XO"): win = 'A', board[0]

    # D is a win down the first column,
    if board[0]==board[3] and board[3]==board[6] and (board[0]=="X" or board[0]=="O"):
        winner = board[0]
        winLine = "D"

    # G is a win along the diagonal from the top left to the bottom right, and   
    if board[0]==board[4] and board[4]==board[8] and (board[0]=="X" or board[0]=="O"):
        winner = board[0]
        winLine = "G"
    '''
    012
    345
    678
    '''
    pass

currentBoard="XXXOX O X"

currentBoard="XO OX O X"
print(checkForWin(currentBoard))
