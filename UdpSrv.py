import socket
import sys

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
data = 300

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)
 

try:
    sock.bind(('', 9999))
except socket.error as msg:
	print("Bind to local port failed")
	sys.exit()

print("Listening for UDP requests (IPv6/IPv4). Use CTRL+C to terminate the server") 
while(True):
    udpPacket = sock.recvfrom(data)
    print("Request from: {} port: {}".format(udpPacket[1][0], udpPacket[1][1]))
    data1 = udpPacket[0].decode() [::-1]
    sock.sendto(str.encode(data1), udpPacket[1])