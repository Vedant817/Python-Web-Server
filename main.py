import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Stream signifies TCP Protocol.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.setblocking(False)

server_socket.bind(("0.0.0.0", 8080))
server_socket.listen(5)  # Here 5 refers to the backlog which means the number of connections that can wait in the queue
print('Listening at the port 8080')

while True:
    client_socket, client_address = server_socket.accept()
    # print(client_socket)
    # print(client_address)
    request = client_socket.recv(1500).decode()
    print(request)
