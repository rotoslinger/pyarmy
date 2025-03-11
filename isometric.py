import pygame, sys, os

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption('pyarmy')

WINDOW_SIZE = (600,400)

player_image = pygame.image.load('Green_man.png')
guy_image = pygame.image.load('Green_man.png')
block = pygame.image.load('Big_block.png')
shadow_image = pygame.image.load('shadow.png')
width = block.get_width()-1
height = block.get_height()

display = pygame.Surface((300,200))

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)

# Tiled program!!!!
# tutorial https://www.youtube.com/watch?v=N6xqCwblyiw&t=52s
# software download!
# https://thorbjorn.itch.io/tiled

game_map = [['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','2','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]


z = 0
jump_force = 0
gravity =0

hopping = False

hopping_up_right = False
hopping_up_left = False
hopping_down_right = False
hopping_down_left = False
hopping_up = False
hopping_down = False
hopping_right = False
hopping_left = False

current_hop = 0
hop_size = 27

moving_left = False
moving_right = False
moving_up = False
moving_down = False

# little_guys = [[player_rect,x,y,z,hp,weapon,status(whether their following or not),direction,hopping status]]
little_guys = [[pygame.Rect(100,100,player_image.get_width(),player_image.get_height()-12,),100,100,0,10,1,0,1,0],
               [pygame.Rect(10,100,player_image.get_width(),player_image.get_height()-12,),10,100,0,10,1,0,1,0],
               [pygame.Rect(30,6,player_image.get_width(),player_image.get_height()-12,),30,6,0,1,0,1,0],
               [pygame.Rect(10,10,player_image.get_width(),player_image.get_height()-12,),10,10,0,10,1,0,1,0],
               [pygame.Rect(50,40,player_image.get_width(),player_image.get_height()-12,),50,40,0,1,0,1,0]]
army_size = 0
temp_army_size = 0

shadow_pos= [150,100]

cam_pos_y = 0
cam_pos_x = 0

cam_pos_y_tile = 0
cam_pos_x_tile = 0
player_rect = pygame.Rect(150,100,player_image.get_width(),
                          player_image.get_height()-12,)

def guy_create(guy):
  guy[0].x = guy[1]+cam_pos_x
  guy[0].y = guy[2]+cam_pos_y
  display.blit(shadow_image,(guy[0].x,guy[0].y))
  display.blit(guy_image,(guy[0].x,guy[0].y+guy[3]- 11))
  

def collide(object_rect):
  return

movement = [0,0]

def move(pos,move_amount):
  pos[0] += move_amount[0]
  pos[1] += move_amount[1]
  move_amount[1] = 0
  move_amount[0] = 0



def camera_set(focal_point):
    global cam_pos_x
    global cam_pos_y
    global cam_pos_x_tile
    global cam_pos_y_tile

    cam_pos_x = -focal_point[0] + 100
    cam_pos_y = -focal_point[1] + 100
    
    ################################################################
    # Inverse matrix calculation for world to tile conversion
    
    # Theory:
    
    # If you have Matrix A:
    #      _     _
    # A  =| a,  b |
    #     | c,  d |
    #      ‾     ‾
    # Invert the diagonals and negate from bottom left to upper right:
    #      _     _
    # A⁻¹=| d, -b |
    #     | -c, a |
    #      ‾     ‾
    # Calculate the determinant:
    # a * d - b * c
    #
    # newly inverted a,b,c,d:
    # inv_a = d
    # inv_b = -b
    # inv_c = -c
    # inv_d = a
    
    # Practice: 
    # in your tilemap, you are creating your tile dimensions this way:
    
    # tile_width  = (x * 0.5 * width) + (y * -0.5 * width)
    # tile_height = (x * 0.25 * height) + (y * 0.25 * height)
    
    # lets break this down into the
    
    # getting the parts of the determinant while factoring in the tile-map scaling
    # a ---  0.5  * width 
    # b ---  0.25 * height
    # c --- -0.5  * width
    # d ---  0.25 * height
    
    # final parts of the determinant
    # determinant = a * d - b * c
    
    # get the reciprocal of the determinant
    # inverse determinant = 1 / det
    
    ################################################################
    
    # Calculate the determinant 
    # inv_det is the reciprocal of this determinant, used to scale the transformation matrix
    inv_det = 1 / ((0.5 * width * 0.25 * height) - (-0.5 * width * 0.25 * height))

    # Compute the inverse elements
    # These values are derived from the inverse of the affine transformation matrix

    # IMPORTANT This is the core of this whole step!
    # You are transforming your ORTHOGRAPHIC view back to ISOMETRIC!
    # you are essentially rotating your camera move counter clock-wise 🕘 while still doing the original movement
    inv_a = 0.25 * height * inv_det
    inv_b = 0.5 * width * inv_det
    inv_c = -0.25 * height * inv_det
    inv_d = -0.5 * width * inv_det

    # Convert screen-space movement to tile-space
    cam_pos_x_tile = int((inv_a * shadow_pos[0] + inv_b * shadow_pos[1]) / 16)
    cam_pos_y_tile = int((inv_c * shadow_pos[0] + inv_d * shadow_pos[1]) / 16)
    
    # YEEEEEAAAAAAH 🤘😆🤘 (ʘ‿ʘ)


print("outside")


while True:

  display.fill((50,130,255))

  temp_army_size = 0
  for guy in little_guys:
    temp_army_size+= 1

  move(shadow_pos,movement)
  # sets the player position (basicaly the players position is an offset from the shadow)
  player_rect.x = shadow_pos[0] + cam_pos_x
  player_rect.y = shadow_pos[1]-z - 11+ cam_pos_y
  
  camera_set(shadow_pos)


  y = cam_pos_y_tile / 16

  for row in game_map:
      x = cam_pos_x_tile / 16
      for tile in row:
          if tile != '0':
              # move the tilemap in the opposite direction of the players movement
              t_width = int((x * 0.5 * width) + (y * -0.5 * width)) + cam_pos_x
              t_height = int((x * 0.25 * height) + (y * 0.25 * height)) + cam_pos_y
              
              display.blit(block, (t_width, t_height))
          x += 1
      y += 1
    

  # gets the player inputs

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    
    if event.type == KEYDOWN:
      if event.key == K_LEFT:
        moving_left = True
        # shadow_pos[0] -= 3

      if event.key == K_RIGHT:
        moving_right = True
        # shadow_pos[0] += 3

      if event.key == K_UP:
        moving_up = True

      if event.key == K_DOWN:
        moving_down = True

    if event.type == KEYUP:
      if event.key == K_LEFT:
        moving_left = False

      if event.key == K_RIGHT:
        moving_right = False

      if event.key == K_UP:
        moving_up = False

      if event.key == K_DOWN:
        moving_down = False

  def move_right():
    return
    
  #exampl scipt my dad made that I want to repurpose for little guy movement 
  '''
  if moving_right:
    shadow_pos[0] += .3
    current_hop += 1 
    jump_force = 1

  if moving_left:
    shadow_pos[0] -= .3
    current_hop += 1 
    jump_force = 1

  if moving_up:
    shadow_pos[1] -= .3
    current_hop += 1 
    jump_force = 1

  if moving_down:
    shadow_pos[1] += .3
    current_hop += 1 
    jump_force = 1
  if not any([moving_left, moving_right, moving_down, moving_up]):
     current_hop = 0
     jump_force = 0
     hopping = False
  '''

  if any([moving_down,moving_up]) and any([moving_left,moving_right]) and not any([hopping_up,hopping_right,hopping_left,hopping_down]) or any([hopping_up_left,hopping_up_right,hopping_down_left,hopping_down_right]) and not any([hopping_up,hopping_right,hopping_left,hopping_down]):
    if not hopping and moving_left and moving_up:
      current_hop = 0
      hopping = True
      hopping_up_left = True
      jump_force = 1.4
    elif current_hop > hop_size and hopping_up_left:
      hopping = False
      hopping_up_left = False
      current_hop = 0
      jump_force = 0
    elif hopping_up_left:
      current_hop += 1 
      cam_pos_x_tile += 1
      cam_pos_x += 0.95
      cam_pos_y += 0.5

    if not hopping and moving_left and moving_down:
      current_hop = 0
      hopping = True
      hopping_down_left = True
      jump_force = 1.4
    elif current_hop > hop_size and hopping_down_left:
      hopping = False
      hopping_down_left = False
      current_hop = 0
      jump_force = 0
    elif hopping_down_left:
      current_hop += 1 
      cam_pos_y_tile -= 1
      cam_pos_x += 0.95
      cam_pos_y -= 0.5

    if not hopping and moving_right and moving_up:
      current_hop = 0
      hopping = True
      hopping_up_right = True
      jump_force = 1.4
    elif current_hop > hop_size and hopping_up_right:
      hopping = False
      hopping_up_right = False
      current_hop = 0
      jump_force = 0
    elif hopping_up_right:
      current_hop += 1 
      cam_pos_y_tile += 1
      cam_pos_x -= 0.95
      cam_pos_y += 0.5
  
    if not hopping and moving_right and moving_down:
      current_hop = 0
      hopping = True
      hopping_down_right = True
      jump_force = 1.4
    elif current_hop > hop_size and hopping_down_right:
      hopping = False
      hopping_down_right = False
      current_hop = 0
      jump_force = 0
    elif hopping_down_right:
      current_hop += 1 
      cam_pos_x_tile -= 1
      cam_pos_x -= 0.95
      cam_pos_y -= 0.5
  else:
    #player movement/hopping
    if not hopping and moving_right:
      current_hop = 0
      hopping = True
      hopping_right = True
      jump_force = 1.4
    elif current_hop > hop_size and hopping_right:
      hopping = False
      hopping_right = False
      current_hop = 0
      jump_force = 0
    elif hopping_right:
      current_hop += 1 
      movement[0] += 1

    if not hopping and moving_left:
      current_hop = 0
      hopping = True
      hopping_left = True
      jump_force = 1.4
    elif current_hop > hop_size and hopping_left:
      hopping = False
      hopping_left = False
      current_hop = 0
      jump_force = 0
    elif hopping_left:
      current_hop += 1 
      movement[0] -= 1

    if not hopping and moving_down:
      current_hop = 0
      hopping = True
      hopping_down = True
      jump_force = 1.4
    elif current_hop > hop_size and hopping_down:
      hopping = False
      hopping_down = False
      current_hop = 0
      jump_force = 0
    elif hopping_down:
      current_hop += 1 
      cam_pos_x_tile -= 1
      cam_pos_y_tile -= 1
      cam_pos_y -= 1


    if not hopping and moving_up:
      current_hop = 0
      hopping = True
      hopping_up = True
      jump_force = 1.4
    elif current_hop > hop_size and hopping_up:
      hopping = False
      hopping_up = False
      current_hop = 0
      jump_force = 0
    elif hopping_up:
      current_hop += 1 
      cam_pos_x_tile += 1
      cam_pos_y_tile += 1
      cam_pos_y += 1



#renders the second layer of the map
  y = cam_pos_y_tile/16 -1

  for row in game_map:
    x = cam_pos_x_tile/16 -1
    for tile in row:
      if int(tile) > 1 and y*height+55 < player_rect.y:
        display.blit (block, (x*0.5*width+y*-0.5*width   ,  x*0.25*height+y*0.25*height))
      x += 1
    y += 1

#renders the 3rd layer of the tilemap
  y = cam_pos_y_tile/16 - 2

  for row in game_map:
    x = cam_pos_x_tile/16 - 2
    for tile in row:
      if int(tile) > 2:
        display.blit (block, (x*0.5*width+y*-0.5*width   ,  x*0.25*height+y*0.25*height))
      x += 1
    y += 1

#renders the 4th layer of the tilemap
  y = cam_pos_y_tile/16 - 3

  for row in game_map:
    x = cam_pos_x_tile/16 - 3
    for tile in row:
      if int(tile) > 3:
        display.blit (block, (x*0.5*width+y*-0.5*width   ,  x*0.25*height+y*0.25*height))
      x += 1
    y += 1

  player_rect.x = shadow_pos[0] + cam_pos_x
  player_rect.y = (shadow_pos[1]-z-11)+ cam_pos_y

  # displays the player and their shadow
  display.blit(shadow_image, (shadow_pos[0]+cam_pos_x, shadow_pos[1]+cam_pos_y))
  display.blit(player_image, (player_rect.x, player_rect.y))


  for guy in little_guys:
    guy_create(guy)



#renders the second layer of the map
  y = cam_pos_y_tile/16 -1

  for row in game_map:
    x = cam_pos_x_tile/16 -1
    for tile in row:
      if int(tile) > 1 and y*height+55 >= player_rect.y:
        display.blit (block, (x*0.5*width+y*-0.5*width   ,  x*0.25*height+y*0.25*height))
      x += 1
    y += 1

#renders the 3rd layer of the tilemap
  y = cam_pos_y_tile/16 - 2

  for row in game_map:
    x = cam_pos_x_tile/16 - 2
    for tile in row:
      if int(tile) > 2:
        display.blit (block, (x*0.5*width+y*-0.5*width   ,  x*0.25*height+y*0.25*height))
      x += 1
    y += 1

#renders the 4th layer of the tilemap
  y = cam_pos_y_tile/16 - 3

  for row in game_map:
    x = cam_pos_x_tile/16 - 3
    for tile in row:
      if int(tile) > 3:
        display.blit (block, (x*0.5*width+y*-0.5*width   ,  x*0.25*height+y*0.25*height))
      x += 1
    y += 1

  z += jump_force

  if z < 0 or z == 0:
    z=0
    gravity = 0
  else:
    gravity += 0.1
    z -= gravity

  camera_set([0,56685])

  surf = pygame.transform.scale(display,WINDOW_SIZE)
  screen.blit(surf,(0,0))
  pygame.display.update()
  clock.tick(60)
