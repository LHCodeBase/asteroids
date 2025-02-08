import pygame
from constants import *
from player import Player
if DEBUG:
    import debug

def main():
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    # Set clock
    clock = pygame.time.Clock()
    dt = 0

    # Set initial groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Set initial screen size
    keepGoing = True
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while keepGoing:
        # Exit if user clicks X on window (Needed for mac)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                return # breaks out of parent function

        # Decouple FPS from CPU clock
        dt = (clock.tick(60) / 1000) # pause 1/60th of a second

        # Background
        screen.fill('black') # NOTE: rgb should be 255, 0, 0 or '#ffffff'

        for d in drawable:
            d.draw(screen)
        for u in updatable:
            u.update(dt)

        debug.show_variables(screen)

        pygame.display.flip() # Render screen

    pygame.quit()
    pass

if __name__ == "__main__":
    print("Starting asteroids!")
    main()
