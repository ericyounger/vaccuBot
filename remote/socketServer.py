#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65433       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(4096)
            #if not data:
            #    break
            #conn.sendall(data)

            if data.decode() == "driveForward":
                print("driving forward")

            if data.decode() == "driveRevers":
                print("Reversing")

            if data.decode() == "pivotLeft":
                print("pivoting left")

            if data.decode() == "pivotRight":
                print("pivoting right")

            if data.decode() == "stop":
                print("stopping")

            if data.decode() == "slowDown":
                print("slowing down")

            if data.decode() == "speedUp":
                print("Speeding up")

            if data.decode() == "shutdown":
                print("shutting down all motors")