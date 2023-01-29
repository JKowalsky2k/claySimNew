import pygame

class Container:
    def __init__(self, position: pygame.math.Vector2) -> None:
        self.position = position
        self.update = False
    
    def set_position(self, new_position: pygame.math.Vector2):
        self.position = new_position
        self.update = True
    
    def get_position(self):
        return self.position

    def check_update(self):
        return self.update
    
    def update_finished(self):
        self.update = False