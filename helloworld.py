background_image_filename = 'cs_seated02.jpg'
mouse_image_filename = 'arrowupvoted.png'

import pygame #gives access to submodules 

from pygame.locals import * #important functions and constant
from sys import exit #finish script immediately when user clicks close button

pygame.init() #initializes pygame!

screen = pygame.display.set_mode((640, 480),0, 32) #display surface ((width,height),0|FULLSCREEN|RESIZABLE|OPENGL,depth)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()

  screen.blit(background, (0,0))

  x, y = pygame.mouse.get_pos()
  x-= mouse_cursor.get_width() / 2
  y-= mouse_cursor.get_height() / 2
  screen.blit(mouse_cursor, (x, y))
  
  pygame.display.update()