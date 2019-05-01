import pygame
import keyboard

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class game:

    def __init__(self, width, height, ball_speed):

        self.width = width
        self.height = height
        self.ball_speed = ball_speed
        self.size = width, height
        self.player2_pos_y = height / 2


    def run(self):
        # Initialize the game engine and font
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("pong!")
        clock = pygame.time.Clock()
        keys = pygame.key.get_pressed()
        i = 0
        wait = False

        ball_pos_x = self.width / 2
        ball_pos_y = self.height / 2
        ball_vel_x = -self.ball_speed
        ball_vel_y = -self.ball_speed
        AI_speed = self.ball_speed + 1
        player1_score = 0
        player2_score = 0
        player1_pos_y = self.height / 2
        last_mouse_y = self.height / 2
        done = False

        # Set the height and width of the screen
        screen = pygame.display.set_mode(self.size)

        while not done:

            clock.tick(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            screen.fill(BLACK)

            # controls
            pygame.mouse.set_visible(False)

            # mouse controls
            current_mouse_y = pygame.mouse.get_pos()
            if current_mouse_y != last_mouse_y:
                mouse_pos = player_pos_x, player1_pos_y = pygame.mouse.get_pos()
            last_mouse_y = current_mouse_y

            # keyboard controls
            if keyboard.is_pressed('w') and player1_pos_y > 0:
                player1_pos_y -= 10
            if keyboard.is_pressed('s') and player1_pos_y < self.height:
                player1_pos_y += 10

            # Draw a rectangle outline
            pygame.draw.rect(screen, WHITE, [10, player1_pos_y - 50, 10, 100], 0)
            pygame.draw.rect(screen, WHITE, [980, self.player2_pos_y, 10, 100], 0)
            pygame.draw.circle(screen, WHITE, [int(ball_pos_x), int(ball_pos_y)], 5)

            # move the ball everyframe by its velocity
            ball_pos_x += ball_vel_x
            ball_pos_y += ball_vel_y

            # bounce ball off left paddle
            if 20 > ball_pos_x > 10 and player1_pos_y - 50 < ball_pos_y < player1_pos_y + 50:
                ball_vel_x = -ball_vel_x

            # bounce ball off right paddle
            if self.width - 20 < ball_pos_x < self.width - 10 and self.player2_pos_y < ball_pos_y < self.player2_pos_y + 100:
                ball_vel_x = -ball_vel_x
            # print(ball_pos_y)

            # player 1 scores
            if ball_pos_x > self.width + 200:
                ball_pos_x = 500
                ball_pos_y = 250
                player1_score += 1

            # player 2 scores
            if ball_pos_x < -200:
                ball_pos_x = 500
                ball_pos_y = 250
                player2_score += 1

            # bounce ball up and down
            if ball_pos_y > self.height:
                ball_vel_y = -ball_vel_y
            if ball_pos_y < 0:
                ball_vel_y = -ball_vel_y

            # enemy AI
            if ball_pos_y > self.player2_pos_y + 50:
                self.player2_pos_y += AI_speed
            if ball_pos_y < self.player2_pos_y:
                self.player2_pos_y -= AI_speed

            # score
            font = pygame.font.SysFont(None, 72)
            text1 = font.render(str(player1_score), True, WHITE)
            screen.blit(text1, (400, 0))

            text2 = font.render(str(player2_score), True, WHITE)
            screen.blit(text2, (600, 0))

            if player1_score > 9:
                text3 = font.render("Player 1 Wins!", True, WHITE)
                screen.blit(text3, (self.width / 2 - 150, self.height / 2))
                ball_vel_x = 0
            if player2_score > 9:
                text3 = font.render("Player 2 Wins!", True, WHITE)
                screen.blit(text3, (self.width / 2 - 150, self.height / 2))
                ball_vel_x = 0

            # update screen command
            pygame.display.flip()

            # press a button to start the game
            if i == 0:
                font = pygame.font.SysFont(None, 72)
                text1 = font.render("Press space when ready...", True, WHITE)
                screen.blit(text1, (self.width / 4, self.height / 4))
                pygame.display.flip()
                while True:
                    if keyboard.is_pressed('SPACE'):
                        break

            i += 1

        # close program when pygame is exited
        pygame.quit()


#p1 = game(1000, 500, 5)
#p1.run()
