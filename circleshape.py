import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int):
        # we will use this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

        def draw(self, screen):
            # sub-classes must override
            pass

        def update(self, dt):
            # sub-classes must override
            pass

        def isColliding(self, other: CircleShape) -> bool:
            if self.distance_to(other) <= (self.radius + other.radius):
                return True
            return False
            pass
