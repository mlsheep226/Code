__author__  = "Mitchell Sheep"
__status__ = "Testing"
#import the given Libraries
import socket
import sys
import struct
import random


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create Socket for TCP
server_adrs = ('127.0.0.1', 5432) #Set IP address to send to, and set the  port number
print >>sys.stderr, 'Connecting to %s port %s.' % server_adrs
client_socket.connect(server_adrs) #Connect to server under tuple server_adrs
message = raw_input('Enter GO or NO: ') #Tell the clinet to start or just close
n = int(raw_input('Enter the number of values: ')) #Get n number of floating point numbers to send to the server
r = float(raw_input('Enter max range of floats (MUST BE FLOAT): '))  #Enter the max value in the range
total = n + 1
message2 = message
#try connection with server
try:
    #Capitalize mesage
    message = message.capitalize();
    if message2 == "GO":
        #Start Loop and go unitl n is 0
	while n > 0:
	    floating = random.uniform(1.0, r) #set Random float digit
            sender = struct.pack('f', floating) #pack data into byte foramt
	    client_socket.sendall(sender)#send to the connected server
            print >>sys.stderr, 'Sent: %s' %  floating,  total - n
	    n -= 1 #decerement n for suucesful run
			
finally:
    print >>sys.stderr, 'Number failed overall: "%d"' % n
    print >>sys.stderr, 'Number Loop Complete Closing Socket'
    client_socket.close()

