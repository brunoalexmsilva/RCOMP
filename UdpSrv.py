import socket
import sys

data = 300

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
 
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
try:
    UDPServerSocket.bind(('', 9999))
except socket.error as msg:
	print("Bind to local port failed")
	sys.exit()

print("Listening for UDP requests (IPv6/IPv4). Use CTRL+C to terminate the server") 

# Listen for incoming datagrams
while(True):
    udpPacket = UDPServerSocket.recvfrom(data)
    address = udpPacket[1]
    print("Request from: {} port: {}".format(address[0]), address[1])
    UDPServerSocket.sendto(bytesToSend, address)