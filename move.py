background_image_filename = 'cs_seated02.jpg'
sprite_image_filename = 'arrowupvoted.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480),0,32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)

x=0.

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
  screen.blit(background, (0,0))
  screen.blit(sprite,(x,100))
  x+=10.

  if x> 640.:
    x-=640.
  pygame.display.update() #display everything!
