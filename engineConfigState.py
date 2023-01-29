import pygame
import engineDefaultState
import button

class ConfigStateController(engineDefaultState.DefaultState):
    def __init__(self, window) -> None:
        super().__init__(window)
        self.button = button.Button(window, text="cbe")
        self.button.set_postion(pygame.math.Vector2(100, 100))

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if self.button.is_clicked(event=event.type):
                self.button.disable()

    def draw(self):
        self.window.fill(self.color.black)
        self.button.draw()
        pygame.display.flip()

    def update(self):
        pass
