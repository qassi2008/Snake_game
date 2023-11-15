import pygame
import random

pygame.init()
# Initialize the score
score = 0
# Screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
# Colors
black, white, red, green = (0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0)
# Snake
snake_pos = [[100, 50], [90, 50], [80, 50]]
# Food
food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
# Set FPS
clock = pygame.time.Clock()
fps = 10
# Initialize direction
direction = "RIGHT"
last_direction = "RIGHT"
# Initialize font
font = pygame.font.SysFont("comicsansms", 35)
# Game Over settings
gameover = False

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and last_direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and last_direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and last_direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and last_direction != "LEFT":
                direction = "RIGHT"

    # Move snake
    new_head = list(snake_pos[0])
    if direction == "UP":
        new_head[1] -= 10
    if direction == "DOWN":
        new_head[1] += 10
    if direction == "LEFT":
        new_head[0] -= 10
    if direction == "RIGHT":
        new_head[0] += 10

    # Insert new head of the snake
    snake_pos.insert(0, list(new_head))

    # Check for food collision
    if snake_pos[0] == food_pos:
        score += 1  # Increment score
        food_pos = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10]
    else:
        snake_pos.pop()

    # Check for self-collision
    if snake_pos[0] in snake_pos[1:]:
        gameover = True
        text = font.render("Game Over! You collided with yourself.", True, red)
        screen.blit(text, [width // 4, height // 3])
        pygame.display.flip()
        pygame.time.wait(20000)

    # Check for wall collision
    if new_head[0] >= width or new_head[0] < 0 or new_head[1] >= height or new_head[1] < 0:
        gameover = True
        text = font.render("Game Over! You hit the wall.", True, red)
        screen.blit(text, [width // 4, height // 3])
        pygame.display.flip()
        pygame.time.wait(20000)

    # Update last_direction
    last_direction = direction

    # Draw everything: snake, food, and score
    screen.fill(black)
    # Draw the score
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, [0, 0])  # Adjust the position as needed

    # Draw snake and food
    for pos in snake_pos:
        pygame.draw.rect(screen, green if pos == snake_pos[0] else white, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()