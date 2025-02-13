import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)
        pass

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        pass

    def split(self) -> None:
        # Original size will always be destroyed
        self.kill()
        # Small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle: float = random.uniform(20, 50)
        shard_pos_angle = Asteroid(self.position[0], self.position[1], \
                self.radius - ASTEROID_MIN_RADIUS)
        shard_pos_angle.velocity = self.velocity.rotate(split_angle) * 1.2

        shard_neg_angle = Asteroid(self.position[0], self.position[1], \
                self.radius - ASTEROID_MIN_RADIUS)
        shard_neg_angle.velocity = self.velocity.rotate(-split_angle) * 1.2
        pass

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        pass



