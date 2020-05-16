import socket
import sys

data = 300
targetIP = "255.255.255.255"


serverAddressPort = (targetIP, 9999)
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

while True:
	print("Sentence to send (\"exit\" to quit): ")
	frase = input()
	if frase == "exit": break
	udpPacket = str.encode(frase)
	sock.sendto(udpPacket, serverAddressPort)
	frase = sock.recvfrom(data)
	print("Received reply from {}: {}".format(frase[1], frase[0].decode()))

sock.close()