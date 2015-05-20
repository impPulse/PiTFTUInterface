#!/usr/bin/python
# -*-coding:UTF8 -*

"""Module de gestion de l'interface graphique et de l'affichage."""

import sys
import pygame
import time
import os
import os.path
import fnmatch
import pygame.locals as GLOBALS
import pygame.event as EVENTS

class Icones:

  def __init__(self, name):
    self.name = name

    try:
      self.bitmap = pygame.image.load(icons + '/' + name + '.png')
    except:

      pass

class Bouton:

  def __init__(self, rect, **kwargs):
    self.rect = rect
    self.couleur = None
    self.nom = None
    self.callback = None

    for key, value in kwargs.iteritems():

      if   key == 'couleur' : self.couleur = value
      elif key == 'nom'     : self.nom     = value
      elif key == 'callBack': self.callback= value

  def selection(self, posX, posY):
    x1 = self.rect[0]
    y1 = self.rect[1]
    x2 = x1 + self.rect[2]
    y2 = y1 + self.rect[3]

    if (posX >= x1) and (posX <= x2) and (posY >= y1) and (posY <= y2):

      if self.callback != None:
        self.callback()

  def afficher(self, screen):
    if self.couleur:
      screen.fill(self.couleur, self.rect)

    if self.nom:
      for i in iconsList:

        if self.nom == i.name:
          screen.blit(i.bitmap, (self.rect[0], self.rect[1]))

class Image:

  def __init__(self, fichier):
    self.fichier = fichier
    self.image = pygame.image.load(fichier)
    screen.blit(self.image, (0, 0))

#CALLBACK

def contact():
  texte('contact', 0, 0, blancF)
  pygame.display.update()

def player():
  global screenMode, dockMode
  screenMode = 1
  dockMode =1

def lastSnap():
  Image("test.jpg")
  pygame.display.update()
  time.sleep(2)

def camera():
  global screenMode, dockMode
  screenMode = 2
  dockMode = 1

def photo():
  os.system("raspistill -t 500 -o test.jpg")

def video():
  os.system("raspivid -t 5000 -o test.h264")

def reglages():
  global screenMode, dockMode
  screenMode = 3
  dockMode = 1

def home():
  global screenMode, dockMode
  screenMode = 0
  dockMode = 0

def quitter():
  pygame.quit()
  sys.exit()

#Variable pour la prise en charge du PiTFT RT 2.8

os.environ["SDL_VIDEODRIVER"]= "fbcon"
os.environ["SDL_FBDEV"]= "/dev/fb1"
os.environ["SDL_MOUSEDEV"]= "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"]= "TSLIB"

size = width, height = 320,240

#Variables globales

screenMode = 0
dockMode = 0
icons = 'icones'
tailleIcone = 26

#Set de couleur

noir  =   0,   0,   0
magen = 230,   0, 230
rouge = 230,   0,   0
jaune = 230, 230,   0
vert  =   0, 230,   0
cyan  =   0, 230, 230
bleu  =   0,   0, 230
blanc = 230, 230, 230

magenF = 255,   0, 255
rougeF = 255,   0,   0
jauneF = 255, 255,   0
vertF  =   0, 255,   0
cyanF  =   0, 255, 255
bleuF  =   0,   0, 255
blancF = 255, 255, 255

gris  = 100, 100, 100

#Icones

iconsList = []

#Boutons

boutons = [
  #Ecran d'accueil
  [Bouton((  0,  0,100,100), couleur = rouge, nom = 'contacts' , callBack = contact),
   Bouton((110,110,100,100), couleur =  vert, nom = 'camera'   , callBack = camera),
   Bouton((220,  0,100,100), couleur =  bleu, nom = 'player'   , callBack = player),
   Bouton((220,110,100,100), couleur =  cyan, nom = 'jeux'     ),
   Bouton((110,  0,100,100), couleur = magen, nom = 'clavier'  ),
   Bouton((  0,110,100,100), couleur = jaune, nom = 'reglages' , callBack = reglages),
   Bouton((  2,212,317, 26), couleur =  gris, nom = 'dock'     )
  ],
  #Player
  [Bouton((  0,  0,100,100), couleur = rouge, nom = 'prev'    ),
   Bouton((110,110,100,100), couleur =  vert, nom = 'play'    , callBack = lastSnap),
   Bouton((220,  0,100,100), couleur =  bleu, nom = 'next'    ),
   Bouton((220,110,100,100), couleur =  cyan, nom = 'stop'    ),
   Bouton((110,  0,100,100), couleur = magen, nom = 'pause'   ),
   Bouton((  0,110,100,100), couleur = jaune, nom = 'reglages'),
   Bouton((  2,212,317, 26), couleur =  gris, nom = 'dock'     )
  ],
  #Camera
  [Bouton((  0,  0,100,100), couleur = rouge, nom = 'iso'     ),
   Bouton((110,110,100,100), couleur =  vert, nom = 'photo'   , callBack = photo),
   Bouton((220,  0,100,100), couleur =  bleu, nom = 'scene'   ),
   Bouton((220,110,100,100), couleur =  cyan, nom = 'wb'      ),
   Bouton((110,  0,100,100), couleur = magen, nom = 'video'   , callBack = video),
   Bouton((  0,110,100,100), couleur = jaune, nom = 'reglages'),
   Bouton((  2,212,317, 26), couleur =  gris, nom = 'dock'     )
  ],
  #Reglages
  [Bouton((  0,  0,100,100), couleur = rouge, nom = 'fichiers' ),
   Bouton((110,110,100,100), couleur =  vert, nom = 'user'     ),
   Bouton((220,  0,100,100), couleur =  bleu, nom = 'volume'   ),
   Bouton((220,110,100,100), couleur =  cyan, nom = 'affichage'),
   Bouton((110,  0,100,100), couleur = magen, nom = 'reseau'   ),
   Bouton((  0,110,100,100), couleur = jaune, nom = 'console'  ),
   Bouton((  2,212,317, 26), couleur =  gris, nom = 'dock'     )
  ]
]

#Docks

docks = [
  #Accueil
  [Bouton((((width / 2) - (tailleIcone / 2)),(height - tailleIcone), tailleIcone, tailleIcone), nom = 'exit', callBack = quitter),
   Bouton(((((width / 2) - (tailleIcone / 2)) - tailleIcone),(height - tailleIcone), tailleIcone, tailleIcone), nom = 'volm', callBack = quitter),
   Bouton(((((width / 2) - (tailleIcone / 2)) + tailleIcone),(height - tailleIcone), tailleIcone, tailleIcone), nom = 'volp', callBack = quitter)
  ],
  #Menus
  [Bouton((((width / 2) - (tailleIcone / 2)),(height - tailleIcone), tailleIcone, tailleIcone), nom = 'home', callBack = home)
  ]
]

#Surface d'affichage

pygame.init()

screen = pygame.display.set_mode((size), GLOBALS.FULLSCREEN)

positionPointeur = width / 2, height / 2

pygame.mouse.set_visible(0)

# BootScreen

fond = pygame.image.load("fond.jpg").convert()
screen.blit(fond, (0,0))

pygame.display.flip()
time.sleep(1)

for file in os.listdir(icons):
  if fnmatch.fnmatch(file, '*.png'):
    iconsList.append(Icones(file.split('.')[0]))

#FONCTIONS

# Animation

def splash():
  screen.fill(noir)

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

  while carreSizeX <= 100:
    pygame.draw.rect(screen, rougeF, (carreRougeX - carreSizeX / 2, carreRougeY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen,  vertF, (carreVertX - carreSizeX / 2, carreVertY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen,  bleuF, (carreBleuX - carreSizeX / 2, carreBleuY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen,  cyanF, (carreCyanX - carreSizeX / 2, carreCyanY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen, magenF, (carreMagentaX - carreSizeX / 2, carreMagentaY - carreSizeY / 2, carreSizeX, carreSizeY))
    pygame.draw.rect(screen, jauneF, (carreJauneX - carreSizeX / 2, carreJauneY - carreSizeY / 2, carreSizeX, carreSizeY))

    if carreSizeX <= 100:
      carreSizeX += carreVX

    if carreSizeY <= 100:
      carreSizeY += carreVY 

    pygame.display.update()


#Menu

def menu():
  global screenMode, dockMode

  for i,b in enumerate(boutons[screenMode]):
    b.afficher(screen)

  for i,d in enumerate(docks[dockMode]):
    d.afficher(screen)

  pygame.display.update()

#Posisition du touch

def touch():
  positionPointeur = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

  return positionPointeur[0], positionPointeur[1]

#Touche clikée

def clik():
  for event in EVENTS.get():

    if event.type == GLOBALS.KEYDOWN:
      if event.key == GLOBALS.K_ESCAPE:
        quitter()

      if event.key == GLOBALS.K_RETURN:
        texte("Entree", 0, 0, blancF)
        time.sleep(0.5)

      if event.key == GLOBALS.K_LEFT:
        texte("Gauche", 0, 0, blancF)
        time.sleep(0.5)

      if event.key == GLOBALS.K_RIGHT:
        texte("Droite", 0, 0, blancF)
        time.sleep(0.5)

      if event.key == GLOBALS.K_UP:
        texte("Haut", 0, 0, blancF)
        time.sleep(0.5)

      if event.key == GLOBALS.K_DOWN:
        texte("Bas", 0, 0, blancF)
        time.sleep(0.5)

#Afficher un texte

def texte(text, xpo, ypo, couleur):
  font = pygame.font.Font(None, 24)
  label = font.render(str(text), 1, couleur)
  screen.blit(label, (xpo, ypo))
  pygame.display.flip()

#SplashScreen

splash()

#Main Loop

while 1:

  contact = pygame.mouse.get_pressed()[0]

  menu()

  if contact == True:

    posX, posY = touch()

    for b in boutons[screenMode]:
      b.selection(posX, posY)

    for d in docks[dockMode]:
      d.selection(posX, posY)

  clik()

