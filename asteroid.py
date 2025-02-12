import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)
        pass

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        pass

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        pass


