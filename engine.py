import pygame

import engineStateMachine
import engineConfigState

class Engine():
    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.display.set_mode([500, 500])

        self.state_machine = engineStateMachine.StateMachineController()
        self.config = engineConfigState.ConfigStateController(window=self.window)

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
            self.config.event_manager()
            self.config.update()
            self.config.draw()
            clock.tick()

    def state_simulation(self) -> None:
        clock = pygame.time.Clock()
        while True == self.state_machine.is_simulation:
            self.config.display_fps_in_caption(clock=clock)
            exit(0)
            clock.tick()