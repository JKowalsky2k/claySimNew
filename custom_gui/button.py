import pygame
import custom_gui.container as container
import custom_gui.defaultElement as defaultElement

class Button(defaultElement.DefaultElement):

    def __init__(   self, window, 
                    position=pygame.math.Vector2(0, 0), 
                    size=pygame.math.Vector2(100, 40), 
                    text="",
                    font_size=20,
                    default_status=True,
                    color="blue",
                    container=container.Container(pygame.math.Vector2(0, 0))
                ) -> None:
        super().__init__(window, position, size, text, font_size, container)
        self.foreground_color, self.background_color = self.color_manager.get_button_color_theme(color)
        self.color = self.foreground_color
        self.is_enabled = default_status

    def is_clicked(self, event: pygame.event):
        return self.is_hover() and event == pygame.MOUSEBUTTONDOWN

    def is_hover(self):
        if True == self.visiblity:
            if True == self.is_enabled:
                mouse_posx, mouse_posy = pygame.mouse.get_pos()
                if  self.position.x < mouse_posx < self.position.x + self.size.x and \
                    self.position.y < mouse_posy < self.position.y + self.size.y:
                    self.color = self.background_color
                    return True
            self.color = self.foreground_color
        return False

    def disable(self):
        self.is_enabled = False
    
    def enable(self):
        self.is_enabled = True
    
    def draw(self):
        if True == self.visiblity:
            if True == self.is_enabled:
                pygame.draw.rect(surface=self.window, color=self.color, rect=self.rect, border_radius=5)
            else:
                pygame.draw.rect(surface=self.window, color=self.color_manager.buttin_disable, rect=self.rect, border_radius=5)
            self.window.blit(self.text, self.text.get_rect(center=self.rect.center))