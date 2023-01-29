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
                    container=container.Container(pygame.math.Vector2(0, 0))
                ) -> None:
        super().__init__(window, position, size, text, font_size, container)
        self.foreground_color = self.color_manager.button_fg
        self.background_color = self.color_manager.button_bg
        self.color = self.foreground_color
        self.status = default_status

    def is_clicked(self, event: pygame.event):
        return self.is_hover() and event == pygame.MOUSEBUTTONDOWN

    def is_hover(self):
        if True == self.status:
            mouse_posx, mouse_posy = pygame.mouse.get_pos()
            if  self.position.x < mouse_posx < self.position.x + self.size.x and \
                self.position.y < mouse_posy < self.position.y + self.size.y:
                self.color = self.background_color
                return True
        self.color = self.foreground_color
        return False

    def disable(self):
        self.status = False
    
    def enable(self):
        self.status = True
    
    def draw(self):
        if True == self.status:
            pygame.draw.rect(surface=self.window, color=self.color, rect=self.rect, border_radius=10)
        else:
            pygame.draw.rect(surface=self.window, color=self.color_manager.buttin_disable, rect=self.rect, border_radius=10)
        self.window.blit(self.text, self.text.get_rect(center=self.rect.center))