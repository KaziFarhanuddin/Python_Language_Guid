import random

window_width = 800
window_height = 600

class Blob():
	def __init__(self, color, window_width, window_height, size=random.randrange(4, 8)):
		self.color = color
		self.x = random.randrange(0, window_width)
		self.y = random.randrange(0, window_height)
		self.size = size

	def move(self):
		self.move_x = random.randrange(-1, 2)
		self.move_y = random.randrange(-1, 2)
		self.x += self.move_x
		self.y += self.move_y

	def check_boundery(self):
		if self.x < 0: self.x = 0
		elif self.x > window_width: self.x = window_width

		if self.y < 0: self.y = 0
		elif self.y > window_height: self.y = window_height