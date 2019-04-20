# Import libraries
import pygame
from math import pi
import keyboard
import time
 
# Initialize the game engine and font
pygame.init()
pygame.font.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)

#select difficulty of the game
difficulty = 5

# Set the height and width of the screen
size = width, height =  [1000, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong!")

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

#menu screen
menu = False
difficulty_menu = True
multi_menu = True
menu1 = 0
menu2 = 0

while menu == False:
    clock.tick(20)
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 72)
    text_game_mode = font.render("Select Game Mode", True, WHITE)
    text_single_player = font.render("Single Player", True, WHITE)
    text_multi_player = font.render("Multi-Player", True, WHITE)
    screen.blit(text_game_mode,(width/4,100))
    screen.blit(text_single_player,(width/4,200))
    screen.blit(text_multi_player,(width/4,250))
    
    if menu1 == 0:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),225], 5)
    if menu1 == 1:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),275], 5)

    if keyboard.is_pressed('w') or keyboard.is_pressed('UP'):
        menu1 = 0
    if keyboard.is_pressed('s') or keyboard.is_pressed('DOWN'):
        menu1 = 1

    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            menu = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and menu1 == 0:
            difficulty_menu = False
            menu = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and menu1 == 1:
            multi_menu = False
            menu = True

while difficulty_menu == False:
    clock.tick(20)
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 72)
    text_difficulty = font.render("Select difficulty", True, WHITE)
    text_normal = font.render("Normal", True, WHITE)
    text_hard = font.render("Hard", True, WHITE)
    screen.blit(text_difficulty,(width/4,100))
    screen.blit(text_normal,(width/4,200))
    screen.blit(text_hard,(width/4,250))
    if menu2 == 0:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),225], 5)
    if menu2 == 1:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),275], 5)

    pygame.display.flip()

    if keyboard.is_pressed('w') or keyboard.is_pressed('UP'):
        menu2 = 0
    if keyboard.is_pressed('s') or keyboard.is_pressed('DOWN'):
        menu2 = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            menu = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and menu2 == 0:
            difficulty = 5
            difficulty_menu = True
            multi_menu = True
            menu = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and menu2 == 1:
            difficulty = 9
            difficulty_menu = True
            multi_menu = True
            menu = True

while multi_menu == False:
    clock.tick(20)
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 72)
    text_multi = font.render("Select multi options", True, WHITE)
    text_host = font.render("Host", True, WHITE)
    text_join = font.render("Join", True, WHITE)
    screen.blit(text_multi,(width/4,100))
    screen.blit(text_host,(width/4,200))
    screen.blit(text_join,(width/4,250))
    if menu2 == 0:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),225], 5)
    if menu2 == 1:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),275], 5)

    pygame.display.flip()

    if keyboard.is_pressed('w') or keyboard.is_pressed('UP'):
        menu2 = 0
    if keyboard.is_pressed('s') or keyboard.is_pressed('DOWN'):
        menu2 = 1


#this stuff needs to be organized
ball_pos_x = width/2
ball_pos_y = height/2
ball_vel_x = -difficulty
ball_vel_y = -difficulty
AI_pos_y = height/2
AI_speed = difficulty + 1
player1_score = 0
player2_score = 0
keys = pygame.key.get_pressed()
player_pos_y = height/2
last_mouse_y = height/2
i = 0
wait = False

while not done:
 
    #limits while loop to max of ___ times per second.
    clock.tick(100)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(BLACK)
	
    #controls
    pygame.mouse.set_visible(False)
	
    #mouse controls
    current_mouse_y = pygame.mouse.get_pos()
    if current_mouse_y != last_mouse_y:
        mouse_pos = player_pos_x, player_pos_y = pygame.mouse.get_pos()
    last_mouse_y = current_mouse_y

    #keyboard controls
    if keyboard.is_pressed('w'):
        player_pos_y -= 10
    if keyboard.is_pressed('s'):
        player_pos_y += 10
    
    # Draw a rectangle outline
    pygame.draw.rect(screen, WHITE, [10, player_pos_y-50, 10, 100], 0)
    pygame.draw.rect(screen, WHITE, [980, AI_pos_y, 10, 100], 0)
    pygame.draw.circle(screen, WHITE, [int(ball_pos_x), int(ball_pos_y)], 5)

    #move the ball everyframe by its velocity
    ball_pos_x += ball_vel_x
    ball_pos_y += ball_vel_y

    #bounce ball off left paddle
    if ball_pos_x < 20 and ball_pos_x > 10 and ball_pos_y > player_pos_y-50 and ball_pos_y < player_pos_y+50:
        ball_vel_x = -ball_vel_x

    #bounce ball off right paddle
    if ball_pos_x > width-20 and ball_pos_x < width-10 and ball_pos_y > AI_pos_y and ball_pos_y < AI_pos_y+100:
        ball_vel_x = -ball_vel_x

    #player 1 scores
    if ball_pos_x > 1200:
        ball_pos_x = 500
        ball_pos_y = 250
        player1_score += 1

    #player 2 scores
    if ball_pos_x < -200:
        ball_pos_x = 500
        ball_pos_y = 250
        player2_score += 1

        
    #bounce ball up and down
    if ball_pos_y > height:
        ball_vel_y = -ball_vel_y
    if ball_pos_y < 0:
        ball_vel_y = -ball_vel_y

    #enemy AI
    if ball_pos_y > AI_pos_y+50:
        AI_pos_y += AI_speed
    if ball_pos_y < AI_pos_y:
        AI_pos_y -= AI_speed


    #score
    font = pygame.font.SysFont(None, 72)
    text1 = font.render(str(player1_score), True, WHITE)
    screen.blit(text1,(400,0))

    text2 = font.render(str(player2_score), True, WHITE)
    screen.blit(text2,(600,0))

    if player1_score > 9:
        text3 = font.render("Player 1 Wins!", True, WHITE)
        screen.blit(text3,(width/2-150,height/2))
        ball_vel_x = 0
    if player2_score > 9:
        text3 = font.render("Player 2 Wins!", True, WHITE)
        screen.blit(text3,(width/2-150,height/2))
        ball_vel_x = 0
    
    #update screen command
    pygame.display.flip()

    #press a button to start the game
    if i == 0:
        font = pygame.font.SysFont(None, 72)
        text1 = font.render("Press space when ready...", True, WHITE)
        screen.blit(text1,(width/4,height/4))
        pygame.display.flip()
        while wait == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    wait = True
                
    i += 1
# Be IDLE friendly
pygame.quit()
