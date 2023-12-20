     
    # ---------------------------------------------------------------
    # Process the request (as an "XOX Server")
    # ---------------------------------------------------------------
    position = int(request)-1
    game.place(position,"O")
    print(game.generateBoard("X"))
    if game.getWinner() != "":
        print(game.getFinalState())
        reply = game.generateBoard("O")
        break
    else:
        play=game.getPlay("X")
        game.place(play,"X")
        reply = game.generateBoard("O")