import RPi.GPIO as GPIO
import time


class Cannon:
    def __init__(self,pin):
        self.sign_ON = pin

    def initialize(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.sign_ON,GPIO.OUT)
        GPIO.output(self.sign_ON,False)

    def shoot(self):
        GPIO.setup(self.sign_ON,GPIO.OUT)
        GPIO.output(self.sign_ON,True)
        time.sleep(2)
        GPIO.output(self.sign_ON,False)

