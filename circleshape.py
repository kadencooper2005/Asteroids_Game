import pygame   # pyright: ignore[reportMissingImports]
from constants import LINE_WIDTH

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass
   
    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        """Check collision with another CircleShape."""
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
   