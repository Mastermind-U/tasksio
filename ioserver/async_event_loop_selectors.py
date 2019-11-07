import socket
import selectors


selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen()


def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('connection from', addr)


def send_message(client_socket):
    request = client_socket.recv(4096)
    if request:
        response = f'Hello world {request}\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        pass


if __name__ == "__main__":
    event_loop()
