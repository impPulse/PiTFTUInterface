#!/usr/bin/python
# -*-coding:UTF8 -*

"""Module de gestion de l'interface graphique et de l'affichage."""

import sys
import pygame
import time
import os
import random
import pygame.locals as GLOBALS
import pygame.event as EVENTS


#Variable pour la prise en charge du PiTFT RT 2.8

os.environ["SDL_VIDEODRIVER"]= "fbcon"
os.environ["SDL_FBDEV"]= "/dev/fb1"
os.environ["SDL_MOUSEDEV"]= "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"]= "TSLIB"

size = width, height = 320,240

#Set de couleur

noir  =   0,   0,   0
magen = 255,   0, 255
rouge = 255,   0,   0
jaune = 255, 255,   0
vert  =   0, 255,   0
cyan  =   0, 255, 255
bleu  =   0,   0, 255
blanc = 255, 255, 255
gris  = 100, 100, 100

#Surface d'affichage

pygame.init()
screen = pygame.display.set_mode((size), GLOBALS.FULLSCREEN)
pygame.mouse.set_visible(0)

# BootScreen

fond = pygame.image.load("fond.jpg")
screen.blit(fond, (0,0))
pygame.display.flip()
time.sleep(1)

# Animation

carreRougeX   =  49; carreRougeY   =  49
carreVertX    = 159; carreVertY    = 159
carreBleuX    = 269; carreBleuY    =  49
carreCyanX    = 269; carreCyanY    = 159
carreMagentaX = 159; carreMagentaY =  49
carreJauneX   =  49; carreJauneY   = 159
carreSizeX = 10
carreSizeY = 10
carreVX = 1
carreVY = 1
#couleur = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

#Menu

def menu():
  screen.fill(noir)
  pygame.draw.rect(screen, rouge, (0,0,100,100))
  pygame.draw.rect(screen, vert, (110,110,100,100))
  pygame.draw.rect(screen, bleu, (220,0,100,100))
  pygame.draw.rect(screen, cyan, (220,110,100,100))
  pygame.draw.rect(screen, magen, (110,0,100,100))
  pygame.draw.rect(screen, jaune, (0,110,100,100))
  pygame.draw.rect(screen, blanc, (0,214,320,30))
  pygame.display.update()
  

#Main Loop

while 1:

  if carreSizeX <= 100:
    pygame.draw.rect(screen, rouge, (carreRougeX - carreSizeX / 2, carreRougeY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen,  vert, (carreVertX - carreSizeX / 2, carreVertY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen,  bleu, (carreBleuX - carreSizeX / 2, carreBleuY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen,  cyan, (carreCyanX - carreSizeX / 2, carreCyanY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen, magen, (carreMagentaX - carreSizeX / 2, carreMagentaY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen, jaune, (carreJauneX - carreSizeX / 2, carreJauneY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.display.update()
  if carreSizeX <= 100:
    carreSizeX += carreVX
  if carreSizeY <= 100:
    carreSizeY += carreVY 

  if carreSizeX >= 100 and carreSizeY >=100:
    menu()

  for event in EVENTS.get():
    if event.type == GLOBALS.KEYDOWN:
      if event.key == GLOBALS.K_ESCAPE:
        sys.exit()

