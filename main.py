import pygame
from constants import *

def main():
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    keepGoing = True
    # Set initial screen size
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    while keepGoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        pygame.display.flip()
    pass

if __name__ == "__main__":
    print("Starting asteroids!")
    main()
