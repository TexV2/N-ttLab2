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


while True:
    #Creating a buffer to prevent incomplete packets from being processed
    buffer = ""
    #Keeps collecting data until we have a complete packet
    while "####" not in buffer:
        data = conn.recv(2048)
        if not data:
            break
        buffer += data.decode()
    if not data:
        break
    #Runs through each complete message in buffer
    while "####" in buffer:
        #Splits the buffer on the first #### (first complete message)
        packet, buffer = buffer.split("####", 1)
        #Splits that message on ;, removing the uneccesary filler data
        seq_str = packet.split(";")[0]
        try:
            seq = int(seq_str)
        except ValueError:
            print(f"INCOMPLETE PACKET: {seq_str}")
            continue
        #check if the packets arrived in the right order then advance the expected sequence order
        if seq != expected:
            print(f"WRONG ORDER: expected {expected}, got {seq}")
        else:
            print(f"OK: {seq}")
        expected = seq +1
