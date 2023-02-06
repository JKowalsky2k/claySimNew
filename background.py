import pygame
import glob
import json

import color

class Background:
    def __init__(self, window) -> None:
        with open('settings/default_settings.json') as default_settings_file:
            self.default_settings = json.load(default_settings_file)

        self.window = window
        default_background = pygame.Surface((2000, 2000))
        default_background.fill(color.Color().black)
        self.backgorunds = [default_background]
        self.backgorunds.extend([pygame.image.load(path) for path in glob.glob('backgrounds/*')])
        self.index = 0

    def get_id(self):
        return self.index+1

    def next(self):
        if self.index < len(self.backgorunds)-1:
            self.index += 1
        else:
            self.index = 0

    def previous(self):
        if self.index > 0:
            self.index -= 1
        else:
            self.index = len(self.backgorunds)-1
    
    def draw(self):
        self.window.blit(pygame.transform.scale(self.backgorunds[self.index], (pygame.display.get_surface().get_size()[0], pygame.display.get_surface().get_size()[1]-self.default_settings["hud_config"]["height"])), (0, 0))