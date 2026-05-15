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
    #Creating a buffer to prevent incomplete packets from being processed
    buffer = ""
    while "####" not in buffer:
        data = conn.recv(2048)
        if not data:
            break
        buffer += data.decode()
    if not data:
        break

    while "####" in buffer:
        packet, buffer = buffer.split("####", 1)
        seq_str = packet.split(";")[0]
        try:
            seq = int(seq_str)
        except ValueError:
            print(f"INCOMPLETE PACKET: {seq_str}")
            continue
        if seq != expected:
            print(f"WRONG ORDER: expected {expected}, got {seq}")
        else:
            print(f"OK: {seq}")
        expected = seq +1
