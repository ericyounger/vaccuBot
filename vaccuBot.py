
import MotorControl
import Sensors


class VaccuBot:

    def __init__(self):
        self.engine = MotorControl()
        self.sensors = Sensors()


if __name__ == "__main__":
    skynet = VaccuBot()

    # auto-disables motors on shutdown!
    atexit.register(skynet.engine.turnOffMotors)


    skynet.sensors.distance()


