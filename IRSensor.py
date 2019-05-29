# Class responsible of read the amount of IR that we recive into the sensor
class IRSensor:
	def __init__(self, pin):
		self.sign_pin = pin
		self.value = 0
	def getValue(self):
		return self.value
