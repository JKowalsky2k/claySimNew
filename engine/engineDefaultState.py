import pygame
import color

class DefaultState():
    def __init__(self, window, start_point1, start_point2, end_point1, end_point2, trajectory1, trajectory2, background) -> None:
        self.color = color.Color()
        self.window = window
        self.start_point1 = start_point1
        self.start_point2 = start_point2
        self.end_point1 = end_point1
        self.end_point2 = end_point2
        self.trajectory1 = trajectory1
        self.trajectory2 = trajectory2
        self.background = background

    def update(self):
        print("update")

    def draw(self):
        print("draw")

    def event_manager(self):
        print("event_manager")

    def display_fps_in_caption(self, clock):
        pygame.display.set_caption(f'{round(clock.get_fps(), 2)}')