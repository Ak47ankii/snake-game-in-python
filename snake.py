import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SNAKE_COLOR = (0, 128, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (255, 255, 255)

# Snake directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Function to draw the snake
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Function to generate food at a random position
def generate_food():
    while True:
        food_pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if food_pos not in snake:
            return food_pos

# Check for collision with the food
def check_food_collision(snake_head, food_pos):
    return snake_head == food_pos

# Check for collision with the boundaries or itself
def check_collision(snake):
    head = snake[0]
    return (
        head[0] < 0 or head[0] >= GRID_WIDTH or
        head[1] < 0 or head[1] >= GRID_HEIGHT or
        head in snake[1:]
    )

# Initialize the game
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
direction = RIGHT
food_pos = generate_food()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            elif event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            elif event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    # Move the snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Check for collisions
    if check_collision(snake):
        pygame.quit()
        sys.exit()

    # Check for food collision
    if check_food_collision(new_head, food_pos):
        food_pos = generate_food()
    else:
        snake.pop()

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    draw_snake(snake)
    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food_pos[0] * GRID_SIZE, food_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.display.flip()

    # Control game speed
    clock.tick(7)  # Adjust this value to control the game speed
