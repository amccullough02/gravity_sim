import pygame
import math
from body import Body
from constants import HEIGHT, WIDTH, BLACK, YELLOW

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, vsync=1)
pygame.display.set_caption("N-body Sim")

sun = Body(0, 0, 30, 1.98892 * 10**30, YELLOW)
sun.is_sun = True

bodies = [sun]


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for body in bodies:
            body.draw(WIN)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
