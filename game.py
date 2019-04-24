# Import libraries
import pygame
from math import pi
import keyboard
import time

# neither mode will run unless called in menu
done = True
multi_local_done = True
multi_mode_chosen = 0
difficulty = 5

# this input needs to be sanitized

# game mode
print("Select Game Mode")
print("1) Single Player")
print("2) Multiplayer")
game_mode_chosen = int(input())

# single player - difficulty
if game_mode_chosen == 1:
    print("")
    difficulty = int(input("Enter a difficulty 1-9: "))
    done = False

# multiplayer - mode
if game_mode_chosen == 2:
    print("")
    print("Multiplayer")
    print("")
    print("1) Splitscreen")
    print("2) Host")
    print("3) Join")
    multi_mode_chosen = int(input())

# splitscreen - difficulty
if multi_mode_chosen == 1:
    print("")
    print("Splitscreen")
    difficulty = int(input("Enter ball speed 1-9: "))
    multi_local_done = False

# host
if multi_mode_chosen == 2:
    print("")
    print("Host")
    print("waiting for connection...")

# join
if multi_mode_chosen == 3:
    print("")
    print("Join")
    print("")
    host_ip = input("Enter host IP address: ")
    print("connecting...")

# Initialize the game engine and font
pygame.init()
pygame.font.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the height and width of the screen
size = width, height = [1000, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong!")

# Loop until the user clicks the close button.
clock = pygame.time.Clock()

# this stuff needs to be organized
ball_pos_x = width / 2
ball_pos_y = height / 2
ball_vel_x = -difficulty
ball_vel_y = -difficulty
player2_pos_y = height / 2
AI_speed = difficulty + 1
player1_score = 0
player2_score = 0
keys = pygame.key.get_pressed()
player1_pos_y = height / 2
last_mouse_y = height / 2
i = 0
wait = False

while not done:

    # limits while loop to max of ___ times per second.
    clock.tick(100)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(BLACK)

    # controls
    pygame.mouse.set_visible(False)

    # mouse controls
    current_mouse_y = pygame.mouse.get_pos()
    if current_mouse_y != last_mouse_y:
        mouse_pos = player_pos_x, player1_pos_y = pygame.mouse.get_pos()
    last_mouse_y = current_mouse_y

    # keyboard controls
    if keyboard.is_pressed('w'):
        player1_pos_y -= 10
    if keyboard.is_pressed('s'):
        player1_pos_y += 10

    # Draw a rectangle outline
    pygame.draw.rect(screen, WHITE, [10, player1_pos_y - 50, 10, 100], 0)
    pygame.draw.rect(screen, WHITE, [980, player2_pos_y, 10, 100], 0)
    pygame.draw.circle(screen, WHITE, [int(ball_pos_x), int(ball_pos_y)], 5)

    # move the ball everyframe by its velocity
    ball_pos_x += ball_vel_x
    ball_pos_y += ball_vel_y

    # bounce ball off left paddle
    if ball_pos_x < 20 and ball_pos_x > 10 and ball_pos_y > player1_pos_y - 50 and ball_pos_y < player1_pos_y + 50:
        ball_vel_x = -ball_vel_x

    # bounce ball off right paddle
    if ball_pos_x > width - 20 and ball_pos_x < width - 10 and ball_pos_y > player2_pos_y and ball_pos_y < player2_pos_y + 100:
        ball_vel_x = -ball_vel_x

    # player 1 scores
    if ball_pos_x > 1200:
        ball_pos_x = 500
        ball_pos_y = 250
        player1_score += 1

    # player 2 scores
    if ball_pos_x < -200:
        ball_pos_x = 500
        ball_pos_y = 250
        player2_score += 1

    # bounce ball up and down
    if ball_pos_y > height:
        ball_vel_y = -ball_vel_y
    if ball_pos_y < 0:
        ball_vel_y = -ball_vel_y

    # enemy AI
    if ball_pos_y > player2_pos_y + 50:
        player2_pos_y += AI_speed
    if ball_pos_y < player2_pos_y:
        player2_pos_y -= AI_speed

    # score
    font = pygame.font.SysFont(None, 72)
    text1 = font.render(str(player1_score), True, WHITE)
    screen.blit(text1, (400, 0))

    text2 = font.render(str(player2_score), True, WHITE)
    screen.blit(text2, (600, 0))

    if player1_score > 9:
        text3 = font.render("Player 1 Wins!", True, WHITE)
        screen.blit(text3, (width / 2 - 150, height / 2))
        ball_vel_x = 0
    if player2_score > 9:
        text3 = font.render("Player 2 Wins!", True, WHITE)
        screen.blit(text3, (width / 2 - 150, height / 2))
        ball_vel_x = 0

    # update screen command
    pygame.display.flip()

    # press a button to start the game
    if i == 0:
        font = pygame.font.SysFont(None, 72)
        text1 = font.render("Press space when ready...", True, WHITE)
        screen.blit(text1, (width / 4, height / 4))
        pygame.display.flip()
        while wait == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    wait = True

    i += 1

# Be IDLE friendly


while not multi_local_done:

    # limits while loop to max of ___ times per second.
    clock.tick(100)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.

    # Clear the screen and set the screen background
    screen.fill(BLACK)

    # controls
    pygame.mouse.set_visible(False)

    # mouse controls
    current_mouse_y = pygame.mouse.get_pos()
    if current_mouse_y != last_mouse_y:
        mouse_pos = player_pos_x, player1_pos_y = pygame.mouse.get_pos()
    last_mouse_y = current_mouse_y

    # keyboard controls
    if keyboard.is_pressed('w'):
        player1_pos_y -= 10
    if keyboard.is_pressed('s'):
        player1_pos_y += 10
    if keyboard.is_pressed('UP'):
        player2_pos_y -= 10
    if keyboard.is_pressed('DOWN'):
        player2_pos_y += 10

    # Draw a rectangle outline
    pygame.draw.rect(screen, WHITE, [10, player1_pos_y - 50, 10, 100], 0)
    pygame.draw.rect(screen, WHITE, [980, player2_pos_y, 10, 100], 0)
    pygame.draw.circle(screen, WHITE, [int(ball_pos_x), int(ball_pos_y)], 5)

    # move the ball everyframe by its velocity
    ball_pos_x += ball_vel_x
    ball_pos_y += ball_vel_y

    # bounce ball off left paddle
    if ball_pos_x < 20 and ball_pos_x > 10 and ball_pos_y > player1_pos_y - 50 and ball_pos_y < player1_pos_y + 50:
        ball_vel_x = -ball_vel_x

    # bounce ball off right paddle
    if ball_pos_x > width - 20 and ball_pos_x < width - 10 and ball_pos_y > player2_pos_y and ball_pos_y < player2_pos_y + 100:
        ball_vel_x = -ball_vel_x

    # player 1 scores
    if ball_pos_x > 1200:
        ball_pos_x = 500
        ball_pos_y = 250
        player1_score += 1

    # player 2 scores
    if ball_pos_x < -200:
        ball_pos_x = 500
        ball_pos_y = 250
        player2_score += 1

    # bounce ball up and down
    if ball_pos_y > height:
        ball_vel_y = -ball_vel_y
    if ball_pos_y < 0:
        ball_vel_y = -ball_vel_y

    # score
    font = pygame.font.SysFont(None, 72)
    text1 = font.render(str(player1_score), True, WHITE)
    screen.blit(text1, (400, 0))

    text2 = font.render(str(player2_score), True, WHITE)
    screen.blit(text2, (600, 0))

    if player1_score > 9:
        text3 = font.render("Player 1 Wins!", True, WHITE)
        screen.blit(text3, (width / 2 - 150, height / 2))
        ball_vel_x = 0
    if player2_score > 9:
        text3 = font.render("Player 2 Wins!", True, WHITE)
        screen.blit(text3, (width / 2 - 150, height / 2))
        ball_vel_x = 0

    # update screen command
    pygame.display.flip()

    # press a button to start the game
    if i == 0:
        font = pygame.font.SysFont(None, 72)
        text1 = font.render("Press space when ready...", True, WHITE)
        screen.blit(text1, (width / 4, height / 4))
        pygame.display.flip()
        while wait == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    wait = True

    i += 1

# Be IDLE friendly
pygame.quit()