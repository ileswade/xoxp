import socket

# Part A
port = 5372
serverAddress = "localhost"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = (socket.gethostbyname(serverAddress))
s.bind((addr, port))
s.listen(5)
print("Waiting for client...")
conn, addr = s.accept()

print(f"{conn} connection from {addr[0]} IP on port {addr[1]}")

reply = "Welcome to Xs and Os game"
outbound = reply.encode('utf-8')
conn.sendall(outbound)

# Part B
while True:
    # Listen (forever) on socket
    inbound =conn.recv(2048)

    # Decode inbound string to a Python string
    request = inbound.decode('utf-8')

    # decide what to do with the request
    # In this first case we will just ECHO the message
    print(request)
    reply = request.swapcase()

    # encode the reply Python string outbound string
    outbound = reply.encode('utf-8')

    # Send 
    conn.sendall(outbound)


# Part C
# Sen last message as to who one 
# Display to user at the serve who one and the game baord
# Close connection
s.shutdown(0)
conn.close()
s.close()