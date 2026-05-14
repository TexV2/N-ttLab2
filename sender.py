import socket, time

HOST = "RECEIVER_IP"
PORT = 5005
RATE = 1
NUMBER_OF_PACKETS = 60
SEQUENCE_START = 10001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
delay = 1.0 / RATE

for i in range(NUMBER_OF_PACKETS):
    seq = str(SEQUENCE_START + i) + ";"
    payload = ("A" * 1465)[:1465]
    msg = (seq + payload + "####").encode()
    sock.sendto(msg, (HOST, PORT))
    time.sleep(delay)

sock.close()