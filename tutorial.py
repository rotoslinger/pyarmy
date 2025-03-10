import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('pygame window')

WINDOW_SIZE = (600,400)

display = pygame.Surface((300,200))

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

player_image = pygame.image.load('Green_man.png')

Grass = pygame.image.load('Grass_block.png')
Dirt = pygame.image.load('Dirt.png')
TILE_SIZE = Grass.get_width()

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','2','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]


def collision_test(rect, tiles):
  hit_list = []
  for tile in tiles:
    if rect.colliderect(tile):
      hit_list.append(tile)
  return hit_list

def move(rect, movement, tiles):
  collision_types = {'top':False, 'bottom':False,'right':False,'left':False}
  rect.x = movement[0]
  hit_list = collision_test(rect, tiles)
  for tile in hit_list:
    if movement[0] > 0:
      rect.right = tile.left
      collision_types['right'] = True
    elif movement[0] < 0:
     rect.left = tile.right
    collision_types['left'] = True
  rect.y += movement[1]
  hit_list = collision_test(rect, tiles)
  for tile in hit_list:
    if movement[1] > 0:
      rect.bottom = tile.top
      collision_types['bottom'] = True
    elif movement[1] < 0:
      rect.top = tile.bottom
      collision_types['top'] = True
  return rect, collision_types

moving_right = False
moving_left = False



player_y_momentum = 0

player_rect = pygame.Rect(50,50,player_image.get_width(),player_image.get_height(),)

test_rect = pygame.Rect(100,100,100, 50)


while True:
  display.fill((146,244,255))
  
  tile_rects = []
  y=0
  for row in game_map:
    x = 0
    for tile in row:
      if tile == '1':
        display.blit(Dirt, (x*TILE_SIZE,y*TILE_SIZE))
      if tile == '2':
        display.blit(Grass, (x*TILE_SIZE,y*TILE_SIZE))
      if tile !='0':
        tile_rects.append(pygame.Rect(x*TILE_SIZE,y*TILE_SIZE,TILE_SIZE,TILE_SIZE))
      x += 1
    y += 1

  display.blit(player_image, (player_rect.x, player_rect.y))
  
  
    
  player_movement = [0,0]
  if moving_right:
    player_movement[0] += 2
    if moving_left:
      player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.0
    if player_y_momentum > 3:
      player_y_momentum = 3

  player_rect, collisions = move(player_rect, player_movement, tile_rects)

  display.blit(player_image, (player_rect.x, player_rect.y))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
    if event.type == KEYDOWN:
      if event.key == K_LEFT:
        moving_left = True
      if event.key == K_RIGHT:
        moving_right = True
      
    if event.type == KEYUP:
      if event.key == K_LEFT:
        moving_left = False
      if event.key == K_RIGHT:
        moving_right = False
  surf = pygame.transform.scale(display,WINDOW_SIZE)

  # screen.blit(pygame.transform.scale(display,WINDOW_SIZE))
  screen.blit(surf,(0,0))
        

  pygame.display.update()
  clock.tick(60)  