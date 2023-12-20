
class Packet():
    def __init__(self, connection):
        self.connection = connection
    
    @staticmethod
    def package(command, *attributes):
        data = "["+command.strip().lower()+"]"      # Lower case the command, remove trailing and leading spaces, and encapsulate it in square brackets
        for item in attributes:                     # For each additioan bit of data found in the attributes
            data += "[" + str(item) +"]"            #    also encapsulate it in square brackets
        data = data.encode("utf-8")                 # Finally, encode the string as UTF-8 in prepration for sending across the network
        return data

    @staticmethod
    def unpackage(data):
        try:
            data = data.decode("utf-8")             # Decode the data from a UTF-8 byte string to a regular Python string
        finally:                                    # if the decoding worked or not
            if(data[0]=="[" and data[-1]=="]"):     # Check to see if the string has square barackets at the start and end of the string
                items = (data[1:-1].split("]["))    # and if it does, split the string in to a Python List with each item in brackets as an element in the list
            command = items.pop(0).strip().lower()  # The "command" is the first item.  Remove it from the attributes list
        return command, items                       # Return both the command and the attributes
    
class Board():
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    def __init__(self, myLetter="X", board=""):
        self.setMyLetter(myLetter)
        self.resetBoard(board)
    
    def setMyLetter(self, myLetter):
        self.__myLetter = ""
        self.__theirLetter = ""
        if myLetter.upper() in "XO":
            if myLetter.upper()=="X":
                self.__myLetter = "X"
                self.__theirLetter = "O"
            elif myLetter.upper()=="O":
                self.__myLetter = "O"
                self.__theirLetter = "X"
        return self.__myLetter

    def resetBoard(self, board=" "*9):
        self.__gameBoard = board
        self.__winLine = ""
        self.__winner = ""
        self.__playerRotation = "XO"
        if len(board)!=9:
            self.__gameBoard=" "*9
        return self.__gameBoard

    def generateBoard(self, generateFor=""):
        self.checkForWin()
        if generateFor not in "XO": generateFor=self.__myLetter

        colorX =        self.color.BOLD + self.color.GREEN if generateFor=="X" else self.color.RED
        colorO =        self.color.BOLD + self.color.GREEN if generateFor=="O" else self.color.RED
        colorWinline =  self.color.BOLD + self.color.YELLOW
        colorLines =    self.color.END
        colorCounter =  self.color.DARKCYAN
        buffer = ""
        
        counter=0
        # This is the drawing board.  It is a template of the gameboard, to show
        #  A) location of lines that seperate the GAME grid, 
        #  B) the location of WINLINES used for showing what line won
        #  C) the placement of the GAME plays index.
        drawBoard =  ".G.D...|...E...|...F.H.;.AA1AAA|AAA2AAA|AAA3AA.;...D.G@|...E..@|.H.F..@;-------+-------+-------;...D...|.G.E.H.|...F...;.BB4BBB|BBB5BBB|BBB6BB.;...D..@|.H.E.G@|...F..@;-------+-------+-------;...D.H.|...E...|.G.F...;.CC7CCC|CCC8CCC|CCC9CC.;.H.D..@|...E..@|...F.G@;"

        for char in drawBoard:
            # the @ token represent the GAME square's index (eg 1-9) for the user to select "where to play"
            # The @ increases the counter by one, and puts that number down (eg first or second or third...  playable square)
            # Don't display the square's index when someone has been detected as winning.
            if char == "@":
                counter += 1
                addChar = (colorCounter + str(counter)) if not self.__winner else " "
            
            # The .|-+ symbold are to be drawn literally.  They represent the lines that divide
            # the playable squares.
            if char in " |-+": addChar = colorLines + char
            
            # The "." token is used for counting spaces in the drawBoard and are to be replaced with a space " "
            if char ==".": addChar=" "

            # The tokens of 1-9 are replaced by the X or O that was played in that square.
            # Given a token value (1-9), check the board for which player (X or O) or blank
            # is currently stored in the in-memory board.  Replace the token with an X, and 
            # O or a blank
            if char >= "1" and char <="9":
                XorO = self.__gameBoard[int(char)-1]
                addChar=" "
                if XorO == "X": addChar = colorX + "X"
                if XorO == "O": addChar = colorO + "O"

            # If a win is detected, the winline is a letter (A-H) represeting which row, column
            # or diagonal IS the winning line.  The token (A-H) is replaced with a "-" if it is
            # row win, "|" if it is a column win, or "\"(or"/") if it is a diagonal win    
            if char >= "A" and char <="H":
                addChar = (colorWinline + "---|||\/"[ord(char)-65]) if char==self.__winLine else " "
            
            # The ";" is is the end of the TEXT row.  Three rows of TEXT make up a single
            # GAME play row.  In X's and O's, the playing GAME grid is 3x3, the TEXT grid, however
            # the TEXT grid is made up of 11 lines and 11 columns (9 lines made up of 3 lines/columns)
            # plus two text lines seperating the playing columns and rows from each other.
            if char ==";": addChar= "\n"

            # If colours have been used, ensure to turn the color off after the character 
            # is added to the buffer.
            buffer += (addChar + self.color.END)
        return buffer

    def checkForWin(self):
        win = "", ""                                    # Assume no one has won                           
        if self.__gameBoard.find(" ")==-1: win="T","T"  # If the board is filled, assume it is a tie until proven otherwise
        board=self.__gameBoard                          # used only to shorten code below
        # This method detects if a win is present in the Board.  A win is detected if the
        # same character is found in three location of the GAME board.  For instance, if the
        # 0th, 4th and 8th characters of the 'board' string are all X, then X wins along the "G" line
        if board[0]==board[1] and board[1]==board[2] and board[0] in "XO": win=board[0], "A"
        if board[3]==board[4] and board[4]==board[5] and board[3] in "XO": win=board[3], "B"
        if board[6]==board[7] and board[7]==board[8] and board[6] in "XO": win=board[6], "C"
        if board[0]==board[3] and board[3]==board[6] and board[0] in "XO": win=board[0], "D"
        if board[1]==board[4] and board[4]==board[7] and board[1] in "XO": win=board[1], "E"
        if board[2]==board[5] and board[5]==board[8] and board[2] in "XO": win=board[2], "F"
        if board[0]==board[4] and board[4]==board[8] and board[0] in "XO": win=board[0], "G"
        if board[2]==board[4] and board[4]==board[6] and board[2] in "XO": win=board[2], "H"
        
        self.__winner, self.__winLine=win               # Unpack and set member variables
        return bool(self.__winner)

    def getNextPlayer(self):
        self.__playerRotation = self.__playerRotation[-1]+self.__playerRotation[0]
        return self.__playerRotation[-1]
    
    def getWinner(self):
        return self.__winner
    
    def getWinLine(self):
        return self.__winLine
    
    def getBoard(self):
        return self.__gameBoard
    
    def getFinalState(self):
        if self.__winner=="T":
            return f"{self.color.BOLD}{self.color.RED}Tie{self.color.END} Game."
        elif self.__winner in ("XO"):
            return f"Game won by {self.color.BOLD}{self.color.GREEN}{self.__winner}{self.color.END} along the {self.color.BOLD}{self.color.YELLOW}{self.__winLine}{self.color.END} winline."
    
    def place(self, position, player):
        self.__gameBoard = self.__gameBoard[0:position]+player.upper()+self.__gameBoard[position+1:]
        self.checkForWin()
        return self.__gameBoard
    
    def getPlay(self, player):
        while True:
            play = input(f"It is your turn player \"{player}\". Which square do you wish to play?")
            if play == "end":
                return -1
            try:
                position = int(play)-1
            except:
                print(f"That is {self.color.RED}not{self.color.END} a valid character.")
                continue
            if position < 0 or position > 8: 
                print(f"That is {self.color.RED}not{self.color.END} a valid number (1-9).")
                continue
            if self.__gameBoard[position]!=" ":
                print(f"That space is {self.color.RED}already{self.color.END} played.")
                continue
            if self.__gameBoard[position]==" ": 
                return position


