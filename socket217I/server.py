from backend import Color, Packet, Board
import socket
import sys

# ###########################################################
# Part A - Setup and connecting
# ###########################################################

# Configure IP address (of server) and PORT
# c:\> python server.py [PORT [SERVER IP]]
port = 5371             # Inbound port that the server is listening on
server = "127.0.0.1"    # The IP address you want this server listining on. (It needs to be an IP address for this machine)
if len(sys.argv)>=2: port=int(sys.argv[1])
print(f"XOXp Server will listen to {server} on port {port}\n")

# Setup network connection(s)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #  IPv4 with TCP
addr = (socket.gethostbyname(server))
s.bind((addr,port))
s.listen(5)

# Wait for a Client to connect
print("Waiting for clients...")
conn, address = s.accept()
print(f"The address connecting inbound is {address[0]} on port {address[1]}")

# Serup an XOX board to play the game
game=Board()

# ###########################################################
# Part B - The Main Loop
# ###########################################################

# Loop getting a request and replying
# Server = Software listens for requests and sends replies
while True:
    # ---------------------------------------------------------------
    # Wait for a request from the client, decode and display it
    # ---------------------------------------------------------------
    print("\nWaiting for Client's request...")
    inbound = conn.recv(2048)           # Listening for a request
    request = inbound.decode('utf-8')   # Decode the request to a Python String
    print(f"> {request}\n")

    # ---------------------------------------------------------------
    # Process the request (as an "Echo Server")
    # ---------------------------------------------------------------
    # reply="I dont know what you mean"
    # if request=="Hi": reply = "Hello"
    # if request=="What is your name": reply = "Iles"
    # if request=="[GET]": reply = "<html><h1>Hi</h1></html>"

    # ---------------------------------------------------------------
    # Process the request (as an "XOX Server")
    # ---------------------------------------------------------------
    if request in "123456789":
        position = int(request)-1       # Get the position; 1-9  needs to be converted to 0-8
        game.place(position, "O")       # update the board 
        print(game.generateBoard("X"))  # display the board
        if game.getWinner() =="":       # If the game has not been won, then
            play = game.getPlay("X")    #   Ask the X player for their position
            game.place(play,"X")        #   Update the board
        else:                           # Else:
            print(game.getFinalState())
        reply=game.generateBoard("O")   # Send the cleint the update baord
        if game.getWinner() != "":
            reply += ("\n"+game.getFinalState()+"\n")
    
    
    # ---------------------------------------------------------------
    # Encode the reply, and send it back to the client
    # ---------------------------------------------------------------
    outbound = reply.encode('utf-8')    # Encode the reply
    conn.sendall(outbound)              # Send the reply
    if request=="end": break
    if game.getWinner() !="": break

# ###########################################################
# Part C - Close the connection and Exit
# ###########################################################

s.detach()
s.close()
conn.close()


