import pygame
import json

import engineDefaultState
import custom_gui.container as container
import custom_gui.button as button
import custom_gui.label as label
import clay

class SimulationStateController(engineDefaultState.DefaultState):
    def __init__(self, window, start_point1, start_point2, end_point1, end_point2, trajectory1, trajectory2) -> None:
        super().__init__(window, start_point1, start_point2, end_point1, end_point2, trajectory1, trajectory2)
        with open('default_settings.json') as default_settings_file:
            self.default_settings = json.load(default_settings_file)
        self.local_window_width, self.local_widow_height = pygame.display.get_surface().get_size()
        self.clay = clay.Clay(self.window, self.start_point1.get_position(), 20)
        self.current_index = 0
        self.simulation_speed = 10
        self.create_gui()
    
    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if self.button_background_next.is_clicked(event=event.type):
                print("Background Next")
            if self.button_background_previous.is_clicked(event=event.type):
                print("Background Previous")
            if self.button_start.is_clicked(event=event.type):
                return True
    
    def draw(self):
        self.window.fill(self.color.black)

        self.trajectory1.draw()
        self.start_point1.draw()
        # self.end_point1.draw()
        self.clay.draw()

        if True == self.container.check_update():
            for control in self.controls:
                control.update_position()
            self.container.update_finished()
        for control in self.controls:
            control.draw()

        pygame.display.flip()

    def update(self, delta_time):
        print(f"{delta_time = }")
        if delta_time < 1:
            self.current_index += self.simulation_speed
        else:
            self.current_index += self.simulation_speed*delta_time
        if self.current_index > self.trajectory1.get_last_index():
            self.current_index = 0
        self.clay.set_position(self.trajectory1.get_point(self.current_index))


    def create_gui(self):
        self.controls = []

        self.container = container.Container(pygame.math.Vector2(self.local_window_width/2-self.default_settings["hud"]["width"]/2, self.local_widow_height-self.default_settings["hud"]["height"]))



        self.label_background_name = label.Label(self.window, position=pygame.math.Vector2(495, 0), text="Background", color="green", font_size=18, container=self.container)
        self.controls.append(self.label_background_name)
        self.label_background_value = label.Label(self.window, position=pygame.math.Vector2(495, 50), text="0", color="green", font_size=18, container=self.container)
        self.controls.append(self.label_background_value)
        self.button_background_previous = button.Button(self.window, position=pygame.math.Vector2(495, 100), size=pygame.math.Vector2(45, 30), text="<", color="green", container=self.container)
        self.controls.append(self.button_background_previous)
        self.button_background_next = button.Button(self.window, position=pygame.math.Vector2(550, 100), size=pygame.math.Vector2(45, 30), text=">", color="green", container=self.container)
        self.controls.append(self.button_background_next)

        self.button_start = button.Button(self.window, position=pygame.math.Vector2(605, 0), size=pygame.math.Vector2(100, 130), text="Back", color="purple", font_size=30, container=self.container)
        self.controls.append(self.button_start)

    def check_is_resolution_changed(self):
        return (self.local_window_width, self.local_widow_height) != pygame.display.get_surface().get_size()

    def setup_clay_position(self):
        self.clay.set_offset(self.start_point1.get_position())
        self.clay.set_position(pygame.math.Vector2(0, 0))
