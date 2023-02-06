import statemachine

class StateMachineController(statemachine.StateMachine):
    config = statemachine.State("CONFIG", initial=True)
    simulation = statemachine.State("SIMULATION")

    goto_simulation = config.to(simulation)
    goto_config = simulation.to(config)


