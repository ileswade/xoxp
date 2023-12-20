import socket

def sendMessage(connection, outMessage):
    connection.sendall(outMessage.encode('utf-8'))

def getMessage(connection):
    data = connection.recv(2048)
    return data.decode('utf-8')

## Initalize Client and create outbound socket
port = 5371
server = "localhost"
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inital connection and wait for server reply
s.connect((server, port))
text = getMessage(s)
print(text)

# Application Loop
while True:
    # get user message
    message = input("> ")

    # Prepare message to send
    outbound = message.encode('utf-8')

    # Send message to server
    s.sendall(outbound)

    # Wait for Server to Reply
    inbound = s.recv(2048)

    # Decode reply data back to a Python string
    reply = inbound.decode('utf-8')

    # Display on the screen
    print (f"< {reply}")

    if reply=="end": break

s.close()


