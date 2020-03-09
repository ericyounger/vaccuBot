
from MotorControl import MotorControl

import atexit
import time
from worker_thread import Worker
from distanceSense import Sensors
import SensorReadings


class VaccuBot:
    
    
    def __init__(self):
        self.engine = MotorControl()
        self.sensors = Sensors()
        
        
    def callback(number):
        print(number)


if __name__ == "__main__":
    skynet = VaccuBot()
    
    # auto-disables motors on shutdown!
    atexit.register(skynet.engine.turnOffMotors)
    atexit.register(skynet.sensors.killThreads)

    workers = Worker(4)
    workers.start()
    skynet.engine.turnOffMotors()
    #skynet.engine.driveForward()
    while True:
        if(SensorReadings.proximityFront < 20):
            print(SensorReadings.proximityFront)
            skynet.engine.driveReverse()
            time.sleep(0.6)
            skynet.engine.pivotLeft()
            time.sleep(0.4)
            skynet.engine.driveForward()
            
        
        
    




