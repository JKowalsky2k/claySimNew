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
        self.raw_text = text
        self.text = self.font.render(f'{text}', True, self.color_manager.white)
        self.relative_position = position
        self.position = self.relative_position
        if None != container:
            self.position = container.get_position() + self.relative_position
        self.size = size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.container = container
        self.is_visible, self.is_enabled = True, True

    def get_info(self):
        print(f"Pos: {(self.position.x, self.position.y) = }")
        print(f"Size: {(self.size.x, self.size.y) = }")

    def get_text(self):
        return self.raw_text

    def set_text(self, text: str):
        self.raw_text = text
        self.text = self.font.render(f'{text}', True, self.color_manager.white)

    def set_size(self, new_size: pygame.math.Vector2):
        self.size = new_size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def update_position(self):
        if None != self.container:
            self.position = self.container.get_position() + self.relative_position
            self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def set_position(self, new_position: pygame.math.Vector2):
        self.relative_position = new_position
        self.update_position()
    
    def set_absolute_position(self, new_position: pygame.math.Vector2):
        self.position.update(new_position)
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)        
        
    def set_invisible(self):
        self.is_visible = False

    def set_visible(self):
        self.is_visible = True

    def set_disable(self):
        self.is_enabled = False
    
    def set_enable(self):
        self.is_enabled = True

    def check_if_visible(self):
        return self.is_visible
    
    def check_if_enabled(self):
        return self.is_enabled
