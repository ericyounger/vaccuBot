#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import keyboard



class MotorControl(object):
    
    def __init__(self):
        #setup motors, and communication with motorHAT
        # create a default object, no changes to I2C address or frequency
        self.mh = Adafruit_MotorHAT(addr=0x60)
        
        ################################# Set motors
        self.motorA = self.mh.getMotor(1)
        self.motorB = self.mh.getMotor(2)
        
        # set the speed to start, from 0 (off) to 255 (max speed)
        self.motorA.setSpeed(150)
        self.motorB.setSpeed(150)
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

        self.motorA.setSpeed(200)
        self.motorB.setSpeed(200)

    

    def driveRevers(self):
        print("Reversing")
        self.motorA.run(Adafruit_MotorHAT.BACKWARD)
        self.motorB.run(Adafruit_MotorHAT.BACKWARD)
        
        self.motorA.setSpeed(200)
        self.motorB.setSpeed(200)


    def pivotLeft(self):
        print("pivoting left")
        self.motorA.run(Adafruit_MotorHAT.FORWARD)
        self.motorB.run(Adafruit_MotorHAT.BACKWARD)
        
        self.motorA.setSpeed(200)
        self.motorB.setSpeed(100)

    def pivotRight(self):
        print("pivoting right")
        self.motorA.run(Adafruit_MotorHAT.BACKWARD)
        self.motorB.run(Adafruit_MotorHAT.FORWARD)
        
        self.motorA.setSpeed(100)
        self.motorB.setSpeed(200)
    
    def stop(self):
        self.motorA.setSpeed(0)
        self.motorB.setSpeed(0)
    




    


vaccuBot = MotorControl()


# recommended for auto-disabling motors on shutdown!
atexit.register(vaccuBot.turnOffMotors)

while True:
    if(keyboard.is_pressed("w")):
       vaccuBot.driveForward()
    if(keyboard.is_pressed("s")):
        vaccuBot.driveRevers()
    if(keyboard.is_pressed("a")):
        vaccuBot.pivotLeft()
    if(keyboard.is_pressed("d")):
        vaccuBot.pivotRight()
    if(keyboard.is_pressed(",")):
        vaccuBot.stop()