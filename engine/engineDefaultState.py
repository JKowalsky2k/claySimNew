import pygame
import color

class DefaultState():
    def __init__(self, window, start_point1, start_point2, end_point1, end_point2, trajectory1, trajectory2, background, button_hide_hud) -> None:
        self.color = color.Color()
        self.window = window
        self.start_point1 = start_point1
        self.start_point2 = start_point2
        self.end_point1 = end_point1
        self.end_point2 = end_point2
        self.trajectory1 = trajectory1
        self.trajectory2 = trajectory2
        self.background = background
        self.button_hide_hud = button_hide_hud
        self.controls = list()

    def update(self):
        print("update")

    def draw(self):
        print("draw")

    def event_manager(self):
        print("event_manager")

    def hide_controls(self):
        for control in self.controls:
            control.set_invisible()
        self.container.set_invisible()

    def show_controls(self):
        for control in self.controls:
            control.set_visible()
        self.container.set_visible()

    def display_fps_in_caption(self, clock):
        pygame.display.set_caption(f'{round(clock.get_fps(), 2)}')