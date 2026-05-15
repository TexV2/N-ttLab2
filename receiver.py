import socket
# Empty string means listen on all network interfaces
HOST = ""
PORT = 5005
expected = 10001

#Creates UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Binds socket to PORT
sock.bind((HOST, PORT))

#TCP listening for an incoming connection
sock.listen(1)
print("Listening...")

#Accept incoming connection
conn, addr =sock.accept()
print(f"Connected to {addr}")

#Constant loop 
while True:
    #Waiting for the next packet, 2048 is the max bytes
    data = conn.recv(2048)
    if not data:
        break
    #Decodes bytes into string
    msg = data.decode()
    #Removes the unecessary parts of the string
    seq_str = msg.split(";")[0]
    #Converts string to int
    seq = int(seq_str)
    #Checks if the packet arrived in the correct order
    if seq != expected:
        print(f"ORDER ERROR: expected {expected}, got {seq}")
    else:
        print(f"OK : {seq}")
    expected = seq +1