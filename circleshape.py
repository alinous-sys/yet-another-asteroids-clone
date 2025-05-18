import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self,x,y,radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def is_collided(self, shape):
        distance = self.position.distance_to(shape.position)
        radius_combined = self.radius + shape.radius
        if distance <= radius_combined:
            return True
        else:
            return False