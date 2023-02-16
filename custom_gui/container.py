import pygame
import json

import color

class Container:
    def __init__(self, window, position: pygame.math.Vector2, size=pygame.math.Vector2(0, 0)) -> None:
        self.window = window
        self.position = position
        self.size = size
        self.color_manager = color.Color()
        self.update = False
        self.is_visible = True
    
    def set_position(self, new_position: pygame.math.Vector2):
        self.position = new_position
        self.update = True
    
    def get_position(self):
        return self.position

    def check_update(self):
        return self.update
    
    def update_finished(self):
        self.update = False

    def check_if_visible(self):
        return self.is_visible
        
    def set_invisible(self):
        self.is_visible = False

    def set_visible(self):
        self.is_visible = True
    
    def draw(self):
        if True == self.check_if_visible():
            pygame.draw.rect(self.window, color=self.color_manager.black, rect=pygame.Rect(self.position.x-5, self.position.y, self.size.x+10, self.size.y), border_radius=5)