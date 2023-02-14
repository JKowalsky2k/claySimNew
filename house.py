import pygame
import color

class House:
    def __init__(self, window, position=pygame.math.Vector2(0, 0), size=pygame.math.Vector2(50, 50), color=color.Color().brown) -> None:
        self.window = window
        self.position = position
        self.size = size
        self.color = color
        self.movable = False
        self.add_status = False
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.Rect(self.position, self.size)
        self.rect.center = self.position

    def set_position(self, new_position: pygame.math.Vector2):
        self.position.update(new_position)
        self.update_rect()

    def set_position_x(self, new_x: int):
        self.position.x = new_x
        self.update_rect()
    
    def set_position_y(self, new_y: int):
        self.position.y = new_y
        self.update_rect()

    def set_size(self, new_size: pygame.math.Vector2):
        self.size.update(new_size)
        self.update_rect()

    def set_movable(self, state: bool):
        self.movable = state
    
    def add(self):
        self.add_status = True
    
    def remove(self):
        self.add_status = False
    
    def is_added(self):
        return self.add_status

    def is_movable(self):
        return self.movable

    def get_rect(self):
        return self.rect

    def get_position(self):
        return self.position

    def draw(self):
        pygame.draw.rect(self.window, color=self.color, rect=self.rect)