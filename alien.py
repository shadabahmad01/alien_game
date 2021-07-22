import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" class to represent a single aien in fleet"""

	def __init__(self,ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		#load the alien image
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		#start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store alien's exact horizontal position
		self.x = float(self.rect.x)

	def check_edges(self):
		"""return true if alien is at edge of screen"""
		screen_rect = self.screen.get_rect()

		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True

	def update(self):
		"""move alien to the right"""
		self.x += (self.settings.alein_speed*self.settings.fleet_direction)
		self.rect.x = self.x