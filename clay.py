import pygame
import copy

class Clay(pygame.sprite.Sprite):
    def __init__(self, window, offset, radius) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.window = window
        self.radius = radius
        self.offset = offset
        self.reference_sprite = pygame.image.load("clay.png").convert_alpha()
        self.sprite = copy.copy(self.reference_sprite)
        self.set_position(pygame.math.Vector2(0, 0))
        self.update()

    def update(self):
        self.sprite = pygame.transform.scale(self.reference_sprite, pygame.math.Vector2(2*self.radius, 2*self.radius))

    def set_position(self, new_position):
        self.position = new_position + self.offset - pygame.math.Vector2(self.radius, self.radius)
        self.update()

    def set_offset(self, new_offset):
        self.offset.update(new_offset)

    def increase_radius(self):
        self.radius += 1
    
    def decrease_radius(self):
        self.radius -= 1

    def draw(self):
        pygame.Surface.blit(self.window, self.sprite, self.position)
    
