# coding=utf-8

# imports the Pygame library
import pygame



# initializes Pygame
pygame.init()

# sets the window title
pygame.display.set_caption(u'Keyboard events')

# sets the window size
pygame.display.set_mode((400, 400))

# infinite loop
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
                print("lol")
            elif(key_name == 'A'):
                pass
            elif(key_name == 'S'):
                pass
            elif(key_name == 'D'):
                pass



pygame.quit()


