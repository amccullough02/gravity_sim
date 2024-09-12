import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, vsync=1)
pygame.display.set_caption("N-body Sim")

BLACK = (0, 0, 0)


class Planet:
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
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.colour, (x, y), self.radius)


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill(BLACK)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()
