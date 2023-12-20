import socket

def sendMessage(connection, outMessage):
    connection.sendall(outMessage.encode('utf-8'))

def getMessage(connection):
    data = connection.recv(2048)
    return data.decode('utf-8')


# Intialize Server, create inbound socket and listen
port = 5371
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr =(socket.gethostbyname('localhost'))
s.bind((addr, port))
s.listen(5)
print("Waiting for client...")
conn, addr=s.accept()

# Inbound conenction recieved.  Prtint conenction infomration and reply with a welcom message
print(f"{conn} conection to {addr[0]} on port {addr[1]}")
sendMessage(conn, "Welcome to the Server")

# Go in to a looo of listening
while True:
    # Listen (forever) on the socket
    inbound = conn.recv(2048)

    # Decode inbound data back to a Pythin String
    request = inbound.decode('utf-8')

    # make some decision as to how to reply
    # In this case just echo the reply
    reply = request

    # Prepare to send the reply. Conver to a byte string for sending
    outbound = reply.encode('utf-8')

    # Send the the outbound reply
    conn.sendall(outbound)

    if reply=="end": break

s.shutdown(0)
conn.close()
s.close()
