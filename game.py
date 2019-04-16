# Import a library of functions called 'pygame'
import pygame
from math import pi
 
# Initialize the game engine
pygame.init()
pygame.font.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
# Set the height and width of the screen
size = width, height =  [1000, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example code for the draw module")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
ball_x_pos = 500
ball_y_pos = 250
velx = -5
vely = -5
AI_y = 50
AI_speed = 2
player1_score = 0
player2_score = 0
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(100)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(BLACK)

    pygame.mouse.set_visible(False)
    mouse_pos = x, y = pygame.mouse.get_pos()
    
    # Draw a rectangle outline
    pygame.draw.rect(screen, WHITE, [10, y-50, 10, 100], 0)
    pygame.draw.rect(screen, WHITE, [980, AI_y, 10, 100], 0)
    pygame.draw.circle(screen, WHITE, [ball_x_pos, ball_y_pos], 5)

    ball_x_pos = ball_x_pos + velx
    ball_y_pos = ball_y_pos + vely

    #bounce ball off left paddle
    if ball_x_pos < 20 and ball_x_pos > 10 and ball_y_pos > y-50 and ball_y_pos < y+50:
        velx = -velx

    #bounce ball off right paddle
    if ball_x_pos > width-20 and ball_x_pos < width-10 and ball_y_pos > AI_y and ball_y_pos < AI_y+100:
        velx = -velx
        
    if ball_x_pos > 1200:
        #reposition ball
        ball_x_pos = 500
        ball_y_pos = 250
        player1_score = player1_score + 1
        print("player 1 scored")

    if ball_x_pos < -200:
        #reposition ball
        ball_x_pos = 500
        ball_y_pos = 250
        player2_score = player2_score + 1
        print("player 2 scored")

        
    #bounce ball up and down
    if ball_y_pos > height:
        vely = -vely
    if ball_y_pos < 0:
        vely = -vely

    #enemy AI
    if ball_y_pos > AI_y+50:
        AI_y = AI_y + AI_speed
    if ball_y_pos < AI_y:
        AI_y = AI_y - AI_speed


    #score
    font = pygame.font.SysFont(None, 72)
    text1 = font.render(str(player1_score), True, WHITE)
    screen.blit(text1,(400,0))

    text2 = font.render(str(player2_score), True, WHITE)
    screen.blit(text2,(600,0))

    if player1_score > 9:
        text3 = font.render("Player 1 Wins!", True, WHITE)
        screen.blit(text3,(width/2-150,height/2))
        velx = 0
    if player2_score > 9:
        text3 = font.render("Player 2 Wins!", True, WHITE)
        screen.blit(text3,(width/2-150,height/2))
        velx = 0
    
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
