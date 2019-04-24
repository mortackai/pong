# Import libraries
import pygame
from math import pi
import keyboard
import time

BLACK = (0,0,0)
WHITE = (255,255,255)

class Game:
    """A game of pong"""

    def __init__(self,width,height,difficulty):
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.ball_pos_x = width/2
        self.ball_pos_y = height/2
        self.ball_vel_x = -difficulty
        self.ball_vel_y = -difficulty
        self.player2_pos_y = height/2
        self.AI_speed = difficulty + 1
        self.player1_score = 0
        self.player2_score = 0
        self.keys = pygame.key.get_pressed()
        self.last_mouse_y = height/2
        self.player1_pos_y = height/2

    def run(self, done, multi_local_done, screen):

        clock = pygame.time.Clock()

        wait = False
        i = 0

        while not done:
         
            # limits while loop to max of ___ times per second.
            clock.tick(100)
             
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop
         
            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.
             
            # Clear the screen and set the screen background
            screen.fill(BLACK)
                
            # controls
            pygame.mouse.set_visible(False)
                
            # mouse controls
            current_mouse_y = pygame.mouse.get_pos()
            if current_mouse_y != self.last_mouse_y:
                mouse_pos = player_pos_x, self.player1_pos_y = pygame.mouse.get_pos()
            self.last_mouse_y = current_mouse_y

            # keyboard controls
            if keyboard.is_pressed('w'):
                self.player1_pos_y -= 10
            if keyboard.is_pressed('s'):
                self.player1_pos_y += 10
            
            # Draw a rectangle outline
            pygame.draw.rect(screen, WHITE, [10, self.player1_pos_y-50, 10, 100], 0)
            pygame.draw.rect(screen, WHITE, [980, self.player2_pos_y, 10, 100], 0)
            pygame.draw.circle(screen, WHITE, [int(self.ball_pos_x), int(self.ball_pos_y)], 5)

            # move the ball everyframe by its velocity
            self.ball_pos_x += self.ball_vel_x
            self.ball_pos_y += self.ball_vel_y

            # bounce ball off left paddle
            if 20 > self.ball_pos_x > 10 and self.player1_pos_y - 50 < self.ball_pos_y < self.player1_pos_y + 50:
                self.ball_vel_x = -self.ball_vel_x

            # bounce ball off right paddle
            if self.width - 20 < self.ball_pos_x < self.width - 10 and self.player2_pos_y < self.ball_pos_y < self.player2_pos_y + 100:
                self.ball_vel_x = -self.ball_vel_x

            # player 1 scores
            if self.ball_pos_x > 1200:
                self.ball_pos_x = 500
                self.ball_pos_y = 250
                self.player1_score += 1

            # player 2 scores
            if self.ball_pos_x < -200:
                self.ball_pos_x = 500
                self.ball_pos_y = 250
                self.player2_score += 1

                
            # bounce ball up and down
            if self.ball_pos_y > self.height:
                self.ball_vel_y = -self.ball_vel_y
            if self.ball_pos_y < 0:
                self.ball_vel_y = -self.ball_vel_y

            # enemy AI
            if self.ball_pos_y > self.player2_pos_y+50:
                self.player2_pos_y += self.AI_speed
            if self.ball_pos_y < self.player2_pos_y:
                self.player2_pos_y -= self.AI_speed


            # score
            font = pygame.font.SysFont(None, 72)
            text1 = font.render(str(self.player1_score), True, WHITE)
            screen.blit(text1,(400,0))

            text2 = font.render(str(self.player2_score), True, WHITE)
            screen.blit(text2,(600,0))

            if self.player1_score > 9:
                text3 = font.render("Player 1 Wins!", True, WHITE)
                screen.blit(text3,(self.width/2-150,self.height/2))
                self.ball_vel_x = 0
            if self.player2_score > 9:
                text3 = font.render("Player 2 Wins!", True, WHITE)
                screen.blit(text3,(self.width/2-150,self.height/2))
                self.ball_vel_x = 0
            
            # update screen command
            pygame.display.flip()

            # press a button to start the game
            if i == 0:
                font = pygame.font.SysFont(None, 72)
                text1 = font.render("Press space when ready...", True, WHITE)
                screen.blit(text1,(self.width/4,self.height/4))
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
             
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done=True # Flag that we are done so we exit this loop
         
            # All drawing code happens after the for loop and but
            # inside the main while done==False loop.
             
            # Clear the screen and set the screen background
            screen.fill(BLACK)
                
            # controls
            pygame.mouse.set_visible(False)
                
            # mouse controls
            current_mouse_y = pygame.mouse.get_pos()
            if current_mouse_y != self.last_mouse_y:
                mouse_pos = player_pos_x, self.player1_pos_y = pygame.mouse.get_pos()
            self.last_mouse_y = current_mouse_y

            # keyboard controls
            if keyboard.is_pressed('w'):
                self.player1_pos_y -= 10
            if keyboard.is_pressed('s'):
                self.player1_pos_y += 10
            if keyboard.is_pressed('UP'):
                self.player2_pos_y -= 10
            if keyboard.is_pressed('DOWN'):
                self.player2_pos_y += 10


            # Draw a rectangle outline
            pygame.draw.rect(screen, WHITE, [10, self.player1_pos_y-50, 10, 100], 0)
            pygame.draw.rect(screen, WHITE, [980, self.player2_pos_y, 10, 100], 0)
            pygame.draw.circle(screen, WHITE, [int(self.ball_pos_x), int(self.ball_pos_y)], 5)

            # move the ball everyframe by its velocity
            self.ball_pos_x += self.ball_vel_x
            self.ball_pos_y += self.ball_vel_y

            # bounce ball off left paddle
            if self.ball_pos_x < 20 and self.ball_pos_x > 10 and self.ball_pos_y > self.player1_pos_y-50 and self.ball_pos_y < self.player1_pos_y+50:
                self.ball_vel_x = -self.ball_vel_x

            # bounce ball off right paddle
            if self.ball_pos_x > self.width-20 and self.ball_pos_x < self.width-10 and self.ball_pos_y > self.player2_pos_y and self.ball_pos_y < self.player2_pos_y+100:
                self.ball_vel_x = -self.ball_vel_x

            # player 1 scores
            if self.ball_pos_x > 1200:
                self.ball_pos_x = 500
                self.ball_pos_y = 250
                self.player1_score += 1

            # player 2 scores
            if self.ball_pos_x < -200:
                self.ball_pos_x = 500
                self.ball_pos_y = 250
                self.player2_score += 1

                
            # bounce ball up and down
            if self.ball_pos_y > self.height:
                self.ball_vel_y = -self.ball_vel_y
            if self.ball_pos_y < 0:
                self.ball_vel_y = -self.ball_vel_y

            # score
            font = pygame.font.SysFont(None, 72)
            text1 = font.render(str(self.player1_score), True, WHITE)
            screen.blit(text1,(400,0))

            text2 = font.render(str(self.player2_score), True, WHITE)
            screen.blit(text2,(600,0))

            if self.player1_score > 9:
                text3 = font.render("Player 1 Wins!", True, WHITE)
                screen.blit(text3,(self.width/2-150,self.height/2))
                self.ball_vel_x = 0
            if self.player2_score > 9:
                text3 = font.render("Player 2 Wins!", True, WHITE)
                screen.blit(text3,(self.width/2-150,self.height/2))
                self.ball_vel_x = 0
            
            # update screen command
            pygame.display.flip()

            # press a button to start the game
            if i == 0:
                font = pygame.font.SysFont(None, 72)
                text1 = font.render("Press space when ready...", True, WHITE)
                screen.blit(text1,(self.width/4,self.height/4))
                pygame.display.flip()
                while wait == False:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            wait = True
                        
            i += 1
