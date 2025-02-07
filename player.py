#!/usr/bin/env python3
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        pass

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * \
                self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = (255, 255, 255)
        pygame.draw.polygon(screen, color, self.triangle(), width=2)
        pass

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        pass

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_h]:
            # rotate "left" counter-clockwise
            self.rotate(dt * -1)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_k]:
            # rotate "right" clockwise
            self.rotate(dt)
        pass
