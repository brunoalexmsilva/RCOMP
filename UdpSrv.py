import socket
import sys

bufferSize = 1024

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
 
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
try:
    UDPServerSocket.bind(('', 9998))
except socket.error as msg:
	print("Bind to local port failed")
	sys.exit()
#UDPServerSocket.bind((localIP, localPort))

print("Listening for UDP requests (IPv6/IPv4). Use CTRL+C to terminate the server") 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)