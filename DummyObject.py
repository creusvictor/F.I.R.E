class DummyObject:
	def __init__(self,pos_x,pos_y,high,width,vel,color):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.high = high
		self.width = width
		self.vel = vel
		self.color = color
		self.temperature = 0
		self.shootingWater = False
		self.autoMode = False

	def setColor(self,color):
		self.color = color

	def left(self):
		self.pos_x -= self.vel
	def rigth(self):
		self.pos_x += self.vel
	def up(self):
		self.pos_y -= self.vel
	def down(self):
		self.pos_y += self.vel
