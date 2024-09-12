import pygame
from constants import HEIGHT, WIDTH


class Body:
    AU = (149.6e6 * 1000)  # Distance from Sun in meters.
    G = 6.67428e-11  # Gravitational constant.
    SCALE = 250 / AU  # 1AU = 100 pixels
    TIMESTEP = 86400  # 1 day in seconds

    def __init__(self, x, y, radius, mass, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.colour = colour

        self.orbit = []
        self.is_sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.colour, (x, y), self.radius)
