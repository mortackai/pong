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

#this input needs to be sanitized
#select difficulty of the game
difficulty = 5 #int(input("Enter 1-9 for difficulty: "))

# Set the height and width of the screen
size = width, height =  [1000, 500]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong!")

class menu:
    def __init__(self, title, option1, option2, option3):
        self.title = title
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.selection = 0

    def two_option_menu(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            if keyboard.is_pressed('ESC'):
                done = True
            clock.tick(20)
            screen.fill(BLACK)
            font = pygame.font.SysFont(None, 72)
            text_title = font.render(self.title, True, WHITE)
            text_option1 = font.render(self.option1, True, WHITE)
            text_option2 = font.render(self.option2, True, WHITE)
            screen.blit(text_title,(width/4,100))
            screen.blit(text_option1,(width/4,200))
            screen.blit(text_option2,(width/4,250))

            if self.selection == 0:
                pygame.draw.circle(screen, WHITE, [int(width/4-10),225], 5)
            if self.selection == 1:
                pygame.draw.circle(screen, WHITE, [int(width/4-10),275], 5)
                
            if keyboard.is_pressed('w') or keyboard.is_pressed('UP'):
                self.selection = 0
            if keyboard.is_pressed('s') or keyboard.is_pressed('DOWN'):
                self.selection = 1

            if keyboard.is_pressed('ENTER') or keyboard.is_pressed('SPACE'):
                done = True

            pygame.display.flip()

    def three_option_menu(self):
        done = False
        clock = pygame.time.Clock()
        while not done:
            if keyboard.is_pressed('ESC'):
                done = True
            clock.tick(20)
            screen.fill(BLACK)
            font = pygame.font.SysFont(None, 72)
            text_title = font.render(self.title, True, WHITE)
            text_option1 = font.render(self.option1, True, WHITE)
            text_option2 = font.render(self.option2, True, WHITE)
            text_option3 = font.render(self.option3, True, WHITE)
            screen.blit(text_title,(width/4,100))
            screen.blit(text_option1,(width/4,200))
            screen.blit(text_option2,(width/4,250))
            screen.blit(text_option3,(width/4,300))

            if self.selection == 0:
                pygame.draw.circle(screen, WHITE, [int(width/4-10),225], 5)
            if self.selection == 1:
                pygame.draw.circle(screen, WHITE, [int(width/4-10),275], 5)
                
            if keyboard.is_pressed('w') or keyboard.is_pressed('UP'):
                self.selection = 0
            if keyboard.is_pressed('s') or keyboard.is_pressed('DOWN'):
                self.selection = 1

            if keyboard.is_pressed('ENTER') or keyboard.is_pressed('SPACE'):
                done = True

            pygame.display.flip()

