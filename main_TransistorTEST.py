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

import RPi.GPIO as GPIO
# Initialize the interface #
interface = Interface(300,300,100,600,"F.I.R.E. -UltrasoundSensor TEST-",100)
interface.build()
pygame.init()
############################
GPIO.setmode(GPIO.BOARD)   # BOARD!!!
############################
# Initialize the transistor#
GPIO.setup(37,GPIO.OUT)
############################

#-#-#    MAIN  LOOP    #-#-#
text = '_'
run = True
#ultrasoundSensor.initialize()
while(run):
	pygame.time.delay(interface.delay)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		GPIO.output(37,True)
		text = 'WATER: shoting'
	if keys[pygame.K_q]:
		GPIO.output(37,False)
		text = 'WATER: stopped'

	interface.win.fill(Black())

	# Write some text
	interface.writeText(text,Green(),Black(),5,5,interface.win)

	# Update the display
	interface.refresh()
interface.quit()
############################
