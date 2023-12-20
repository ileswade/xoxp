from backend import Color, Packet, Board


game = Board("X")
winner = ""

while not winner:
    whosTurnIsIt = game.getNextPlayer()
    print(game.generateBoard(whosTurnIsIt))
    position=game.getPlay(whosTurnIsIt)
    game.place(position, whosTurnIsIt)
    winner = game.getWinner()
    
print(game.generateBoard(whosTurnIsIt))
print(game.getFinalState())

