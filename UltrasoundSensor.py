import RPi.GPIO as GPIO
import time

# Class responsible of the calculate of the distance using the ultrasounds sensors
class UltrasoundSensor:
    def __init__(self,Trig,Echo):
        self.Trig_pin = Trig
        self.Echo_pin = Echo
        self.distance = None
        self.value_echo = 0

    def initialize(self):
        GPIO.setup(self.Trig_pin,GPIO.OUT)
        GPIO.setup(self.Echo_pin,GPIO.IN)

    def getDistance(self):
        print("Distance Measurement in progress")
        GPIO.output(self.Trig_pin, False)
        print("Waiting for sensor to settle")
        time.sleep(2)

        GPIO.output(self.Trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.Trig_pin, False)

        while GPIO.input(self.Echo_pin) == 0:
            pulse_start = time.time()

        while GPIO.input(self.Echo_pin) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        self.distance = pulse_duration*17150
        self.distance = round(self.distance/2)

        #return self.distance

    def getText(self):
        text = "Distance: "+str(self.distance)+"cm"
        return text
