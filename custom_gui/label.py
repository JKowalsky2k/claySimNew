import pygame
import custom_gui.container as container
import custom_gui.defaultElement as defaultElement

class Label(defaultElement.DefaultElement):

    def __init__(   self, window, 
                    position=pygame.math.Vector2(0, 0), 
                    size=pygame.math.Vector2(100, 40), 
                    text="",
                    font_size=20,
                    background=False,
                    color="blue",
                    container=container.Container(pygame.math.Vector2(0, 0))
                ) -> None:
        super().__init__(window, position, size, text, font_size, container)
        self.foreground_color, _ = self.color_manager.get_button_color_theme(color)
        self.color = self.foreground_color
        self.background = background
    
    def draw(self):
        if False == self.background:
            pygame.draw.rect(surface=self.window, color=self.color, rect=self.rect, width=1, border_radius=5)
        else:
            pygame.draw.rect(surface=self.window, color=self.color, rect=self.rect, border_radius=5)
        self.window.blit(self.text, self.text.get_rect(center=self.rect.center))
