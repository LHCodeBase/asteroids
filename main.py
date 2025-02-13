import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Set initial screen size
    keepGoing = True
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

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

        # Check for player collision
        if any([player.isColliding(a) for a in asteroids if asteroids]):
            print("Game over!")
            pygame.quit()
            break;

        # Check for asteroid / shot collision
        for shot in shots:
            for asteroid in asteroids:
                if asteroid and shot.isColliding(asteroid):
                    asteroid.split()
                    shot.kill()

        debug.show_variables(screen)

        pygame.display.flip() # Render screen

    pygame.quit()
    pass

if __name__ == "__main__":
    print("Starting asteroids!")
    main()
