#!/usr/bin/env python
# -*- coding:UTF-8 -*

import os
import pygame
from pygame.locals import *

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
os.putenv('SDL_MOUSEDRV', 'TSLIB')

size = width, height = 320, 240

space = widthS, heightS = 320, 210
spaceO = spaceX, spaceY = 0, 0

dock = widthD, heightD = 320, 30
dockO = dockX, dockY = 0, 210

noir = 0, 0, 0
gris = 100, 100, 100
blanc = 255, 255, 255

path = '/home/pi/'

pygame.init()

pygame.mouse.set_visible(0)

screen = pygame.display.set_mode((size), pygame.FULLSCREEN)
screen.fill(blanc)
pygame.display.update()

clock = pygame.time.Clock()

class Interface:

  def __init__(self, size, pos, couleur, mode):
    self.size = size
    self.pos = pos
    self.couleur = couleur
    self.mode = mode

  def afficher(self):
    pygame.draw.rect(screen, self.couleur, (self.pos[0], self.pos[1], self.size[0], self.size[1])) 


S = Interface(space, spaceO, gris, 0)
D = Interface(dock, dockO, noir, 0)

S.afficher()
D.afficher()

pygame.display.update()

pygame.time.wait(2000)
