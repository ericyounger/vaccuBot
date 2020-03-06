
from MotorControl import MotorControl
from distanceSense import Sensors
import atexit
import time

class VaccuBot:

    def __init__(self):
        self.proximityFront = 0
        self.engine = MotorControl()
        self.sensors = Sensors()


if __name__ == "__main__":
    skynet = VaccuBot()

    # auto-disables motors on shutdown!
    atexit.register(skynet.engine.turnOffMotors)

    while True:
        print("calculating distance")
        skynet.proximityFront = skynet.sensors.distance()
        print(skynet.proximityFront)
        time.sleep(1)


