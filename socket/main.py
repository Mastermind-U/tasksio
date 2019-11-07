import socket
from views import index, blog

URLS = {
    '/': index,
    '/blog': blog
}


def parse_request(request):
    parserd = request.split(' ')
    method = parserd[0]
    url = parserd[1]
    return (method, url)


def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)
    if url not in URLS:
        return ('HTTP/1.1 404 Not found\n\n', 404)
    return ('HTTP/1.1 200 OK\n\n', 200)


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return URLS[url]()


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)

    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5555))
    server_socket.listen()
    try:
        while True:
            clint_socket, addr = server_socket.accept()
            request = clint_socket.recv(1024)
            print(f'\n{request.decode()}\n{addr}')

            response = generate_response(request.decode())

            clint_socket.sendall(response)
            clint_socket.close()

    except KeyboardInterrupt:
        print('Finished!')


if __name__ == '__main__':
    run()
