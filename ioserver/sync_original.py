import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 5555))
server_socket.listen()

while True:
    print('server accepted')
    client_socket, addr = server_socket.accept()
    print('connection from', addr)
    while True:
        print('ready to recieve')
        request = client_socket.recv(4096)

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()
            client_socket.send(response)
    print('outside loop')
    client_socket.close()
