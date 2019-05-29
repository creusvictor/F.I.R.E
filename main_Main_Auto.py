
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
from Cannon import *
from IRSensor import *

import time
import RPi.GPIO as GPIO

# Initialize the interface #
interface = Interface(640,695,100,600,"F.I.R.E. -MAIN_AUTO(0.1) TEST-",100)
interface.build()
pygame.init()
############################
GPIO.setmode(GPIO.BOARD)   # BOARD!!!
############################
# Initialize the devices   #
motorController = MotorController(12,29,31,33,35,26,100) #ENA,IN1,IN2,IN3,IN4,ENB,Velocity(from 0 to 100) 
ultrasoundSensorL = UltrasoundSensor(5,3) #TRIGG,ECHO
ultrasoundSensorF = UltrasoundSensor(11,7) #TRIGG,ECHO
ultrasoundSensorR = UltrasoundSensor(15,13) #TRIGG,ECHO
view = View(23,21) #LRServo,UDServo     [servoLR = ServoMotor(23)YELLOW, servoUD = ServoMotor(21)YELLOW]   
tempHumL = TempHumSensor(8) #DATA
tempHumR = TempHumSensor(10) #DATA
irSensor = IRSensor(19) #DATA
cannon = Cannon(37)
webcam = WebCam()
############################

#-#-#    MAIN  LOOP    #-#-#
textMov = 'MOVING: STOP'
textView = 'VIEW: CENTER'
textCannon = 'CANNON: STOPPED'
textTempL = '_'
textTempR = '_'
textDistL = '_'
textDistF = '_'
textDistR = '_'
run = True
motorController.initialize()
ultrasoundSensorL.initialize()
ultrasoundSensorF.initialize()
ultrasoundSensorR.initialize()
webcam.start()
record = False
img = None
##########################
first = True # <-
tempL = 0
tempR = 0
distL = 0
distF = 0
distR = 0
IRLecture = 0
#########################
while(run):
    pygame.time.delay(interface.delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            motorController.stop()
            GPIO.cleanup()
            run = False
###############
	tempL = tempHumL.getTemp()
	tempR = tempHumR.getTemp()
	if(tempL>tempR):
		motorController.left()
		textMov = 'MOVING: LEFT'
		time.wait(2)
		motorController.stop()
		textMov = 'MOVING: STOPED'
	else:
		motorController.rigth()
		textMov = 'MOVING: RIGTH'
		time.wait(2)
		motorController.stop()
		textMov = 'MOVING: STOPED'
	distL = ultrasoundSensorL.getDist()
	distF = ultrasoundSensorL.getDist()
	distR = ultrasoundSensorL.getDist()
	textDistL = ultrasoundSensorL.getText()
        textDistF = ultrasoundSensorF.getText()
        textDistR = ultrasoundSensorR.getText()
	if(webcam.isFire()):
		IRLecture = irSensor.getValue
		if(IRLecture>100):
			img = webcam.darknet()
			interface.win.blit(img,(0,200))
			textCannon = 'CANNON: SHOOTING'
			interface.writeText(textCannon,Green(),Black(),350,90,interface.win)
			cannon.fire()
			textCannon = 'CANNON: STOPED'
			interface.writeText(textCannon,Green(),Black(),350,90,interface.win)
	else:
		if((distL>10)and(distF>10)and(distR>10))
			motorController.forward()
			time.wait((distF/10))
			motorController.stop()
	img = webcam.takeImage()
	interface.win.blit(img,(0,200))
    ########### REFRESH THE INTERFACE ###################

    # Write texts (WE MUST CHECH THE POSITION FOR THE DIFFERENTS TEXTS...)
    interface.writeText(textMov,Green(),Black(),5,5,interface.win)
    interface.writeText(textView,Green(),Black(),5,30,interface.win)
    interface.writeText(textDistL,Green(),Black(),350,30,interface.win)
    interface.writeText(textDistF,Green(),Black(),350,60,interface.win)
    interface.writeText(textDistR,Green(),Black(),350,5,interface.win)
    interface.writeText(textTempL,Green(),Black(),5,60,interface.win)
    interface.writeText(textTempR,Green(),Black(),5,90,interface.win)

    # Update the display
    interface.refresh()
interface.quit()
############################
