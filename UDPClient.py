__author__ = "Mitchell Sheep"
# Import These libraries 
import socket
import sys
import random
import struct
import time
 
UDP_IP = "127.0.0.1" 
UDP_PORT = 5005
MESSAGE = raw_input('Key-IN Go or NO: ') # indicate GO for start prgram or NO for exit
 
print "UDP target IP:", UDP_IP
n = int(raw_input('Key-In number: ')) # enter in the nuber of values to send
r = float(raw_input('Key-In float max range (must be float): ')) # enter in the nuber of values to send
total = n+1 #Add one to offset list tos start at 1 and end at n
 
clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #open socket for client under UDP
MESSAGE.capitalize();
if MESSAGE == "GO":
    while n > 0: #Loop for all values    
        time.sleep(0.01) # Sleep for 0.01 seconds to align with server
        floating = random.uniform(1.0, r) #Choose random flaot from 1.0 to 100.0
        sender = struct.pack('f', floating) # packfloat into binary byte  packet
        clientsock.sendto(sender, (UDP_IP, UDP_PORT)) #Send sender varieble to specified address 
        print>> sys.stderr, 'Sent: %s' %  floating,  total - n #indicate what number has sent and its index
	n -= 1 #Decrement nfor succesful loop
    clientsock.sendto(struct.pack('f', -1.0), (UDP_IP, UDP_PORT)) #Sewnd signal for server to close
    print >>sys.stderr, 'Socket Closing. Smell Ya Later!'  
    clientsock.close() # Close Socket

elif MESSAGE == "NO":
    print >>sys.stderr, 'Rest Day'
    clientsock.close()

