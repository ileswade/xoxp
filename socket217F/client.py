import socket
import sys

IPAddress="127.0.0.1"

if len(sys.argv)>1:
    IPaddress = sys.argv[1]
    print (f"An IP Address of {IPaddress} was entered")
else:
    print (f"No IP Address was entered on the command line")

print (f"I will use IP Address {IPAddress}")

# PArt A
port = 5380
serverAddress = 'IPAddress'
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( (serverAddress, port) )

data = s.recv(2048)
reply = data.decode("utf-8")
print(reply)

# Part B
while True:
    # get user input
    message = input("> ")

    # encode data for network
    outbound = message.encode('utf-8')

    # send message
    s.sendall(outbound)

    # wait for a reply
    inbound = s.recv(2048)

    # decode the reply back a Python String
    reply = inbound.decode('utf-8')

    # print
    print(f"< {reply}")

 

#Part C
# display who one
# Close connection

