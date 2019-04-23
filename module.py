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

#Loop until the user clicks the close button.
done = False
multi_local_done = False
clock = pygame.time.Clock()

class menu:
  def __init__(self, title, option1, option2, option3):
    self.title = title
    self.option1 = option1
    self.option2 = option2
    self.option3 = option3


  def two_option_menu(title,option1,option2):
    done = False
    selection = 0
    while not done:
        clock.tick(20)
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 72)
        text_title = font.render(title, True, WHITE)
        text_option1 = font.render(option1, True, WHITE)
        text_option2 = font.render(option2, True, WHITE)
        screen.blit(text_title,(width/4,100))
        screen.blit(text_option1,(width/4,200))
        screen.blit(text_option2,(width/4,250))
        
        if selection == 0:
            pygame.draw.circle(screen, WHITE, [int(width/4-10),225], 5)
        if selection == 1:
            pygame.draw.circle(screen, WHITE, [int(width/4-10),275], 5)

        if keyboard.is_pressed('w') or keyboard.is_pressed('UP'):
            selection = 0
        if keyboard.is_pressed('s') or keyboard.is_pressed('DOWN'):
            selection = 1

        pygame.display.flip()

'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and selection == 0:
                print(option1 + " has been selected")
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and selection == 1:
                print(option2 + " has been selected")
                return
'''




'''
  def three_option_menu(title,option1,option2,option3):
    done = False
    selection = 0
    while not done:
        clock.tick(20)
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 72)
        text_title = font.render(title, True, WHITE)
        text_option1 = font.render(option1, True, WHITE)
        text_option2 = font.render(option2, True, WHITE)
        text_option3 = font.render(option3, True, WHITE)
        screen.blit(text_title,(width/4,100))
        screen.blit(text_option1,(width/4,200))
        screen.blit(text_option2,(width/4,250))
        screen.blit(text_option3,(width/4,300))
        
        if selection == 0:
            pygame.draw.circle(screen, WHITE, [int(width/4-10),225], 5)
        if selection == 1:
            pygame.draw.circle(screen, WHITE, [int(width/4-10),275], 5)

        if keyboard.is_pressed('w') or keyboard.is_pressed('UP'):
            selection = 0
        if keyboard.is_pressed('s') or keyboard.is_pressed('DOWN'):
            selection = 1

        pygame.display.flip()
'''
