import RPi.GPIO as GPIO

# Class responsible of the correct movement of the motors
class MotorController:
    def __init__(self,ena,in1,in2,in3,in4,enb,vel): #,IN3,IN4,ENB):
        self.ena = ena
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.enb = enb
        self.velocidad = vel
        self.pwm_a = None
        self.pwm_b = None

    def initialize(self):
        #configura los pines segun el microprocesador Broadcom
        #configura los pines como salidas
        GPIO.setup(self.ena,GPIO.OUT)
        GPIO.setup(self.enb,GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        #Define las salidas PWM q
        self.pwm_a = GPIO.PWM(self.ena,500)
        self.pwm_b = GPIO.PWM(self.enb,500)
        #inicializan los PWM con un duty Cicly de cero
        self.pwm_a.start(0)
        self.pwm_b.start(0)

    def forward(self):
        GPIO.output(self.in1,False)
        GPIO.output(self.in2,True)
        GPIO.output(self.in3,False)
        GPIO.output(self.in4,True)
        self.pwm_a.ChangeDutyCycle(self.velocidad)
        self.pwm_b.ChangeDutyCycle(self.velocidad)

    def backward(self):
        GPIO.output(self.in1,True)
        GPIO.output(self.in2,False)
        GPIO.output(self.in3,True)
        GPIO.output(self.in4,False)
        self.pwm_a.ChangeDutyCycle(self.velocidad)
        self.pwm_b.ChangeDutyCycle(self.velocidad)

    def left(self):
        GPIO.output(self.in1,True)
        GPIO.output(self.in2,False)
        GPIO.output(self.in3,False)
        GPIO.output(self.in4,True)
        self.pwm_a.ChangeDutyCycle(self.velocidad)
        self.pwm_b.ChangeDutyCycle(self.velocidad)

    def rigth(self):
        GPIO.output(self.in1,False)
        GPIO.output(self.in2,True)
        GPIO.output(self.in3,True)
        GPIO.output(self.in4,False)
        self.pwm_a.ChangeDutyCycle(self.velocidad)
        self.pwm_b.ChangeDutyCycle(self.velocidad)

    def stop(self):
        self.pwm_a.ChangeDutyCycle(0)
        self.pwm_b.ChangeDutyCycle(0)
