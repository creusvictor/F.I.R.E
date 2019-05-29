import RPi.GPIO as GPIO
import time

# Class responsible of set the rotation for the servo
class ServoMotor:
    def __init__(self,pin):
        self.sign_pin = pin
        self.pos = 2
               
    def setPos(self,pos): #[0,1,2,3,4] => [L,LM,M,MR,R],[D,DM,M,MU,U]
        GPIO.setup(self.sign_pin,GPIO.OUT)
        p = GPIO.PWM(self.sign_pin,50)
        p.start(7.5)
        self.pos = pos
        print(self.pos)
        if(self.pos==0):
            p.ChangeDutyCycle(2.5)
            time.sleep(1)
        if(self.pos==1):
            p.ChangeDutyCycle(5)
            time.sleep(1)
        if(self.pos==2):
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
        if(self.pos==3):
            p.ChangeDutyCycle(10)
            time.sleep(1)
        if(self.pos==4):
            p.ChangeDutyCycle(12.5)
            time.sleep(1)
        