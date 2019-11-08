import socket
from select import select

tasks = []

rdict = {}
wdict = {}


READ = 0
WRITE = 1


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.listen()

    while True:
        yield (READ, server_socket)

        client_socket, addr = server_socket.accept()  # read
        print('connection from', addr)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield (READ, client_socket)
        request = client_socket.recv(4096)  # read

        if not request:
            break
        else:
            response = 'Hello world\n'.encode()

            yield (WRITE, client_socket)
            client_socket.send(response)  # write

    client_socket.close()


def event_loop():
    while any([tasks, rdict, wdict]):
        while not tasks:
            ready_to_read, ready_to_write, _ = select(rdict, wdict, [])

            for sock in ready_to_read:
                tasks.append(rdict.pop(sock))

            for sock in ready_to_write:
                tasks.append(wdict.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)

            if reason == READ:
                rdict[sock] = task

            if reason == WRITE:
                wdict[sock] = task

        except StopIteration:
            print('done!')


if __name__ == "__main__":
    tasks.append(server())
    event_loop()
