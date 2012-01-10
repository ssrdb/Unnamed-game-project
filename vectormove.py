background_image_filename = 'bg.jpg'
star_image_filename = 'star3.png'

import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2

pygame.init()
font = pygame.font.SysFont("arial",32);
font_height = font.get_linesize()

screensize = (1024,720)
screen = pygame.display.set_mode(screensize,0,32)

background = pygame.image.load(background_image_filename).convert()
star = pygame.image.load(star_image_filename)

clock = pygame.time.Clock()
position = Vector2(100.0, 100.0)
speed = 250.
heading = Vector2()

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
    if event.type == MOUSEBUTTONDOWN:
      destination = Vector2(*event.pos) - Vector2(*star.get_size())/2
      heading = Vector2.from_points(position, destination)
      heading.normalize()

  screen.blit(background, (0,0))
  screen.blit(star,position)
  time_passed = clock.tick(70)
  time_passed_seconds = time_passed/1000.0
  
  if position.get_x() > screensize[0]:
    heading.set_x(-heading.get_x())
  if position.get_x() < 0:
    heading.set_x(-heading.get_x())
  if position.get_y() > screensize[1]:
    heading.set_y(-heading.get_y())
  if position.get_y() < 0:
    heading.set_y(-heading.get_y())
    
  distance = time_passed_seconds*speed
  position += heading * distance
  
  
  
  text_surface = font.render("Stadsetning: "+str(position), True, (0,0,0))
  screen.blit(text_surface, (8, font_height))
  pygame.display.update() #display everything
