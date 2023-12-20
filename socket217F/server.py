import socket
from backend import Color, Packet, Board

# Part A
port = 5380
serverAddress = "localhost"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (socket.gethostbyname(serverAddress))
s.bind((addr, port))
s.listen(5)
print("Waiting for client...")
conn, addr = s.accept()

print(f"{conn} connection from {addr[0]} IP on port {addr[1]}")

reply = "Idiot GPT"
outbound = reply.encode('utf-8')
conn.sendall(outbound)

game = Board()

# Part B
while True:
    # Listen (forever) on socket
    request =conn.recv(2048).decode('utf-8')
    request = int(request)-1


    print(request)
    game.place(request,"O")
    print(game.generateBoard(""))
    if game.getWinner() != "":
        print(game.getFinalState())
        reply = game.generateBoard("")
        break
    else:
        play=game.getPlay("X")
        game.place(play,"X")
        reply = game.generateBoard("O")

    # Send 
    conn.sendall(reply.encode('utf-8'))


# Part C
# Sen last message as to who one 
# Display to user at the serve who one and the game baord
# Close connection
s.shutdown(0)
conn.close()
s.close()