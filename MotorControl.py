#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time

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
        self.motorB.setSpeed(self.speed)

    def pivotRight(self):
        print("pivoting right")
        self.motorA.run(Adafruit_MotorHAT.BACKWARD)
        self.motorB.run(Adafruit_MotorHAT.FORWARD)
        
        self.motorA.setSpeed(self.speed)
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
    



