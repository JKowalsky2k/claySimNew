import pygame

import engineDefaultState
import custom_gui.container as container
import custom_gui.button as button
import custom_gui.label as label

class ConfigStateController(engineDefaultState.DefaultState):
    def __init__(self, window) -> None:
        super().__init__(window)
        self.container = container.Container(pygame.math.Vector2(10, 460))
        self.create_gui()

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            for button in self.buttons:
                if button.is_clicked(event=event.type):
                    print(f'{button = }')

    def draw(self):
        self.window.fill(self.color.black)
        if True == self.container.check_update():
            for control in self.controls:
                control.update_position()
            self.container.update_finished()
        for control in self.controls:
            control.draw()
        pygame.display.flip()

    def update(self):
        pass

    def create_gui(self):
        self.label_velocity_name = label.Label(self.window, position=pygame.math.Vector2(0, 0), text="Predkosc", font_size=18, container=self.container)
        self.label_velocity_value = label.Label(self.window, position=pygame.math.Vector2(0, 50), text="10", container=self.container)
        self.button_velocity_increase = button.Button(self.window, position=pygame.math.Vector2(0, 100), size=pygame.math.Vector2(45, 30), text="+", container=self.container)
        self.button_velocity_decrease = button.Button(self.window, position=pygame.math.Vector2(55, 100), size=pygame.math.Vector2(45, 30), text="-", container=self.container)

        self.labels = [self.label_velocity_name, self.label_velocity_value]
        self.buttons = [self.button_velocity_increase, self.button_velocity_decrease]
        self.controls = [*self.labels, *self.buttons]
