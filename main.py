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


difficulty = 5

# Set the height and width of the screen
size = width, height =  [1000, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong!")

game = Game(width, height, difficulty)

#Loop until the user clicks the close button.
done = False
multi_local_done = False
clock = pygame.time.Clock()

game.run(done, multi_local_done, screen)

# Be IDLE friendly
pygame.quit()
