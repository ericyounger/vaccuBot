
from MotorControl import MotorControl
from distanceSense import Sensors
import atexit
import time
from worker_thread import Worker

class VaccuBot:

    def __init__(self):
        self.proximityFront = 0
        self.engine = MotorControl()
        self.sensors = Sensors()


if __name__ == "__main__":
    skynet = VaccuBot()

    # auto-disables motors on shutdown!
    atexit.register(skynet.engine.turnOffMotors)

    workers = Worker(4)
    workers.start()


    while True:
        print("calculating distance")
        
        print(skynet.proximityFront)
        time.sleep(1)
        workers.post(print(skynet.sensors.distance))


