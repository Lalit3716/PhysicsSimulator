import pygame
import pymunk
from pymunk.pygame_util import DrawOptions
from shapes import *

# All Simulation/Physics happens here


class Simulator:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.space = pymunk.Space()
        self.space.gravity = 0, 900
        self.draw_options = DrawOptions(self.screen)
        Box(self.space, (0, 0), (screen.get_width(), screen.get_height()))

    def get_input(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Circle(self.space, event.pos)

    def run(self, dt) -> None:
        self.space.debug_draw(self.draw_options)
        self.space.step(dt)
