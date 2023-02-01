import pygame
import json

import engineStateMachine
import engineConfigState
import color
import house
import trajectory

class Engine():
    def __init__(self) -> None:
        pygame.init()

        with open('default_settings.json') as default_settings_file:
            self.settings = json.load(default_settings_file)

        self.window = pygame.display.set_mode(size=(self.settings["window"]["width"], self.settings["window"]["height"]), flags=pygame.RESIZABLE)
        pygame.display.set_caption(f'{self.settings["window"]["title"]}')

        self.start_point1 = house.House(self.window, position=pygame.math.Vector2(tuple(map(lambda dimension: dimension//2, pygame.display.get_surface().get_size()))), color=color.Color().blue_button_fg)
        self.start_point2 = house.House(self.window, position=pygame.math.Vector2(tuple(map(lambda dimension: dimension//2, pygame.display.get_surface().get_size()))), color=color.Color().yellow_button_fg)

        self.trajectory1 = trajectory.Trajectory(self.window)
        self.trajectory1.set_offset(self.start_point1.get_position())
        self.trajectory2 = trajectory.Trajectory(self.window)
        self.trajectory2.set_offset(self.start_point2.get_position())

        self.state_machine = engineStateMachine.StateMachineController()
        self.config = engineConfigState.ConfigStateController(window=self.window, start_point1=self.start_point1, start_point2=self.start_point2, trajectory1=self.trajectory1, trajectory2=self.trajectory2)

    def __str__(self) -> str:
        return f'Engine({self.state_machine.current_state.name = })'

    def run(self) -> None:
        self.state_machine_manager()

    def state_machine_manager(self) -> None:
        while True:
            print(self.state_machine.current_state.name)
            if True == self.state_machine.is_config:
                self.state_config()
            elif True == self.state_machine.is_simulation:
                self.state_simulation()

    def state_config(self) -> None:
        clock = pygame.time.Clock()
        while True == self.state_machine.is_config:
            self.config.display_fps_in_caption(clock=clock)
            if self.config.event_manager():
                self.state_machine.goto_simulation()
            self.config.update()
            self.config.draw()
            clock.tick()

    def state_simulation(self) -> None:
        clock = pygame.time.Clock()
        while True == self.state_machine.is_simulation:
            self.config.display_fps_in_caption(clock=clock)
            self.state_machine.goto_config()
            clock.tick()