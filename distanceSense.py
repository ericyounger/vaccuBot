import RPi.GPIO as gpio
import time


def distance():
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
        return distance

    except:
        distance = 100
        gpio.cleanup()
        return distance


if __name__ == "__main__":
    print(distance())
