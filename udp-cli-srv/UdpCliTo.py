import socket
import sys

data = 300
TIMEOUT = 3

if len(sys.argv) < 2:
    print("Server IPv4/IPv6 address or DNS name is required as argument")
    sys.exit()

serverIP = sys.argv[1]

try:
    socket.inet_aton(serverIP)
except socket.error:
	print("Invalid server address supplied: "  + serverIP)
	sys.exit()

serverAddressPort = (serverIP, 9999)
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.settimeout(TIMEOUT)

while True:
	print("Sentence to send (\"exit\" to quit): ")
	frase = input()
	if frase == "exit": break
	udpPacket = str.encode(frase)
	sock.sendto(udpPacket, serverAddressPort)
	try:
		frase = sock.recvfrom(data)
		print("Received reply: " + frase[0].decode())
	except socket.timeout:
		print("No reply from server")

sock.close()

