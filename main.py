import pygame
from constants import *
from player import Player

def main():
    pygame.init()    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        dt = clock.tick(60) / 1000
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        

        

pygame.quit()


if __name__ == "__main__":
    main()
