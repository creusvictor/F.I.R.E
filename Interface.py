import pygame

class Interface:
	def __init__(self,screen_high,screen_width,textBox_high,textBox_width,title,delay):
		self.screen_high = screen_high
		self.screen_width = screen_width
		self.textBox_high = textBox_high
		self.textBox_width = textBox_width
		self.title = title
		self.win = None
		self.delay = delay

	def build(self):
		pygame.init()
		self.win = pygame.display.set_mode((self.screen_high,self.screen_width))
		pygame.display.set_caption(self.title)

	def updateSprite(self,sprite):
		pygame.draw.rect(self.win,sprite.color,(sprite.pos_x,sprite.pos_y,sprite.high,sprite.width))

	def refresh(self):
		pygame.display.update()

	def delay(self):
		pygame.time.delay(int(self.delay))

	def quit(self):
		pygame.quit()

	#[5,5],[300,5],[5,35],[300,35]
	def writeText(self,text,frontColor,backColor,pos_x,pos_y,win):
		font = pygame.font.Font('freesansbold.ttf',16)
		text = font.render(text,True,frontColor,backColor)
		textRect = [pos_x,pos_y]
		win.blit(text, textRect)
