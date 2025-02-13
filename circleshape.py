from __future__ import annotations # Allow typehint before class is initialized
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int) -> None:
        # we will use this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.x = lambda: self.position[0]
        self.y = lambda: self.position[1]

    def draw(self, screen: pygame.Surface) -> None:
        # sub-classes must override
        pass

    def update(self, dt: float) -> None:
        # sub-classes must override
        pass

    def isColliding(self, other: CircleShape) -> bool:
        if self.position.distance_to(other.position) <= (self.radius + other.radius):
            return True
        return False
