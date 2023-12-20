from backend import Color, Packet
import socket
import sys

# ###########################################################
# Part A - Setup and connecting
# ###########################################################

# Configure IP address (of server) and PORT
# c:\> python client.py [PORT [SERVER IP]]
port = 5371             # Outbound port that the server is listening on
server = "127.0.0.1"    # THe Server's IP address (127.0.0.1 assumes the server is running on the same computer)
if len(sys.argv)>=2: port=int(sys.argv[1])
if len(sys.argv)>=3: server=sys.argv[2]
print(f"XOXp Client is trying to connect to the server at {server} on port {port}\n")

# Setup network connection(s)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #  IPv4 with TCP




# Attempt to connect
try:
    s.connect((server, port))
except:
    print(f"For some reason, the connection failed.  Is the server not running and listening on port {port}?")
    exit()
# ###########################################################
# Part B - The Main Loop
# ###########################################################

# Loop getting a request and replying
# Client = Software makes requests and listens for replies
while True:
    # Get user request
    request = input("> ")

    # Convert to byte string
    outbound = request.encode('utf-8')

    # send to the server using the "s" obejct
    s.sendall(outbound)

    # Listen for a reply using the "s" object
    inbound = s.recv(2048)

    # Convert to a Python String
    reply = inbound.decode('utf-8')

    # Print reply
    print(reply)
    if reply.endswith("winline."): break
    if request=="end": break

# ###########################################################
# Part C - Close the connection and Exit
# ###########################################################

s.close()