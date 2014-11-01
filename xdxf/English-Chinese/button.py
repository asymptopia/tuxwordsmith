"""
/**********************************************************

    Organization    :AsymptopiaSoftware | Software@theLimit

    Website         :www.asymptopia.org

    Author          :Charles B. Cosse

    Email           :ccosse@gmail.com

    Copyright       :(C) 2006-2008 Asymptopia Software

    License         :GPL2

***********************************************************/
"""

import pygame,os
from pygame.locals import *

class Button(pygame.sprite.Sprite):
	def __init__(self,fname):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(fname)
		self.rect=self.image.get_rect()
	
	def get_height(self):
		return self.rect[3]-self.rect[1]	
	
	def get_width(self):
		return self.rect[2]-self.rect[0]	
