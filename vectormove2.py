#
background_image_filename = 'bg.jpg'
star_image_filename = 'star3.png'
sprite_image_filename = 'arrowupvoted.png'
#
import pygame
from pygame.locals import *
from sys import exit
from gameobjects.vector2 import Vector2
from math import *
#
pygame.init()
#
font = pygame.font.SysFont("arial",32);
font_height = font.get_linesize()
screensize = (1024,720)
screen = pygame.display.set_mode(screensize,0,32)
background = pygame.image.load(background_image_filename).convert()
star = pygame.image.load(star_image_filename)
sprite = pygame.image.load(sprite_image_filename)
clock = pygame.time.Clock()
#
sprite_pos = Vector2(200, 150)
sprite_speed = 300.
sprite_rotation = 0.
sprite_rotation_speed = 360.
star_position = Vector2(100.0, 100.0)
star_speed = 250.
star_heading = Vector2()
#

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
    if event.type == MOUSEBUTTONDOWN:
      star_destination = Vector2(*event.pos) - Vector2(*star.get_size())/2
      star_heading = Vector2.from_points(star_position, star_destination)
      star_heading.normalize()
  pressed_keys = pygame.key.get_pressed()
  rotation_direction = 0.
  movement_direction = 0.
  
  if pressed_keys[K_LEFT]:
    rotation_direction=+1.
  elif pressed_keys[K_RIGHT]:
    rotation_direction=-1.
  if pressed_keys[K_UP]:
    movement_direction=-1.
  elif pressed_keys[K_DOWN]:
    movement_direction = +1.
    
  screen.blit(background, (0,0))
  screen.blit(star,star_position)
  
  rotated_sprite = pygame.transform.rotate(sprite, sprite_rotation)
  w, h = rotated_sprite.get_size()
  sprite_draw_pos = Vector2(sprite_pos.x-w/2,sprite_pos.y-h/2)
  screen.blit(rotated_sprite, sprite_draw_pos)
  
  time_passed = clock.tick(70)
  time_passed_seconds = time_passed/1000.0
  
  sprite_rotation+= rotation_direction*sprite_rotation_speed*time_passed_seconds
  
  sprite_headX = sin(sprite_rotation*pi/180.)
  sprite_headY = cos(sprite_rotation*pi/180.)
  sprite_heading = Vector2(sprite_headX, sprite_headY)
  sprite_heading *= movement_direction
  
  if star_position.get_x() > screensize[0]:
    star_heading.set_x(-star_heading.get_x())
  if star_position.get_x() < 0:
    star_heading.set_x(-star_heading.get_x())
  if star_position.get_y() > screensize[1]:
    star_heading.set_y(-star_heading.get_y())
  if star_position.get_y() < 0:
    star_heading.set_y(-star_heading.get_y())
    
  sprite_pos+= sprite_heading * sprite_speed * time_passed_seconds
  star_distance = time_passed_seconds*star_speed
  star_position += star_heading * star_distance
  
  text_surface = font.render("Stadsetning: "+str(star_position), True, (0,0,0))
  screen.blit(text_surface, (8, font_height))
  pygame.display.update() #display everything
