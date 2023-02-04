import pygame

import color

class Point:
    def __init__(self, window, position=pygame.math.Vector2(0, 0), radius=5, color=color.Color().brown) -> None:
        self.window = window
        self.position = position
        self.radius = radius
        self.size = pygame.math.Vector2(2*self.radius, 2*self.radius)
        self.rect = pygame.Rect(self.position, self.size)
        self.color = color
        self.movable = False
        self.offset = pygame.math.Vector2(0, 0)
        self.update_bounding_box()
    
    def update_bounding_box(self):
        self.rect.center = self.position+self.offset

    # def set_radius(self, new_radius):
    #     self.radius = new_radius
    #     self.size = pygame.math.Vector2(2*self.radius, 2*self.radius)
    #     self.update_bounding_box()
    
    def set_position(self, new_position):
        self.position.update(new_position)
        self.update_bounding_box()

    def set_default_posiiton(self):
        self.position.update(pygame.math.Vector2(0, 0))
        self.update_bounding_box()

    def get_position(self):
        return self.position
    
    def get_rect(self):
        return self.rect

    def set_movable(self, state: bool):
        self.movable = state
    
    def set_offset(self, new_offset):
        self.offset.update(new_offset)
        self.update_bounding_box()

    def is_movable(self):
        return self.movable
    
    def draw(self, draw_bbox=True):
        if True == draw_bbox:
            pygame.draw.rect(self.window, color.Color().blue, self.rect)
        pygame.draw.circle(self.window, self.color, self.position+self.offset, self.radius)

    


