import sys
import socket

ip = input("IP-Adresse: ")
port = 34578

# Buffer size
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ip, port))

    try:
        # Receive greeting
        greeter = s.recv(buffer_size)
        print("Connected to [{}]\n{}".format(ip, greeter.decode()))
        while True:
            # send message to host
            nachricht = input("Nachricht: ")
            s.send(nachricht.encode())
            # if send 'exit' command to host, close
            if nachricht == 'exit':
                print("Connection closed to [{}]".format(ip))
                break
            # receive answer from remote host
            antwort = s.recv(1024)
            # print answer from remote host
            print("[{}] {}".format(ip, antwort.decode()))
            # if remote host send 'exit' command, close
            if antwort.decode() == 'exit':
                print("Connection closed from remote host [{}]".format(ip))
                break
        sys.exit(0)
    except KeyboardInterrupt:
        print("You pressed Ctlr+C")
        sys.exit(0)

