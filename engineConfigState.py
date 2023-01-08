import pygame
import engineDefaultState

class ConfigStateController(engineDefaultState.DefaultState):
    def __init__(self, window) -> None:
        super().__init__(window)

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

    def draw(self):
        self.window.fill(self.color.black)
        pygame.draw.circle(self.window, self.color.green, (250, 250), 75)
        pygame.display.flip()

    def update(self):
        pass
