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
interface = Interface(1200,800,100,600,"F.I.R.E.",100)
interface.build()
pygame.init()
############################
#  Initialize the Web Cam  #
webcam = WebCam('/dev/video0',200,200,'capture.png')

# Initialize the DummyObj. #
dummyObj = DummyObject(150,150,40,40,5,Red())
############################

#-#-#    MAIN  LOOP    #-#-#
run = True
while(run):
	pygame.time.delay(interface.delay)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT] and dummyObj.pos_x>dummyObj.vel:
		dummyObj.left()
	if keys[pygame.K_RIGHT] and dummyObj.pos_x<(interface.screen_width-dummyObj.high-dummyObj.vel):
		dummyObj.rigth()
	if keys[pygame.K_UP] and dummyObj.pos_y>dummyObj.vel+interface.textBox_high:
		dummyObj.up()
	if keys[pygame.K_DOWN] and dummyObj.pos_y<(interface.screen_high-dummyObj.width-dummyObj.vel):
		dummyObj.down()
	interface.win.fill(Black())

	# Record WebCam
	#webcam.camstream(interface.win)

	# Draw the dummyObj
	interface.updateSprite(dummyObj)

	# Write some text
	text = 'Some_Text_TEST: '+str(run)
	interface.writeText(text,Green(),Black(),5,5,interface.win)

	# Update the display
	interface.refresh()
interface.quit()
############################
