import sys
import socket

ip = "0.0.0.0"
port = 34578

# Buffer size
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen(1)

    try:
        while True:
            # Listening
            print("Listening ...")
            # Accept
            client_socket, addr = s.accept()
            # Greeting after client connect
            print("[{}] has connected".format(addr[0]))
            greeting = "Hello [{}]".format(addr[0])
            client_socket.send(greeting.encode())
            while True:
                data = client_socket.recv(buffer_size)
                # break if no data
                if not data:
                    client_socket.close()
                    break
                # print message from client
                print("[{}] {}".format(addr[0], data.decode()))
                # close if the client sends 'exit' command
                if data.decode() == 'exit':
                    print("Connection closed from client side [{}]".format(addr[0]))
                    break
                # answer to client
                nachricht = input("Antwort: ")
                client_socket.send(nachricht.encode())
                # close and print message when send 'exit' command
                if nachricht == 'exit':
                    print("Connection closed to [{}]".format(addr[0]))
                    break
            # Restart after disconnect/close
            print("Reload ...")
            continue
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit(0)

