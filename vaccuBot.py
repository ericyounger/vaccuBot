#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import pygame


# sets the window title
pygame.display.set_caption(u'Keyboard events')

# sets the window size
pygame.display.set_mode((400, 400))

class MotorControl(object):
    
    def __init__(self):
        self.speed = 100

        #setup motors, and communication with motorHAT
        # create a default object, no changes to I2C address or frequency
        self.mh = Adafruit_MotorHAT(addr=0x60)
        
        ################################# Set motors
        self.motorA = self.mh.getMotor(1)
        self.motorB = self.mh.getMotor(2)
        
        # set the speed to start, from 0 (off) to 255 (max speed)
        self.motorA.setSpeed(self.speed)
        self.motorB.setSpeed(self.speed)
        self.motorA.run(Adafruit_MotorHAT.FORWARD)
        self.motorB.run(Adafruit_MotorHAT.FORWARD)
        # turn on motor
        self.motorA.run(Adafruit_MotorHAT.RELEASE)
        self.motorB.run(Adafruit_MotorHAT.RELEASE)
        
        
    def turnOffMotors(self):
        print("Turning off motors")
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    def driveForward(self):
        print("Driving forward")
        self.motorA.run(Adafruit_MotorHAT.FORWARD)
        self.motorB.run(Adafruit_MotorHAT.FORWARD)

        self.motorA.setSpeed(self.speed)
        self.motorB.setSpeed(self.speed)

    def driveRevers(self):
        print("Reversing")
        self.motorA.run(Adafruit_MotorHAT.BACKWARD)
        self.motorB.run(Adafruit_MotorHAT.BACKWARD)
        
        self.motorA.setSpeed(self.speed)
        self.motorB.setSpeed(self.speed)

    def pivotLeft(self):
        print("pivoting left")
        self.motorA.run(Adafruit_MotorHAT.FORWARD)
        self.motorB.run(Adafruit_MotorHAT.BACKWARD)
        
        self.motorA.setSpeed(self.speed)
        self.motorB.setSpeed(int(self.speed/2))

    def pivotRight(self):
        print("pivoting right")
        self.motorA.run(Adafruit_MotorHAT.BACKWARD)
        self.motorB.run(Adafruit_MotorHAT.FORWARD)
        
        self.motorA.setSpeed(int(self.speed/2))
        self.motorB.setSpeed(self.speed)
    
    def stop(self):
        print("Stopping")
        self.speed = 0
        self.motorA.setSpeed(self.speed)
        self.motorB.setSpeed(self.speed)

    def speedUp(self):
        print("Speeding up")
        self.speed += 5
    
    def slowDown(self):
        print("Slowing down")
        self.speed -= 5
    
vaccuBot = MotorControl()


# auto-disables motors on shutdown!
atexit.register(vaccuBot.turnOffMotors)




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
                vaccuBot.driveForward()
            elif(key_name == 'A'):
                vaccuBot.pivotLeft()
            elif(key_name == 'S'):
                vaccuBot.driveRevers()
            elif(key_name == 'D'):
                vaccuBot.pivotRight()
            elif(key_name == 'L'):
                vaccuBot.stop()
pygame.quit()

