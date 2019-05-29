import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(23,GPIO.OUT)

p = GPIO.PWM(23,50)
p.start(7.5)
t=1
try:
	while True:
		p.ChangeDutyCycle(7.5)
		print("MID")
		time.sleep(t)
		p.ChangeDutyCycle(10)
		print("MID-RIGHT")
		time.sleep(t)
		p.ChangeDutyCycle(12.5)
		print("RIGHT")
		time.sleep(t)
		p.ChangeDutyCycle(2.5)
		print("LEFT")
		time.sleep(t)
		p.ChangeDutyCycle(5)
		print("LEFT-MID")
		time.sleep(t)

except KeyboardInterrupt:
	GPIO.cleanup()
