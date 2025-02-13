#!/usr/bin/env python3
import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        pass

    def triangle(self) -> list[tuple[int, int]]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * \
                self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        color = (255, 255, 255)
        pygame.draw.polygon(screen, color, self.triangle(), width=2)
        pass

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
        pass

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_h]:
            # rotate "left" counter-clockwise
            self.rotate(dt * -1)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_k]:
            # rotate "right" clockwise
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_u]:
            # move forward
            self.move(dt)
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN] or keys[pygame.K_j]:
            # move backward
            self.move(-dt)

        # Rate limit shots
        if 0 == self.timer:
            # Fire shot
            if keys[pygame.K_SPACE]:
                self.shoot()
                self.timer = 0.3
        elif self.timer > 0:
            self.timer -= dt
        else:
            self.timer = 0
        pass

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        # Keep player on screen
        if self.y() > SCREEN_HEIGHT:
            self.position -= pygame.Vector2(0, SCREEN_HEIGHT)
        if self.y() < 0:
            self.position += pygame.Vector2(0, SCREEN_HEIGHT)
        if self.x() > SCREEN_WIDTH:
            self.position -= pygame.Vector2(SCREEN_WIDTH, 0)
        if self.x() < 0:
            self.position += pygame.Vector2(SCREEN_WIDTH, 0)
            pass

    def isColliding(self, other: CircleShape) -> bool:
        if self.position.distance_to(other.position) <= (self.radius + other.radius):
            return True
        return False

    def shoot(self) -> None:
        shot = Shot(self.position[0], self.position[1])
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        pass
