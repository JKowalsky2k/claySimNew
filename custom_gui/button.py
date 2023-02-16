import pygame
import custom_gui.container as container
import custom_gui.defaultElement as defaultElement

class Button(defaultElement.DefaultElement):

    def __init__(   self, window, 
                    position=pygame.math.Vector2(0, 0), 
                    size=pygame.math.Vector2(100, 40), 
                    text="",
                    font_size=20,
                    color="blue",
                    container=None
                ) -> None:
        super().__init__(window, position, size, text, font_size, container)
        self.foreground_color, self.background_color = self.color_manager.get_button_color_theme(color)
        self.color = self.foreground_color
        self.is_clicked = False

    def check_if_clicked(self, event: pygame.event):
        click_status = self.check_if_hovered() and event == pygame.MOUSEBUTTONDOWN
        if True == click_status:
            self.is_clicked =  (self.is_clicked + 1) % 2
        return click_status

    def check_if_hovered(self):
        if True == self.check_if_visible():
            if True == self.check_if_enabled():
                mouse_posx, mouse_posy = pygame.mouse.get_pos()
                if  self.position.x < mouse_posx < self.position.x + self.size.x and \
                    self.position.y < mouse_posy < self.position.y + self.size.y:
                    self.color = self.background_color
                    return True
            self.color = self.foreground_color
        return False
    
    def check_status(self):
        return self.is_clicked
    
    def draw(self):
        if True == self.check_if_visible():
            if True == self.check_if_enabled():
                pygame.draw.rect(surface=self.window, color=self.color, rect=self.rect, border_radius=5)
            else:
                pygame.draw.rect(surface=self.window, color=self.color_manager.disable, rect=self.rect, border_radius=5)
            self.window.blit(self.text, self.text.get_rect(center=self.rect.center))