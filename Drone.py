import socket
import sys
import time


class Drone(object):
    """description of class"""
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.Host = ''
        self.HostPort = 9000
        self.locaddr = (self.Host, self.HostPort)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = (self.ip, self.port)
        self.sock.bind(self.locaddr)

    def sendBesked(self,TelloMessage):
        try:   
            #print("send message "+ TelloMessage +" end")
            msg = TelloMessage.encode(encoding="utf-8")
            sent = self.sock.sendto(msg, self.tello_address)
            data, server = self.sock.recvfrom(1518)

            #print(data.decode(encoding="utf-8"))
            return "Succes"
        except:
            return "Did not work"    

    def connect(self):
        print("Forbinder")
        resultat = self.sendBesked("command")
        print(resultat)
        return resultat

    def takeOff(self):
        print("takeOff")
        resultat = self.sendBesked("takeoff")
        print(resultat)

    def forward(self, value):
        print("frem "+str(value))
        resultat = self.sendBesked("forward "+str(value))
        print(resultat)

    def back(self, value):
        print("tilbage "+str(value))
        resultat = self.sendBesked("back "+str(value))
        print(resultat)
    
    def left(self, value):
        print("venstre "+str(value))
        resultat = self.sendBesked("left "+str(value))
        print(resultat)

    def right(self, value):
        print("hojre "+str(value))
        resultat = self.sendBesked("right "+str(value))
        print(resultat)

    def land(self):
        print("lander")
        resultat = self.sendBesked("land")
        print(resultat)
    
    def turn_cw(self, value):
        print("drejer med uret "+str(value))
        resultat = self.sendBesked("cw "+str(value))
        print(resultat)

    def turn_ccw(self, value):
        print("drejer mod uret "+str(value))
        resultat = self.sendBesked("ccw"+str(value))
        print(resultat)

    def up(self, value):
        print("op "+str(value))
        resultat = self.sendBesked("up "+str(value))
        print(resultat)
    
    def down(self, value):
        print("ned "+str(value))
        resultat = self.sendBesked("down "+str(value))
        print(resultat)

    def StaircaseClimbing(self, stair_length, stair_width, steps, step_height):
        # steps i formen = [5, 5, 5] så vi specificerer at der er 3 længder med 5 trin hver, den skal klatre
        
        step_length = 0.0
        for i in range(len(steps)):
            if (i % 2 == 0):
                step_length = float(stair_length) / steps[i]
            else:
                step_length = float(stair_width - 20) / steps[i]
            
            for j in range(steps[i]):
                self.up(step_height)
                time.sleep(1)

                if (j == 0):
                    self.forward(step_length - 5)
                    time.sleep(1)
                elif (j == steps[i]-1):
                    self.forward(step_length + 5)
                    time.sleep(1)
                    if (i != len(steps)-1):
                        self.turn_ccw(90)
                        time.sleep(1)
                else:
                    self.forward(step_length)
                    time.sleep(1)

    