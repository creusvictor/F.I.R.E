from ServoMotor import *

# CLass responsible of move the 'view' of the robot (move the comeras that are recording the image)
#servoUD = ServoMotor(21) #YELLOW
#servoLR = ServoMotor(23) #YELLOW
class View:
    def __init__(self,LRServo,UDServo):
        self.servoLR = ServoMotor(LRServo)
        self.servoUD = ServoMotor(UDServo)

    def initialize(self):
        self.servoLR.initialize()
        self.servoUD.initialize()

    def up(self):
        tempPos = self.servoUD.pos
        if(tempPos<4):
            tempPos = tempPos+1
            self.servoUD.setPos(tempPos)

    def down(self):
        tempPos = self.servoUD.pos
        if(tempPos>0):
            tempPos = tempPos-1
            self.servoUD.setPos(tempPos)

    def left(self):
        tempPos = self.servoLR.pos
        if(tempPos>0):
            tempPos = tempPos-1
            self.servoLR.setPos(tempPos)

    def right(self):
        tempPos = self.servoLR.pos
        if(tempPos<4):
            tempPos = tempPos+1
            self.servoLR.setPos(tempPos)
