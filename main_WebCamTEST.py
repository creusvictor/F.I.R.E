from Color import * #Red(),Green(),Blue(),Black(),White()
from IRSensor import *
#from MotorController import *
from Robot import *
#from ServoMotor import *
#from TempHumSensor import *
#from UltrasoundSensor import *
from View import *
from Interface import *
from DummyObject import *
from WebCam import *

# Initialize the interface #
interface = Interface(640,840,100,600,"F.I.R.E. -WebCam TEST-",100)
interface.build()
pygame.init()
############################
# Initialize the WebCam    #
webcam = WebCam()
############################

#-#-#    MAIN  LOOP    #-#-#
text = 'CAMERA_STATE:'
txt=' '
run = True
webcam.start()
record = False
img = None
while(run):
	pygame.time.delay(interface.delay)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE]:
		if(record):
			record = False
			txt = (text+' '+str(record))
		else:
			record = True
			txt = (text+' '+str(record))
	if(record):
		if keys[pygame.K_o]:
			record = False
			txt = (text+' '+'Darknet: Executing!')
			interface.writeText(txt,Green(),Black(),5,5,interface.win)
			interface.refresh()
			img = webcam.darknet()
			txt = (text+' '+'Darknet: Finished! ')
		else:
			img = webcam.takeImage()
			#img = webcam.captureImage(interface.win)
		interface.win.blit(img,(0,200))
	#interface.win.fill(Black())

	# Write some text
	interface.writeText(txt,Green(),Black(),5,5,interface.win)

	# Update the display
	interface.refresh()
interface.quit()
############################
