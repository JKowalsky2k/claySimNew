import pygame
import color
import custom_gui.container as container

class DefaultElement:
    def __init__(   self, window, 
                    position, 
                    size, 
                    text,
                    font_size,
                    container
                ) -> None:
        self.color_manager = color.Color()
        self.color = self.color_manager.white
        self.window = window
        self.font = pygame.font.SysFont(None, font_size)
        self.text = self.font.render(f'{text}', True, self.color_manager.white)
        self.relative_position = position
        self.position = container.get_position() + self.relative_position
        self.size = size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.container = container
        self.visiblity = True

    def set_text(self, text: str):
        self.text = self.font.render(f'{text}', True, self.color_manager.white)

    def set_size(self, new_size: pygame.math.Vector2):
        self.size = new_size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def update_position(self):
        self.position = self.container.get_position() + self.relative_position
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def set_postion(self, new_position: pygame.math.Vector2):
        self.relative_position = new_position
        self.update_position()

    def is_visible(self):
        return self.visiblity
        
    def invisible(self):
        self.visiblity = False

    def visible(self):
        self.visiblity = True
