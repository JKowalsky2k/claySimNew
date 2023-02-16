import pygame
import copy
import json

import color

class Clay(pygame.sprite.Sprite):
    def __init__(self, window, offset, radius) -> None:
        pygame.sprite.Sprite.__init__(self)
        with open('settings/simulation_settings.json') as simulation_settings_file:
            self.simulation_settings = json.load(simulation_settings_file)

        self.window = window
        self.radius = radius
        self.offset = offset
        self.color_manager = color.Color()
        # self.reference_sprite = pygame.image.load("clay.png").convert_alpha()
        # self.sprite = copy.copy(self.reference_sprite)
        self.set_position(pygame.math.Vector2(0, 0))
        # self.update()

    def update(self):
        self.sprite = pygame.transform.scale(self.reference_sprite, pygame.math.Vector2(2*self.radius, 2*self.radius))

    def set_position(self, new_position):
        self.position = new_position + self.offset
        # self.update()

    def set_offset(self, new_offset):
        self.offset.update(new_offset)

    def get_radius(self):
        return self.radius

    def increase_radius(self):
        if self.radius < self.simulation_settings["size"]["max"]:
            self.radius += self.simulation_settings["size"]["step"]
        else:
            self.radius = self.simulation_settings["size"]["min"]
    
    def decrease_radius(self):
        if self.radius > self.simulation_settings["size"]["min"]:
            self.radius -= self.simulation_settings["size"]["step"]
        else:
            self.radius = self.simulation_settings["size"]["max"]

    def draw(self):
        # pygame.Surface.blit(self.window, self.sprite, self.position)
        pygame.draw.circle(self.window, self.color_manager.orange, self.position, self.radius)
    
