import pygame
import color

class DefaultState():
    def __init__(self, window) -> None:
        self.color = color.Color()
        self.window = window

    def update(self):
        print("update")

    def draw(self):
        print("draw")

    def event_manager(self):
        print("event_manager")

    def display_fps_in_caption(self, clock):
        pygame.display.set_caption(f'{round(clock.get_fps(), 2)}')