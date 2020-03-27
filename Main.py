import Drone
import time
#here you should interact with the drone

voresDrone = Drone.Drone("192.168.10.1", 8889)

isConnected = voresDrone.connect()
if (isConnected != 'Did not work'):
    time.sleep(2)

    voresDrone.takeOff()
    time.sleep(2)

    voresDrone.down(90)
    time.sleep(2)

    voresDrone.StaircaseClimbing(170, 210, [5,5,5], 19)

    voresDrone.land()