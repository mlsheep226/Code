import socket
import sys

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5002)
print >>sys.stderr, 'Starting up on %s port %s.' % server_address
server_socket.bind(server_address)

server_socket.listen(1)

while True:
	# Wait for a connection
	print >>sys.stderr, 'Waiting for a connection to client.'
	connection, client_address = server_socket.accept()
	try:
		print >>sys.stderr, 'Connection from', client_address

		# Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(16)
			print >>sys.stderr, 'Received: "%s"' % data
            		if data:
                		print >>sys.stderr, 'sending data back to the client' 
                		data2 = data.upper()
				connection.sendall(data2)
            		else:
                		print >>sys.stderr, 'No more data from', client_address
                		break
				connection.close()

	finally:
		connection.close()
