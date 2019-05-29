from Color import * #Red(),Green(),Blue(),Black(),White()
from IRSensor import *
from MotorController import *
from Robot import *
from ServoMotor import *
from TempHumSensor import *
from UltrasoundSensor import *
from View import *
from Interface import *
from DummyObject import *
from WebCam import *

import time
import RPi.GPIO as GPIO

# Initialize the interface #
interface = Interface(300,300,100,600,"F.I.R.E. -MotorController TEST-",100)
interface.build()
pygame.init()
############################
GPIO.setmode(GPIO.BOARD)   # BOARD!!!
############################
# Initialize the devices   #
motorController = MotorController(12,16,18,22,24,26,100) #ENA,IN1,IN2,IN3,IN4,ENB,Velocity(from 0 to 100)
ultrasoundSensorL = UltrasoundSensor(5,3) #TRIGG,ECHO
ultrasoundSensorF = UltrasoundSensor(11,7) #TRIGG,ECHO
ultrasoundSensorR = UltrasoundSensor(15,13) #TRIGG,ECHO
servoUD = ServoMotor(23) #YELLOW
servoLR = ServoMotor(21) #YELLOW
tempHumL = TempHumSensor(8) #DATA
tempHumR = TempHumSensor(10) #DATA
############################

#-#-#    MAIN  LOOP    #-#-#
text = '_'
run = True
motorController.initialize()
while(run):
	pygame.time.delay(interface.delay)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			motorController.stop()
			GPIO.cleanup()
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		motorController.left()
		text = 'MOVING: LEFT'
	if keys[pygame.K_RIGHT]:
		motorController.rigth()
		text = 'MOVING: RIGTH'
	if keys[pygame.K_UP]:
		motorController.forward()
		text = 'MOVING: FORWARD'
	if keys[pygame.K_DOWN]:
		motorController.backward()
		text = 'MOVING: BACKWARD'
	if keys[pygame.K_q]:
		motorController.stop()
		text = 'MOVING: STOP'

	interface.win.fill(Black())

	# Write some text
	interface.writeText(text,Green(),Black(),5,5,interface.win)

	# Update the display
	interface.refresh()
interface.quit()
############################
