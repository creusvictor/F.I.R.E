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

# Initialize the interface #
interface = Interface(300,300,100,600,"F.I.R.E. -TempHumSensor TEST-",100)
interface.build()
pygame.init()
############################
# Initialize the ServoMot. #
servoMotor = ServoMotor(11) #FALTA poner el pin!
############################

#-#-#    MAIN  LOOP    #-#-#
text = " "
run = True
servoMotor.initialize()
#while(run):
#	pygame.time.delay(interface.delay)

#	for event in pygame.event.get():
#		if event.type == pygame.QUIT:
#			run = False

#	keys = pygame.key.get_pressed()
#	if keys[pygame.K_LEFT]:
servoMotor.setAngle(50)
#		text = 'Decresing angle'
#	if keys[pygame.K_RIGHT]:
#		servoMotor.setAngle(90)
#		text = 'Incrissing angle'

#	interface.win.fill(Black())

	# Write some text
#	interface.writeText(text,Green(),Black(),5,5,interface.win)

#	# Update the display
#	interface.refresh()
#interface.quit()
############################
