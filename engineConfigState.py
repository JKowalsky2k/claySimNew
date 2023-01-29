import pygame
import engineDefaultState
import button

class ConfigStateController(engineDefaultState.DefaultState):
    def __init__(self, window) -> None:
        super().__init__(window)
        self.button = button.Button(window, text="cbe")

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

    def draw(self):
        self.window.fill(self.color.black)
        self.button.draw()
        pygame.display.flip()

    def update(self):
        self.button.is_hover()
