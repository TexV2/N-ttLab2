import socket
HOST = ""
PORT = 5005
expected = 10001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
print("Listening...")

while True:
    data, addr = sock.recvfrom(2048)
    msg = data.decode()
    seq_str = msg.split(";")[0]
    seq = int(seq_str)
    if seq != expected:
        print(f"ORDER ERROR: expected {expected}, got {seq}")
    else:
        print(f"OK : {seq}")
    expected = seq +1