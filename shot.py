import pygame
from circleshape import CircleShape 
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED

class Shot(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, SHOT_RADIUS)
        pass

    def draw(self, screen: pygame.Surface) -> pygame.Rect:
        pygame.draw.circle(screen, 'orange', self.position, self.radius)
    
    def update(self, dt: float) -> None: 
        self.position += self.velocity * dt
        pass
