import pygame
import color

class Button():
    def __init__(self, window, position=pygame.math.Vector2(0, 0), size=pygame.math.Vector2(100, 40), text="") -> None:
        self.color_manager = color.Color()
        self.foreground_color = self.color_manager.button_fg
        self.background_color = self.color_manager.button_bg
        self.color = self.foreground_color
        self.window = window
        self.font = pygame.font.SysFont(None, 20)
        self.text = self.font.render(f'{text}', True, self.color_manager.white)

        self.position = position
        self.size = size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
        self.status = True

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

    def set_text(self, text: str):
        self.text = self.font.render(f'{text}', True, self.color_manager.white)

    def set_size(self, new_size: pygame.math.Vector2):
        self.size = new_size
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

    def set_postion(self, new_position: pygame.math.Vector2):
        self.position = new_position
        self.rect = pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)

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