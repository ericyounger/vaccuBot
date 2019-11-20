#!/usr/bin/env python3

import socket
#192.168.2.18 is RPI adress
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65433       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected client on', addr)
        while True:
            data = conn.recv(4096)

            if data.decode() == "driveForward":
                print("driving forward")

            elif data.decode() == "driveRevers":
                print("Reversing")

            elif data.decode() == "pivotLeft":
                print("pivoting left")

            elif data.decode() == "pivotRight":
                print("pivoting right")

            elif data.decode() == "stop":
                print("stopping")

            elif data.decode() == "slowDown":
                print("slowing down")

            elif data.decode() == "speedUp":
                print("Speeding up")

            elif data.decode() == "shutdown":
                print("shutting down all motors")