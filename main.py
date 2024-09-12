import pygame
from body import Body
from constants import (HEIGHT, WIDTH, BLACK, YELLOW, BLUE, RED, DARK_GREY,
                       LIGHT_YELLOW)

pygame.init()
pygame.display.set_caption("N-body Sim")

WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF, vsync=1)
FONT = pygame.font.SysFont("comicsans", 16)

# Bodies

sun = Body(0, 0, 30, 1.98892 * 10**30, YELLOW)
sun.is_sun = True

mercury = Body(0.387 * Body.AU, 0, 8, 0.330 * 10**24, DARK_GREY)
mercury.y_vel = -47.4 * 1000

venus = Body(0.723 * Body.AU, 0, 14, 4.86 * 10**24, LIGHT_YELLOW)
venus.y_vel = -35.02 * 1000

earth = Body(-1 * Body.AU, 0, 16, 5.9742 * 10**24, BLUE)
earth.y_vel = 29.783 * 1000

mars = Body(-1.524 * Body.AU, 0, 12, 6.39 * 10**23, RED)
mars.y_vel = 24.077 * 1000

bodies = [sun, mercury, venus, earth, mars]


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
            body.update_position(bodies)
            body.draw(WIN, FONT)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
