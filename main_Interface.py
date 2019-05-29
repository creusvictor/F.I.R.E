from Color import * #Red(),Green(),Blue(),Black(),White()
from IRSensor import *
from MotorController import *
from Robot import *
from ServoMotor import *
#from TempHumSensor import *
#from UltrasoundSensor import *
from View import *
from Interface import *
from DummyObject import *
from WebCam import *

# Initialize the interface #
interface = Interface(640,695,100,600,"F.I.R.E. -MAIN(0.1) TEST-",100)
interface.build()
pygame.init()
############################
#GPIO.setmode(GPIO.BOARD)   # BOARD!!!
############################
# Initialize the devices   #
#motorController = MotorController(12,29,31,33,35,26,100) #ENA,IN1,IN2,IN3,IN4,ENB,$
#ultrasoundSensorL = UltrasoundSensor(5,3) #TRIGG,ECHO
#ultrasoundSensorF = UltrasoundSensor(11,7) #TRIGG,ECHO
#ultrasoundSensorR = UltrasoundSensor(15,13) #TRIGG,ECHO
#view = View(23,21) #LRServo,UDServo     [servoLR = ServoMotor(23)YELLOW, servoUD =$
#tempHumL = TempHumSensor(8) #DATA
#tempHumR = TempHumSensor(10) #DATA
#infraRedSen = IRSensor(19) #DATA
#cannon = Cannon(37) #Transistor sign pin -> WE MUST DEFINE THIS CLASS!!!!
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
#motorController.initialize()
#ultrasoundSensorL.initialize()
#ultrasoundSensorF.initialize()
#ultrasoundSensorR.initialize()
while(run):
	pygame.time.delay(interface.delay)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#motorController.stop()
			#GPIO.cleanup()
			run = False

	keys = pygame.key.get_pressed()
	# MOVEMENT #
	if keys[pygame.K_a]:
		#motorController.left()
		textMov = 'MOVING: LEFT'
	if keys[pygame.K_d]:
		#motorController.rigth()
		textMov = 'MOVING: RIGTH'
	if keys[pygame.K_w]:
		#motorController.forward()
		textMov = 'MOVING: FORWARD'
	if keys[pygame.K_s]:
		#motorController.backward()
		textMov = 'MOVING: BACKWARD'
	if keys[pygame.K_q]:
		#motorController.stop()
		textMov = 'MOVING: STOP'

	# CAMERA #
	if keys[pygame.K_DOWN]:
		#view.down()
		textView = 'VIEW: DOWN'
	if keys[pygame.K_LEFT]:
		#view.left()
		textView = 'VIEW: LEFT'
	if keys[pygame.K_RIGHT]:
		#view.right()
		textView = 'VIEW: RIGTH'
	if keys[pygame.K_UP]:
		#view.up()
		textView = 'VIEW: UP'

	# CANNON #
	if keys[pygame.K_SPACE]:
		#cannon.shoot()
		textCannon = 'CANNON: SHOOTING'

	# ULTRASONIC SENSORS #
	#ultrasoundSensorL.getDistance()
	#ultrasoundSensorF.getDistance()
	#ultrasoundSensorR.getDistance()
	#textDistL = ultrasoundSensorL.getText()
	textDistL = 'DIST-L: dfgnhhdmjghfghhgkjhk'
	#textDistF = ultrasoundSensorF.getText()
	textDistF = 'DIST-F: lhgdfscvxbhjygfxhgjs'
	#textDistR = ultrasoundSensorR.getText()
	textDistR = 'DIST-R: mnkbjmhvngbefzvnmbsg'

	# TEMP-HUM SENSORS #
	#textTempL = tempHumL.getvalue()
	textTempL = 'TEMP-L: sdmflkadsndfkjlnfjkl'
	#textTempR = tempHumR.getValue()
	textTempR = 'TEMP-R: dfdsghfhfghgfdzxgdhx'

        # IR SENSOR #
	

        # WEBCAM #
	

        ########### REFRESH THE INTERFACE ###################
	interface.win.fill(Black())

        # Write texts (WE MUST CHECH THE POSITION FOR THE DIFFERENTS TEXTS...)
	interface.writeText(textMov,Green(),Black(),5,5,interface.win)
	interface.writeText(textView,Green(),Black(),5,30,interface.win)
	interface.writeText(textDistL,Green(),Black(),350,30,interface.win)
	interface.writeText(textDistF,Green(),Black(),350,60,interface.win)
	interface.writeText(textDistR,Green(),Black(),350,5,interface.win)
	interface.writeText(textTempL,Green(),Black(),5,60,interface.win)
	interface.writeText(textTempR,Green(),Black(),5,90,interface.win)
	interface.writeText(textCannon,Green(),Black(),350,90,interface.win)

	# Update the display
	interface.refresh()
interface.quit()
############################



