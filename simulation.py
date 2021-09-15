import pygame
from simulator import Simulator

# Constants
WINDOW_SIZE = 1280, 720
FPS = 60

# Screen Variables
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Simulator")

# Create Simulation
simulation = Simulator(screen)

# Main Loop
while True:
    screen.fill("grey")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        simulation.get_input(event)

    # Run Simulation
    simulation.run(dt=1 / FPS)

    pygame.display.update()
    clock.tick(FPS)
