import socket, time

#Sets the IP addres 192.168.0.33 (my laptop currently) as HOST
HOST = "192.168.0.33"
#Sets the PORT to 5005
PORT = 5005
#Sets the rate at which packets will be sent
RATE = 45
#Sets how many packets will be sent in total
NUMBER_OF_PACKETS = 4500
#Selects what the starting message on the packet will be
SEQUENCE_START = 10001

#Creates a UDP socket using IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Sets the delay
delay = 1.0 / RATE
#Connects to the Host (required for TCP)
sock.connect((HOST, PORT))

#Sends on packet for each i in range number of packets
for i in range(NUMBER_OF_PACKETS):
    #Creates the order verification number that will be read by the receiver
    seq = str(SEQUENCE_START + i) + ";"
    #Creates the message filler to fulfill the 1465 size requirment
    payload = ("A" * 1465)[:1465]
    #Combines the order verification number with the "junk" data
    msg = (seq + payload + "####").encode()
    #Sends the message to the already connected HOST
    sock.send(msg)
    #Pauses the script for one second
    time.sleep(delay)

#Close the socket
sock.close()