import pygame
import json

import engine.engineStateMachine as engineStateMachine
import engine.engineConfigState as engineConfigState
import engine.engineSimulationState as engineSimulationState

import custom_gui.button as button
import color
import house
import point
import trajectory
import background

class Engine():
    def __init__(self) -> None:
        pygame.init()
        with open('settings/default_settings.json') as default_settings_file:
            self.settings = json.load(default_settings_file)

        self.window = pygame.display.set_mode(size=(self.settings["window"]["width"], self.settings["window"]["height"]), flags=pygame.RESIZABLE)
        pygame.display.set_caption(f'{self.settings["window"]["title"]}')

        self.start_point1 = house.House(self.window, position=pygame.math.Vector2(tuple(map(lambda dimension: dimension//2, pygame.display.get_surface().get_size()))), color=color.Color().blue_button_fg)
        self.start_point2 = house.House(self.window, position=pygame.math.Vector2(tuple(map(lambda dimension: dimension//2, pygame.display.get_surface().get_size()))), color=color.Color().yellow_button_fg)

        self.end_point1 = point.Point(self.window, position=pygame.math.Vector2(0, 0), radius=5, color=color.Color().blue)
        self.end_point1.set_offset(self.start_point1.get_position())
        self.end_point2 = point.Point(self.window, position=pygame.math.Vector2(0, 0), radius=5, color=color.Color().yellow)
        self.end_point2.set_offset(self.start_point2.get_position())

        self.trajectory1 = trajectory.Trajectory(self.window)
        self.trajectory1.set_offset(self.start_point1.get_position())
        self.trajectory2 = trajectory.Trajectory(self.window)
        self.trajectory2.set_offset(self.start_point2.get_position())

        self.background = background.Background(self.window)
        self.button_hide_hud = button.Button(self.window, position=pygame.math.Vector2(5, pygame.display.get_surface().get_size()[1]-30), size=pygame.math.Vector2(50, 25), text="Hide", font_size=18, color="purple")

        self.state_machine = engineStateMachine.StateMachineController()
        self.config = engineConfigState.ConfigStateController(window=self.window, start_point1=self.start_point1, start_point2=self.start_point2, end_point1=self.end_point1, end_point2=self.end_point2, trajectory1=self.trajectory1, trajectory2=self.trajectory2, background=self.background, button_hide_hud=self.button_hide_hud)
        self.simulation = engineSimulationState.SimulationStateController(window=self.window, start_point1=self.start_point1, start_point2=self.start_point2, end_point1=self.end_point1, end_point2=self.end_point2, trajectory1=self.trajectory1, trajectory2=self.trajectory2, background=self.background, button_hide_hud=self.button_hide_hud)

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
        self.trajectory1.calculate()
        self.trajectory2.calculate()
        self.trajectory1.set_visible()
        self.trajectory2.set_visible()
        while True == self.state_machine.is_config:
            self.config.display_fps_in_caption(clock=clock)
            if True == self.config.event_manager():
                self.state_machine.goto_simulation()
            self.config.update()
            self.config.draw()
            clock.tick()

    def state_simulation(self) -> None:
        clock = pygame.time.Clock()
        self.trajectory1.adjust(self.end_point1.get_position())
        self.trajectory2.adjust(self.end_point2.get_position())
        self.simulation.setup_clay_position()
        self.simulation.setup()
        while True == self.state_machine.is_simulation:
            self.config.display_fps_in_caption(clock=clock)
            if True == self.simulation.event_manager():
                self.state_machine.goto_config()
            self.simulation.update(clock.tick())
            self.simulation.draw()
            clock.tick()