# for pygame the orgin point (0,0) is in the top left. To increase x (move to the right) we need to add x like normal. However for y in order to move down we need to add y.  
# for importing images add .conert() or .convert_alpha() to allow pygame to work with the image easier. should make the game run faster and easier if their is more stuff on the escreen
import pygame
from sys import exit
#imports pygame... duh
from random import randint
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface_1 = test_font.render(f'Score:{current_time}',False,'black')
    score_rect = score_surface_1.get_rect(center = (400,50))
    screen.blit(score_surface_1,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -=15

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface,obstacle_rect)
            else:
                screen.blit(fly_surface,obstacle_rect)
        
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -10]
        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()
#the equivalant of starting a car. Pygame needs this to start
screen = pygame.display.set_mode((800,400))
#sets the screen size(display surface). width, then height. 
pygame.display.set_caption('Jumpman')
#creates the title for the game
clock = pygame.time.Clock()
test_font = pygame.font.Font('platformer_stuff/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('platformer_stuff/audio/music.wav')
bg_music.set_volume(0.5)
bg_music.play(loops = -1)
# allows the variable to be seen as text.(font type, font size) 
# this variable helps control fps. Does nothing on its own clock.tick is used in loop
sky_surface = pygame.image.load('platformer_stuff/graphics/Sky.png').convert()
# objects on the screen are called surfaces. remember needs a width and height
ground_surface = pygame.image.load('platformer_stuff/graphics/Ground.png').convert()
# score_surface = test_font.render('Score', False,'black')
# # (what text you are putting, anti alias (smooth the edges of text), color)
# score_rect = score_surface.get_rect(topleft =(0,0))
snail_frame_1 = pygame.image.load('platformer_stuff/sprites/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('platformer_stuff/sprites/snail2.png').convert_alpha()
# snail_rect = snail_surface.get_rect(bottomright = (600,300))
# sets the snail to x 600
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]



fly_frame_1 = pygame.image.load('platformer_stuff/sprites/fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('platformer_stuff/sprites/fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]



obstacle_rect_list = []


player_walk_1 = pygame.image.load('platformer_stuff/sprites/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('platformer_stuff/sprites/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump =  pygame.image.load('platformer_stuff/sprites/jump.png').convert_alpha()

player_surface = player_walk[player_index]




player_rect = player_surface.get_rect(midbottom = (80,300))
# creates a rectangle that we put a surface into so we can move it easier.(the cords should be the same position as where you want the surface)
player_gravity = 0
player_stand = pygame.image.load('platformer_stuff/sprites/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))


jump_sound = pygame.mixer.Sound('platformer_stuff/audio/audio_jump.mp3')
jump_sound.set_volume(0.5)





game_name = test_font.render('Jumpman', False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))
game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400, 320))


obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)




while True:
    # this keeps the screen up forever. All elements and updates must happen in this loop.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # when the x button is pressed close the game, cause an error because it doesnt close the while loop
            exit()
            #this exit() stops the while loop and prevents an error
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >=300:
                    player_gravity = -20
                    jump_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                # snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == obstacle_timer and game_active:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
                else:obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900,1100),210)))
            
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index =1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]
            
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index =1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

    
    
    
    if game_active:  
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect)
        # # draws a shape. ((what surface are you drawing on), (color), (what are we drawing)
        # screen.blit(score_surface,(score_rect))
        score = display_score()

        # snail_rect.x -=4
        # # the snail moves -4 pixels aka to the left. 
        # if snail_rect.right <= 0: snail_rect.left = 800
        # # if the right side of the rectangle aka the snail is off the screen then reset the left side of the rectangle to 800 aka the right side of the screen
        # screen.blit(snail_surface,(snail_rect))
        # # bilt mean block image transfer. Allows me to put a surface on a surface (object i want, cords for where i want it)
       
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface, player_rect)

        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        game_active = collisions(player_rect,obstacle_rect_list)

        # if snail_rect.colliderect(player_rect):
        #     game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)

        score_message = test_font.render(f'Your Score: {score}',False,'black')
        score_message_rect = score_message.get_rect(center = (650,50))
        screen.blit(game_name, game_name_rect)
        screen.blit(score_message,score_message_rect)
        screen.blit(game_message, game_message_rect)
        
        
    


    # if player_rect.colliderect(snail_rect):
     # no collision = 0. Collison = 1 if player_rect.colliderect(snail_rect) = 1 is unecessary since pythin automatically converst 0 to False
    pygame.display.update()
    #updating the display on line 6. All changes in this loop are updated on the display surface
    clock.tick(60)
    # tells the game'line 16' to not exceed 60 times a second (maximum frame rate) minimum fram rate you cant really control. depends on computer/ how much is on screen.
