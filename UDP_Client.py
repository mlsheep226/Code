import socket
 
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = raw_input('Key-IN message: ')
 
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
 
clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print "Sending Message: ", MESSAGE
clientsock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

#while True:
data, addr= clientsock.recvfrom(1024) # buffer size is 1024 bytes
print "Received Message: ", data
clientsock.close()
