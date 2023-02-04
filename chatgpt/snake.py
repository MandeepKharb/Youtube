import pygame
import random

# Initialize the game
pygame.init()

# Set the game screen size
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the game title
pygame.display.set_caption("Snake Game")

# Set the clock for controlling game speed
clock = pygame.time.Clock()

# Set the block size and font size
block_size = 10
font_size = 20
font = pygame.font.Font(None, font_size)

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Define the initial position of the snake
snake_x = 300
snake_y = 300
snake_list = [(snake_x, snake_y)]

# Define the initial position of the food
food_x = random.randint(0, screen_width / block_size - 1) * block_size
food_y = random.randint(0, screen_height / block_size - 1) * block_size

# Define the initial direction of the snake
dx = 0
dy = -block_size

# Define the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current keys that are pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        dx = 0
        dy = -block_size
    if keys[pygame.K_DOWN]:
        dx = 0
        dy = block_size
    if keys[pygame.K_LEFT]:
        dx = -block_size
        dy = 0
    if keys[pygame.K_RIGHT]:
        dx = block_size
        dy = 0

    # Update the position of the snake
    snake_x += dx
    snake_y += dy
    snake_list.insert(0, (snake_x, snake_y))

    # Check if the snake has collided with the food
    if snake_x == food_x and snake_y == food_y:
        # Generate a new food position
        food_x = random.randint(0, screen_width / block_size - 1) * block_size
        food_y = random.randint(0, screen_height / block_size - 1) * block_size
    else:
        snake_list.pop()

    # Check if the snake has collided with the walls
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        running = False

    # Check if the snake has collided with itself
    for block in snake_list[1:]:
        if snake_x == block[0] and snake_y == block[1]:
            running = False

    # Draw the game screen
    screen.fill(black)
    for block in snake_list:
        pygame.draw.rect(screen, green, (block[0], block[1], block_size, block_size))
    pygame.draw.rect(screen, red, (food_x, food_y, block_size, block_size))
    pygame.display.update()

    # Set the clock tick rate
    clock.tick(10)

# Quit the game
pygame.quit()