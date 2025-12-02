import pygame
import random

# Initialize Pygame
pygame.init()

# Full-screen setup
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Snake Game 🐍")

# Playable area dimensions
PLAY_WIDTH, PLAY_HEIGHT = 600, 400
PLAY_X = (SCREEN_WIDTH - PLAY_WIDTH) // 2
PLAY_Y = (SCREEN_HEIGHT - PLAY_HEIGHT) // 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
PLAY_BG = (50, 153, 213)     # playable area background
OUTSIDE_BG = (30, 30, 30)    # outside playable area

# Snake properties
SNAKE_BLOCK = 20
SNAKE_SPEED = 15

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 35)
score_font = pygame.font.SysFont(None, 30)


def your_score(score):
    value = score_font.render("Score: " + str(score), True, WHITE)
    WINDOW.blit(value, [PLAY_X + 10, PLAY_Y + 10])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    WINDOW.blit(mesg, [PLAY_X + PLAY_WIDTH // 6, PLAY_Y + PLAY_HEIGHT // 3])


def game_loop():
    game_over = False
    game_close = False

    # Initialize snake position (integers!)
    x1 = PLAY_X + PLAY_WIDTH // 2
    y1 = PLAY_Y + PLAY_HEIGHT // 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Place first food
    foodx = PLAY_X + random.randrange(0, PLAY_WIDTH // SNAKE_BLOCK) * SNAKE_BLOCK
    foody = PLAY_Y + random.randrange(0, PLAY_HEIGHT // SNAKE_BLOCK) * SNAKE_BLOCK

    while not game_over:

        # Game-over handling
        while game_close:
            WINDOW.fill(OUTSIDE_BG)
            pygame.draw.rect(WINDOW, PLAY_BG, [PLAY_X, PLAY_Y, PLAY_WIDTH, PLAY_HEIGHT])
            pygame.draw.rect(WINDOW, RED, [PLAY_X, PLAY_Y, PLAY_WIDTH, PLAY_HEIGHT], 4)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        # Reset game state
                        x1 = PLAY_X + PLAY_WIDTH // 2
                        y1 = PLAY_Y + PLAY_HEIGHT // 2
                        x1_change = 0
                        y1_change = 0
                        snake_list = []
                        length_of_snake = 1
                        foodx = PLAY_X + random.randrange(0, PLAY_WIDTH // SNAKE_BLOCK) * SNAKE_BLOCK
                        foody = PLAY_Y + random.randrange(0, PLAY_HEIGHT // SNAKE_BLOCK) * SNAKE_BLOCK
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        # Move snake
        x1 += x1_change
        y1 += y1_change

        # Boundary collision
        if x1 < PLAY_X or x1 >= PLAY_X + PLAY_WIDTH or y1 < PLAY_Y or y1 >= PLAY_Y + PLAY_HEIGHT:
            game_close = True

        # Draw background
        WINDOW.fill(OUTSIDE_BG)
        pygame.draw.rect(WINDOW, PLAY_BG, [PLAY_X, PLAY_Y, PLAY_WIDTH, PLAY_HEIGHT])
        pygame.draw.rect(WINDOW, RED, [PLAY_X, PLAY_Y, PLAY_WIDTH, PLAY_HEIGHT], 4)

        # Draw food
        pygame.draw.rect(WINDOW, GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        # Update snake
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw snake
        for block in snake_list:
            pygame.draw.rect(WINDOW, WHITE, [block[0], block[1], SNAKE_BLOCK, SNAKE_BLOCK])

        # Display score
        your_score(length_of_snake - 1)
        pygame.display.update()

        # Check food collision
        if x1 == foodx and y1 == foody:
            length_of_snake += 1
            foodx = PLAY_X + random.randrange(0, PLAY_WIDTH // SNAKE_BLOCK) * SNAKE_BLOCK
            foody = PLAY_Y + random.randrange(0, PLAY_HEIGHT // SNAKE_BLOCK) * SNAKE_BLOCK

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


if __name__ == "__main__":
    game_loop()
