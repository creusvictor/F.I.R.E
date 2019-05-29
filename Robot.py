# Class responsible of keep track on the mode of the execution (for now... maybe we can merge all the other classes inside this one... TAKE A LOOK)
class Robot:
	def __init__(self):
		self.manualMode = True
		self.run = True
	def isManual(Self):
		return self.manualMode
	def setManualMode(self):
		self.manualMode = True
	def setAutoMode(self):
		self.manualMode = False
	def turnOff(self):
		self.run = False
