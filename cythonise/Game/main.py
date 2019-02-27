import pygame
import random
from blob_class import Blob

BLUE_BLOBS = 10
RED_BLOBS = 3

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class BlueBlob(Blob):
	def __init__(self, window_width, window_height):
		super(BlueBlob, self).__init__(BLUE, window_width, window_height)
		
	def move_fast(self):
		self.x += random.randrange(-7, 7)
		self.y += random.randrange(-7, 7)

class RedBlob(Blob):
	def __init__(self, window_width, window_height):
		super(RedBlob, self).__init__(RED, window_width, window_height)
		
	def move_fast(self):
		self.x += random.randrange(-7, 7)
		self.y += random.randrange(-7, 7)


def draw_env(blob_list):
	game_display.fill(WHITE)
	for blobs in blob_list:
		for blob in blobs.values():
			pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
			blob.move_fast()
			blob.check_boundery()
	pygame.display.update()


def main():
	red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for blob in range(RED_BLOBS)]))
	blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for blob in range(BLUE_BLOBS)]))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		draw_env([blue_blobs, red_blobs])	
		clock.tick(60)

if __name__ == '__main__':
	main()


