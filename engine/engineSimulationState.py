import pygame
import json

import engine.engineDefaultState as engineDefaultState
import custom_gui.container as container
import custom_gui.button as button
import custom_gui.label as label
import clay
import mode

class SimulationStateController(engineDefaultState.DefaultState):
    def __init__(self, window, start_point1, start_point2, end_point1, end_point2, trajectory1, trajectory2, background) -> None:
        super().__init__(window, start_point1, start_point2, end_point1, end_point2, trajectory1, trajectory2, background)
        with open('settings/default_settings.json') as default_settings_file:
            self.default_settings = json.load(default_settings_file)
        with open('settings/simulation_settings.json') as simulation_settings_file:
            self.simulation_settings = json.load(simulation_settings_file)
            
        self.local_window_width, self.local_widow_height = pygame.display.get_surface().get_size()
        self.clay1 = clay.Clay(self.window, self.start_point1.get_position(), self.simulation_settings["size"]["default"])
        self.clay2 = clay.Clay(self.window, self.start_point2.get_position(), self.simulation_settings["size"]["default"])
        self.current_index1,  self.current_index2 = 0, 0
        self.simulation_speed1, self.simulation_speed2 = self.simulation_settings["speed"]["default"], self.simulation_settings["speed"]["default"]
        self.setup()
        self.create_gui()

    def setup(self):
        self.mode_controller = mode.Mode(self.start_point2.is_added())
    
    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.label_mode_name.disable()
                    self.button_mode.disable()
                    self.mode_controller.run()                        
            if self.button_speed_increase1.is_clicked(event=event.type):
                self.simulation_speed1 = self.increase_speed(self.simulation_speed1)
                self.label_speed_value1.set_text(f'{self.simulation_speed1}')
            if self.button_speed_decrease1.is_clicked(event=event.type):
                self.simulation_speed1 = self.decrease_speed(self.simulation_speed1)
                self.label_speed_value1.set_text(f'{self.simulation_speed1}')
            if self.button_size_increase1.is_clicked(event=event.type):
                self.clay1.increase_radius()
                self.label_size_value1.set_text(f'{self.clay1.get_radius()}')
            if self.button_size_decrease1.is_clicked(event=event.type):
                self.clay1.decrease_radius()
                self.label_size_value1.set_text(f'{self.clay1.get_radius()}')
            if True == self.start_point2.is_added():
                if self.button_speed_increase2.is_clicked(event=event.type):
                    self.simulation_speed2 = self.increase_speed(self.simulation_speed2)
                    self.label_speed_value2.set_text(f'{self.simulation_speed2}')
                if self.button_speed_decrease2.is_clicked(event=event.type):
                    self.simulation_speed2 = self.decrease_speed(self.simulation_speed2)
                    self.label_speed_value2.set_text(f'{self.simulation_speed2}')
                if self.button_size_increase2.is_clicked(event=event.type):
                    self.clay2.increase_radius()
                    self.label_size_value2.set_text(f'{self.clay2.get_radius()}')
                if self.button_size_decrease2.is_clicked(event=event.type):
                    self.clay2.decrease_radius()
                    self.label_size_value2.set_text(f'{self.clay2.get_radius()}')
            if self.button_trajectory_visibility.is_clicked(event=event.type):
                if True == self.trajectory1.is_visible():
                    self.trajectory1.invisible()
                    self.trajectory2.invisible()
                    self.button_trajectory_visibility.set_text("Enable")
                else:
                    self.trajectory1.visible()
                    self.trajectory2.visible()
                    self.button_trajectory_visibility.set_text("Disable")
            if self.button_mode.is_clicked(event=event.type):
                self.mode_controller.change_mode()
                self.button_mode.set_text(f"{self.mode_controller.get_mode()}")
            if self.button_background_next.is_clicked(event=event.type):
                self.background.next()
                self.label_background_value.set_text(f"{self.background.get_id()}")
            if self.button_background_previous.is_clicked(event=event.type):
                self.background.previous()
                self.label_background_value.set_text(f"{self.background.get_id()}")
            if self.button_start.is_clicked(event=event.type):
                return True
    
    def draw(self):
        self.window.fill(self.color.black)
        self.background.draw()

        self.trajectory1.draw()
        self.start_point1.draw()
        self.end_point1.draw()
        self.clay1.draw()

        if True == self.start_point2.is_added():
            self.trajectory2.draw()
            self.start_point2.draw()
            self.end_point2.draw()
            self.clay2.draw()

        if True == self.container.check_update():
            for control in self.controls:
                control.update_position()
            self.container.update_finished()
        for control in self.controls:
            control.draw()

        pygame.display.flip()

    def update(self, delta_time):
        if pygame.display.get_surface().get_size()[0] >= self.default_settings["window"]["width"] and pygame.display.get_surface().get_size()[1] >= self.default_settings["window"]["height"]:
            self.local_window_width, self.local_widow_height = pygame.display.get_surface().get_size()
        else:
            self.local_window_width, self.local_widow_height = self.default_settings["window"]["width"], self.default_settings["window"]["height"]
            self.window = pygame.display.set_mode(size=(self.local_window_width, self.local_widow_height), flags=pygame.RESIZABLE)
        self.container.set_position(pygame.math.Vector2(self.local_window_width/2-self.default_settings["hud_simulation"]["width"]/2, self.local_widow_height-self.default_settings["hud_simulation"]["height"]))

        if False == self.start_point2.is_added():
            self.label_speed_name2.disable()
            self.label_speed_value2.disable()
            self.button_speed_increase2.disable()
            self.button_speed_decrease2.disable()
            self.label_size_name2.disable()
            self.label_size_value2.disable()
            self.button_size_increase2.disable()
            self.button_size_decrease2.disable()
        else:
            self.label_speed_name2.enable()
            self.label_speed_value2.enable()
            self.button_speed_increase2.enable()
            self.button_speed_decrease2.enable()
            self.label_size_name2.enable()
            self.label_size_value2.enable()
            self.button_size_increase2.enable()
            self.button_size_decrease2.enable()

        if True == self.mode_controller.is_first_running():
            if delta_time < 1:
                self.current_index1 += self.simulation_speed1
            else:
                self.current_index1 += self.simulation_speed1*delta_time
            if self.current_index1 > self.trajectory1.get_last_index():
                self.current_index1 = 0
                self.mode_controller.stop_first()
            self.clay1.set_position(self.trajectory1.get_point(self.current_index1))

        if True == self.mode_controller.is_second_running():
            if delta_time < 1:
                self.current_index2 += self.simulation_speed2
            else:
                self.current_index2 += self.simulation_speed2*delta_time
            if self.current_index2 > self.trajectory2.get_last_index():
                self.current_index2 = 0
                self.mode_controller.stop_second()
            self.clay2.set_position(self.trajectory2.get_point(self.current_index2))
        
        if  False == self.mode_controller.is_first_running() and \
            False == self.mode_controller.is_second_running():
            self.label_mode_name.enable()
            self.button_mode.enable()

    def create_gui(self):
        self.controls = []

        self.container = container.Container(pygame.math.Vector2(self.local_window_width/2-self.default_settings["hud_simulation"]["width"]/2, self.local_widow_height-self.default_settings["hud_simulation"]["height"]))

        self.label_speed_name1 = label.Label(self.window, position=pygame.math.Vector2(0, 5), text="Speed", color="blue", font_size=18, container=self.container)
        self.controls.append(self.label_speed_name1)
        self.label_speed_value1 = label.Label(self.window, position=pygame.math.Vector2(0, 55), text=f"{self.simulation_speed1}", color="blue", font_size=18, container=self.container)
        self.controls.append(self.label_speed_value1)
        self.button_speed_increase1 = button.Button(self.window, position=pygame.math.Vector2(0, 105), size=pygame.math.Vector2(45, 30), text="+", container=self.container)
        self.controls.append(self.button_speed_increase1)
        self.button_speed_decrease1 = button.Button(self.window, position=pygame.math.Vector2(55, 105), size=pygame.math.Vector2(45, 30), text="-", container=self.container)
        self.controls.append(self.button_speed_decrease1)

        self.label_size_name1 = label.Label(self.window, position=pygame.math.Vector2(110, 5), text="Size", color="blue", font_size=18, container=self.container)
        self.controls.append(self.label_size_name1)
        self.label_size_value1 = label.Label(self.window, position=pygame.math.Vector2(110, 55), text=f"{self.clay1.get_radius()}", color="blue", font_size=18, container=self.container)
        self.controls.append(self.label_size_value1)
        self.button_size_increase1 = button.Button(self.window, position=pygame.math.Vector2(110, 105), size=pygame.math.Vector2(45, 30), text="+", container=self.container)
        self.controls.append(self.button_size_increase1)
        self.button_size_decrease1 = button.Button(self.window, position=pygame.math.Vector2(165, 105), size=pygame.math.Vector2(45, 30), text="-", container=self.container)
        self.controls.append(self.button_size_decrease1)

        self.label_speed_name2 = label.Label(self.window, position=pygame.math.Vector2(220, 5), text="Speed", color="yellow", font_size=18, container=self.container)
        self.controls.append(self.label_speed_name2)
        self.label_speed_value2 = label.Label(self.window, position=pygame.math.Vector2(220, 55), text=f"{self.simulation_speed2}", color="yellow", font_size=18, container=self.container)
        self.controls.append(self.label_speed_value2)
        self.button_speed_increase2 = button.Button(self.window, position=pygame.math.Vector2(220, 105), size=pygame.math.Vector2(45, 30), text="+", color="yellow", container=self.container)
        self.controls.append(self.button_speed_increase2)
        self.button_speed_decrease2 = button.Button(self.window, position=pygame.math.Vector2(275, 105), size=pygame.math.Vector2(45, 30), text="-", color="yellow", container=self.container)
        self.controls.append(self.button_speed_decrease2)

        self.label_size_name2 = label.Label(self.window, position=pygame.math.Vector2(330, 5), text="Size", color="yellow", font_size=18, container=self.container)
        self.controls.append(self.label_size_name2)
        self.label_size_value2 = label.Label(self.window, position=pygame.math.Vector2(330, 55), text=f"{self.clay1.get_radius()}", color="yellow", font_size=18, container=self.container)
        self.controls.append(self.label_size_value2)
        self.button_size_increase2 = button.Button(self.window, position=pygame.math.Vector2(330, 105), size=pygame.math.Vector2(45, 30), text="+", color="yellow", container=self.container)
        self.controls.append(self.button_size_increase2)
        self.button_size_decrease2 = button.Button(self.window, position=pygame.math.Vector2(385, 105), size=pygame.math.Vector2(45, 30), text="-", color="yellow", container=self.container)
        self.controls.append(self.button_size_decrease2)

        self.label_trajectory_name = label.Label(self.window, position=pygame.math.Vector2(440, 5), text="Trajectory", color="green", font_size=18, container=self.container)
        self.controls.append(self.label_trajectory_name)
        self.button_trajectory_visibility = button.Button(self.window, position=pygame.math.Vector2(440, 55), size=pygame.math.Vector2(100, 80), text="Disable", color="green", container=self.container)
        self.controls.append(self.button_trajectory_visibility)
        self.label_mode_name = label.Label(self.window, position=pygame.math.Vector2(550, 5), text="Mode", color="green", font_size=18, container=self.container)
        self.controls.append(self.label_mode_name)
        self.button_mode = button.Button(self.window, position=pygame.math.Vector2(550, 55), size=pygame.math.Vector2(100, 80), text=f"{self.mode_controller.get_mode()}", color="green", container=self.container)
        self.controls.append(self.button_mode)

        self.label_background_name = label.Label(self.window, position=pygame.math.Vector2(660, 5), text="Background", color="green", font_size=18, container=self.container)
        self.controls.append(self.label_background_name)
        self.label_background_value = label.Label(self.window, position=pygame.math.Vector2(660, 55), text=f"{self.background.get_id()}", color="green", font_size=18, container=self.container)
        self.controls.append(self.label_background_value)
        self.button_background_previous = button.Button(self.window, position=pygame.math.Vector2(660, 105), size=pygame.math.Vector2(45, 30), text="<", color="green", container=self.container)
        self.controls.append(self.button_background_previous)
        self.button_background_next = button.Button(self.window, position=pygame.math.Vector2(715, 105), size=pygame.math.Vector2(45, 30), text=">", color="green", container=self.container)
        self.controls.append(self.button_background_next)

        self.button_start = button.Button(self.window, position=pygame.math.Vector2(770, 5), size=pygame.math.Vector2(100, 130), text="Back", color="purple", font_size=30, container=self.container)
        self.controls.append(self.button_start)

    def check_is_resolution_changed(self):
        return (self.local_window_width, self.local_widow_height) != pygame.display.get_surface().get_size()

    def setup_clay_position(self):
        self.clay1.set_offset(self.start_point1.get_position())
        self.clay1.set_position(pygame.math.Vector2(0, 0))
        self.clay2.set_offset(self.start_point2.get_position())
        self.clay2.set_position(pygame.math.Vector2(0, 0))
    
    def increase_speed(self, speed):
        if speed < self.simulation_settings["speed"]["max"]:
            speed += self.simulation_settings["speed"]["step"]
        else:
            speed = self.simulation_settings["speed"]["min"]
        return speed
    
    def decrease_speed(self, speed):
        if speed > self.simulation_settings["speed"]["min"]:
            speed -= self.simulation_settings["speed"]["step"]
        else:
            speed = self.simulation_settings["speed"]["max"]
        return speed
