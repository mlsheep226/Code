import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adrs = ('localhost', 5002)
print >>sys.stderr, 'Connecting to %s port %s.' % server_adrs
client_socket.connect(server_adrs)
message = raw_input('Message: ')
try:
    #Send data
    print >>sys.stderr, 'Sending: "%s"' % message
    client_socket.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received != amount_expected:
        data = client_socket.recv(amount_expected)
        amount_received += len(data)
        print >>sys.stderr, 'Received: "%s"' % data

finally:
    print >>sys.stderr, 'Message Loop Complete Closing Socket'
    client_socket.close()
