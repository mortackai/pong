# Import libraries
import pygame
from math import pi
import keyboard
import time
from pongGame import Game
#import pongServer
#import pongClient

BLACK=(0,0,0)
WHITE=(254,255,255)

# Initialize the game engine and font
pygame.init()
pygame.font.init()
 
# Define the colors we will use in RGB format

#this input needs to be sanitized
#select difficulty of the game
difficulty = 5 #int(input("Enter 1-9 for difficulty: "))

# Set the height and width of the screen
size = width, height =  [1000, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong!")

game = Game(width, height, difficulty)

#Loop until the user clicks the close button.
done = False
multi_local_done = False
clock = pygame.time.Clock()

#menu screen
menu = False
difficulty_menu = True
multi_menu = True
menu1 = 0
menu2 = 0


#initial menu to select single or multi player
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

#second menu for singleplayer to select difficulty
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

#second menu for multiplayer to select splitscreen, host a game or join one
while multi_menu == False:
    clock.tick(10)
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 72)
    text_multi = font.render("Select multi options", True, WHITE)
    text_split = font.render("Split-Screen", True, WHITE)
    text_host = font.render("Host", True, WHITE)
    text_join = font.render("Join", True, WHITE)
    screen.blit(text_multi,(width/4,100))
    screen.blit(text_split,(width/4,200))
    screen.blit(text_host,(width/4,250))
    screen.blit(text_join,(width/4,300))
    if menu2 == 0:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),225], 5)
    if menu2 == 1:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),275], 5)
    if menu2 == 2:
        pygame.draw.circle(screen, WHITE, [int(width/4-10),325], 5)

    pygame.display.flip()

    if keyboard.is_pressed('w') or keyboard.is_pressed('UP') and menu2 > 0:
        menu2 -= 1
    if keyboard.is_pressed('s') or keyboard.is_pressed('DOWN') and menu2 < 2:
        menu2 += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
            menu = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and menu2 == 0:
            multi_menu = True
            multi_local_done = True
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and menu2 == 1:
            multi_menu = True
            multi_local_done = True
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and menu2 == 2:
            multi_menu = True
            multi_local_done = True
            done = True

game.run(done, multi_local_done, screen)

# Be IDLE friendly
pygame.quit()
