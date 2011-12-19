background_image_filename = 'cs_seated02.jpg'
mouse_image_filename = 'arrowupvoted.png'

import pygame #gives access to submodules 

from pygame.locals import * #important functions and constant
from sys import exit #finish script immediately when user clicks close button

pygame.init() #initializes pygame!

screen = pygame.display.set_mode((640, 480),0, 32) #display surface ((width,height),0|FULLSCREEN|RESIZABLE|OPENGL,depth)
pygame.display.set_caption("Hello, World!") #set title bar

background = pygame.image.load(background_image_filename).convert() #loads a file and returns a surface, convert image to same format as display
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha() #convert_alpha else we would have a square for cursor

while True:
  """Main game loop, the event loop, most games have them!"""
  for event in pygame.event.get(): #Loop through all events, while true!
    if event.type == QUIT:
      exit()

  screen.blit(background, (0,0)) #blitting means copying from one image(background) to another(screen)
                                 #(0,0) is the absolute position of the background, it never moves
                                 #We are always blitting to the same coordinate, (0,0) at the top left of the screen 

  #Draw the mouse cursor underneath the usual mouse pointer
  x, y = pygame.mouse.get_pos()
  x-= mouse_cursor.get_width() / 2
  y-= mouse_cursor.get_height() / 2
  screen.blit(mouse_cursor, (x, y)) #blit the mouse image 
  
  pygame.display.update() #display everything!
