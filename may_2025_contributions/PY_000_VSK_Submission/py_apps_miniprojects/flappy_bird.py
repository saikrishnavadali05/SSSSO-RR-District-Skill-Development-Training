import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)

# Load bird image
BIRD = pygame.Rect(100, HEIGHT // 2, 30, 30)

# Physics
gravity = 0.5
bird_movement = 0
flap_strength = -10

# Pipes
pipe_width = 60
pipe_gap = 150
pipe_list = []
pipe_timer = pygame.USEREVENT
pygame.time.set_timer(pipe_timer, 1500)

def create_pipe():
    height = random.randint(100, 400)
    top = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return top, bottom

def move_pipes(pipes):
    for pipe in pipes:
        pipe.x -= 5
    return [pipe for pipe in pipes if pipe.x > -pipe_width]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(SCREEN, (0, 255, 0), pipe)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    SCREEN.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = flap_strength

        if event.type == pipe_timer:
            pipe_list.extend(create_pipe())

    # Bird physics
    bird_movement += gravity
    BIRD.y += int(bird_movement)

    # Pipe movement
    pipe_list = move_pipes(pipe_list)

    # Collision
    for pipe in pipe_list:
        if BIRD.colliderect(pipe):
            print("Game Over")
            pygame.quit()
            sys.exit()

    # Draw
    pygame.draw.ellipse(SCREEN, (255, 255, 0), BIRD)
    draw_pipes(pipe_list)

    pygame.display.update()

pygame.quit()
