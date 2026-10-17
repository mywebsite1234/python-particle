import pygame
import sys
import random
from math import *

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Particle System")
clock = pygame.time.Clock()


# List to store all active particles
# Each particle will be represented as a list: [[x, y], [vx, vy], radius, color]
particles = []

def create_particles(pos):
    """Spawns a burst of particles at a given position."""
    # Spawn 20 particles per click
    for _ in range(40):
        # Coordinates
        x, y = pos
        
        # Velocity: random speed between -3 and 3 for both directions
        vx = random.uniform(-4, 4)
        vy = random.uniform(-4, 4) # slightly skewed upwards (-vy goes up)
        
        # Appearance
        radius = 15
        color = (255, 255, 0)
        
        # Append to our tracker
        particles.append([[x, y], [vx, vy], radius, color])

# Main Game Loop
while True:
    screen.fill((20, 20, 30))  # Dark blue-gray background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Trigger particle generation on mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            create_particles(pos)

    # Update and Draw Particles
    # We iterate backwards or safely modify the list to handle removals
    for particle in particles[:]:
        # 1. Update position based on velocity
        particle[0][0] += particle[1][0] # Move X
        particle[0][1] += particle[1][1] # Move Y
        
        # 2. Apply simulated gravity (optional)
        # particle[1][1] += 0.1 
        
        # 3. Shrink the particle over time
        particle[2] -= 0.3
        
        # 4. Remove particle if it shrinks to nothing
        # if particle[2] <= 0:
        #     particles.remove(particle)
        #     continue
        if sqrt((particle[0][1] - pos[1])**2 + (particle[0][0] - pos[0])**2) >= 100:
            particles.remove(particle)
            continue
            
        # 5. Draw the particle as a circle
        pygame.draw.rect(
            screen, 
            particle[3], 
            (int(particle[0][0]), int(particle[0][1]), int(particle[2]), int(particle[2]))
        )
    # Refresh screen
    pygame.display.flip()
    clock.tick(60) # Lock to 60 FPS
