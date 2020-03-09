import RPi.GPIO as gpio
import time
import SensorReadings
import threading


class Sensors:
    
    def __init__(self):
        self.runThreads = True
        self.proximitySensor = threading.Thread(target=self.distance)
        self.proximitySensor.start()
        SensorReadings.proximityFront = 404.00 #start value as in not found
    
    def killThreads(self):
        self.runThreads = False
        self.proximitySensor.join()

    def distance(self):
        while self.runThreads:
            TRIG = 12
            ECHO = 16
            try:
                gpio.setmode(gpio.BOARD) # OR BCM depending on layout chosen
                gpio.setup(TRIG, gpio.OUT)
                gpio.setup(ECHO, gpio.IN)
                gpio.output(TRIG, False)

                while gpio.input(ECHO) == 0:
                    start = time.time()

                while gpio.input(ECHO) == 1:
                    stop = time.time()

                duration = stop - start
                distance = duration / 0.000058

                gpio.cleanup()
                SensorReadings.proximityFront = (round(distance,2))
           

            except:
                distance = 100
                gpio.cleanup()
                return distance
                


