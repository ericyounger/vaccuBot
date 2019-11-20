#!/usr/bin/env python3
import pygame
import socket


# initializes Pygame
pygame.init()

# sets the window title
pygame.display.set_caption(u'Keyboard events')

# sets the window size
pygame.display.set_mode((400, 400))

HOST = '192.168.2.189'  # The server's hostname or IP address
PORT = 65433        # The port used by the server


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Connected to server at", HOST)

while True:
    # gets a single event from the event queue
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        break

    # captures the 'KEYDOWN' and 'KEYUP' events
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):
        # gets the key name
        key_name = pygame.key.name(event.key)
        # converts to uppercase the key name
        key_name = key_name.upper()

        if event.type == pygame.KEYDOWN:
            if(key_name == 'W'):
                s.send('w')
                print('W')
            elif(key_name == 'A'):
                pass
            elif(key_name == 'S'):
                pass
            elif(key_name == 'D'):
                pass
pygame.quit()

s.close()


