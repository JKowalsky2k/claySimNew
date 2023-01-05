import engineStateMachine

class Engine():
    def __init__(self) -> None:
        self.state_machine = engineStateMachine.StateMachineController()

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
        t = 1e6
        while True == self.state_machine.is_config:
            self.state_machine.goto_simulation()

    def state_simulation(self) -> None:
        while True == self.state_machine.is_simulation:
            exit()