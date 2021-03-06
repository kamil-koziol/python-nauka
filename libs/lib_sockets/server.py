import socket
import time

HEADERSIZE = 10 # ilość mozliwych bitow do wysłania czyli 2**10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    msg = "Witam na moim serwerze!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))
