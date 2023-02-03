import pygame
import json

import engineDefaultState
import custom_gui.container as container
import custom_gui.button as button
import custom_gui.label as label

class ConfigStateController(engineDefaultState.DefaultState):
    def __init__(self, window, start_point1, start_point2, trajectory1, trajectory2) -> None:
        super().__init__(window, start_point1, start_point2, trajectory1, trajectory2)
        with open('default_settings.json') as default_settings_file:
            self.default_settings = json.load(default_settings_file)
        self.local_window_width, self.local_widow_height = pygame.display.get_surface().get_size()
        self.trajectory1.calculate()
        self.trajectory1.set_offset(self.start_point1.get_position())
        self.trajectory2.calculate()
        self.trajectory2.set_offset(self.start_point2.get_position())     
        self.create_gui()

    def event_manager(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if self.button_velocity_increase1.is_clicked(event=event.type):
                self.trajectory1.increase_initial_velocity()
                self.label_velocity_value1.set_text(self.trajectory1.get_initial_velocity())
                self.trajectory1.calculate()
            if self.button_velocity_decrease1.is_clicked(event=event.type):
                self.trajectory1.decrease_initial_velocity()
                self.label_velocity_value1.set_text(self.trajectory1.get_initial_velocity())
                self.trajectory1.calculate()
            if self.button_angle_increase1.is_clicked(event=event.type):
                self.trajectory1.increase_angle()
                self.label_angle_value1.set_text(self.trajectory1.get_angle())
                self.trajectory1.calculate()
            if self.button_angle_decrease1.is_clicked(event=event.type):
                self.trajectory1.decrease_angle()
                self.label_angle_value1.set_text(self.trajectory1.get_angle())
                self.trajectory1.calculate()
            if self.button_velocity_increase2.is_clicked(event=event.type):
                self.trajectory2.increase_initial_velocity()
                self.label_velocity_value2.set_text(self.trajectory2.get_initial_velocity())
                self.trajectory2.calculate()
            if self.button_velocity_decrease2.is_clicked(event=event.type):
                self.trajectory2.decrease_initial_velocity()
                self.label_velocity_value2.set_text(self.trajectory2.get_initial_velocity())
                self.trajectory2.calculate()
            if self.button_angle_increase2.is_clicked(event=event.type):
                self.trajectory2.increase_angle()
                self.label_angle_value2.set_text(self.trajectory2.get_angle())
                self.trajectory2.calculate()
            if self.button_angle_decrease2.is_clicked(event=event.type):
                self.trajectory2.decrease_angle()
                self.label_angle_value2.set_text(self.trajectory2.get_angle())
                self.trajectory2.calculate()

            if self.button_add_second_house.is_clicked(event=event.type):
                self.button_add_second_house.invisible()
                self.button_velocity_increase2.enable()
                self.button_velocity_decrease2.enable()
                self.button_angle_increase2.enable()
                self.button_angle_decrease2.enable()
                self.button_remove_second_house.enable()
                self.button_add_second_house.disable()
            elif self.button_remove_second_house.is_clicked(event=event.type):
                self.button_add_second_house.visible()
                self.button_velocity_increase2.disable()
                self.button_velocity_decrease2.disable()
                self.button_angle_increase2.disable()
                self.button_angle_decrease2.disable()
                self.button_remove_second_house.disable()
                self.button_add_second_house.enable()

            if self.button_background_next.is_clicked(event=event.type):
                print("Background Next")
            if self.button_background_previous.is_clicked(event=event.type):
                print("Background Previous")
            if self.button_start.is_clicked(event=event.type):
                return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 1 == event.button:
                    if True == self.start_point1.get_rect().collidepoint(pygame.mouse.get_pos()):
                        self.start_point1.set_movable(state=True)
                    elif True == self.start_point2.get_rect().collidepoint(pygame.mouse.get_pos()):
                        self.start_point2.set_movable(state=True)
            elif event.type == pygame.MOUSEBUTTONUP:
                if 1 == event.button:
                    self.start_point1.set_movable(state=False)
                    self.start_point2.set_movable(state=False)
            elif event.type == pygame.MOUSEMOTION:
                if True == self.start_point1.is_movable():
                    self.update_object_position(self.start_point1)
                    self.trajectory1.set_offset(self.start_point1.get_position())
                elif True == self.start_point2.is_movable():
                    self.update_object_position(self.start_point2)
                    self.trajectory2.set_offset(self.start_point2.get_position())         

    def draw(self):
        self.window.fill(self.color.black)
        if True == self.container.check_update():
            for control in self.controls:
                control.update_position()
            self.container.update_finished()
        for control in self.controls:
            control.draw()
        
        self.trajectory1.draw()
        self.start_point1.draw()
        if False == self.button_add_second_house.is_visible():
            self.trajectory2.draw()
            self.start_point2.draw()

        pygame.display.flip()

    def update(self):
        if True == self.check_is_resolution_changed():
            if pygame.display.get_surface().get_size()[0] >= self.default_settings["window"]["width"] and pygame.display.get_surface().get_size()[1] >= self.default_settings["window"]["height"]:
                self.local_window_width, self.local_widow_height = pygame.display.get_surface().get_size()
                self.trajectory1.calculate()
            else:
                self.local_window_width, self.local_widow_height = self.default_settings["window"]["width"], self.default_settings["window"]["height"]
                self.window = pygame.display.set_mode(size=(self.local_window_width, self.local_widow_height), flags=pygame.RESIZABLE)
            self.container.set_position(pygame.math.Vector2(self.local_window_width/2-self.default_settings["hud"]["width"]/2, self.local_widow_height-self.default_settings["hud"]["height"]))

    def create_gui(self):
        self.controls = []
        self.controls = []

        self.container = container.Container(pygame.math.Vector2(self.local_window_width/2-self.default_settings["hud"]["width"]/2, self.local_widow_height-self.default_settings["hud"]["height"]))

        self.label_velocity_name1 = label.Label(self.window, position=pygame.math.Vector2(0, 0), text="Velocity", font_size=18, container=self.container)
        self.controls.append(self.label_velocity_name1)
        self.label_velocity_value1 = label.Label(self.window, position=pygame.math.Vector2(0, 50), text="40", container=self.container)
        self.controls.append(self.label_velocity_value1)
        self.button_velocity_increase1 = button.Button(self.window, position=pygame.math.Vector2(0, 100), size=pygame.math.Vector2(45, 30), text="+", container=self.container)
        self.controls.append(self.button_velocity_increase1)
        self.button_velocity_decrease1 = button.Button(self.window, position=pygame.math.Vector2(55, 100), size=pygame.math.Vector2(45, 30), text="-", container=self.container)
        self.controls.append(self.button_velocity_decrease1)

        self.label_angle_name1 = label.Label(self.window, position=pygame.math.Vector2(110, 0), text="Angle (deg)", font_size=18, container=self.container)
        self.controls.append(self.label_angle_name1)
        self.label_angle_value1 = label.Label(self.window, position=pygame.math.Vector2(110, 50), text="45", font_size=18, container=self.container)
        self.controls.append(self.label_angle_value1)
        self.button_angle_increase1 = button.Button(self.window, position=pygame.math.Vector2(110, 100), size=pygame.math.Vector2(45, 30), text="+", container=self.container)
        self.controls.append(self.button_angle_increase1)
        self.button_angle_decrease1 = button.Button(self.window, position=pygame.math.Vector2(165, 100), size=pygame.math.Vector2(45, 30), text="-", container=self.container)
        self.controls.append(self.button_angle_decrease1)


        self.label_velocity_name2 = label.Label(self.window, position=pygame.math.Vector2(220, 0), text="Velocity", color="yellow", font_size=18, container=self.container)
        self.controls.append(self.label_velocity_name2)
        self.label_velocity_value2 = label.Label(self.window, position=pygame.math.Vector2(220, 50), text="40", color="yellow", container=self.container)
        self.controls.append(self.label_velocity_value2)
        self.button_velocity_increase2 = button.Button(self.window, position=pygame.math.Vector2(220, 100), size=pygame.math.Vector2(45, 30), text="+", color="yellow", container=self.container)
        self.button_velocity_increase2.disable()
        self.controls.append(self.button_velocity_increase2)
        self.button_velocity_decrease2 = button.Button(self.window, position=pygame.math.Vector2(275, 100), size=pygame.math.Vector2(45, 30), text="-", color="yellow", container=self.container)
        self.button_velocity_decrease2.disable()
        self.controls.append(self.button_velocity_decrease2)

        self.label_angle_name2 = label.Label(self.window, position=pygame.math.Vector2(330, 0), text="Angle (deg)", color="yellow", font_size=18, container=self.container)
        self.controls.append(self.label_angle_name2)
        self.label_angle_value2 = label.Label(self.window, position=pygame.math.Vector2(330, 50), text="45", color="yellow", font_size=18, container=self.container)
        self.controls.append(self.label_angle_value2)
        self.button_angle_increase2 = button.Button(self.window, position=pygame.math.Vector2(330, 100), size=pygame.math.Vector2(45, 30), text="+", color="yellow", container=self.container)
        self.button_angle_increase2.disable()
        self.controls.append(self.button_angle_increase2)
        self.button_angle_decrease2 = button.Button(self.window, position=pygame.math.Vector2(385, 100), size=pygame.math.Vector2(45, 30), text="-", color="yellow", container=self.container)
        self.button_angle_decrease2.disable()
        self.controls.append(self.button_angle_decrease2)

        self.label_background_name = label.Label(self.window, position=pygame.math.Vector2(495, 0), text="Background", color="green", font_size=18, container=self.container)
        self.controls.append(self.label_background_name)
        self.label_background_value = label.Label(self.window, position=pygame.math.Vector2(495, 50), text="0", color="green", font_size=18, container=self.container)
        self.controls.append(self.label_background_value)
        self.button_background_previous = button.Button(self.window, position=pygame.math.Vector2(495, 100), size=pygame.math.Vector2(45, 30), text="<", color="green", container=self.container)
        self.controls.append(self.button_background_previous)
        self.button_background_next = button.Button(self.window, position=pygame.math.Vector2(550, 100), size=pygame.math.Vector2(45, 30), text=">", color="green", container=self.container)
        self.controls.append(self.button_background_next)

        self.button_start = button.Button(self.window, position=pygame.math.Vector2(605, 0), size=pygame.math.Vector2(100, 130), text="Start", color="purple", font_size=30, container=self.container)
        self.controls.append(self.button_start)

        self.button_remove_second_house = button.Button(self.window, position=pygame.math.Vector2(440, 0), size=pygame.math.Vector2(45, 130), text="X", color="red", font_size=30, container=self.container)
        self.button_remove_second_house.disable()
        self.controls.append(self.button_remove_second_house)
        self.button_add_second_house = button.Button(self.window, position=pygame.math.Vector2(220, 0), size=pygame.math.Vector2(265, 130), text="Add", color="yellow", font_size=50, container=self.container)
        self.controls.append(self.button_add_second_house)

    def check_is_resolution_changed(self):
        return (self.local_window_width, self.local_widow_height) != pygame.display.get_surface().get_size()

    def update_object_position(self, object):
        if object.get_rect().width//2 > pygame.mouse.get_pos()[0]:
            object.set_position_x(new_x=object.get_rect().width//2)
        elif pygame.mouse.get_pos()[0] > self.local_window_width-object.get_rect().width//2:
            object.set_position_x(new_x=self.local_window_width-object.get_rect().width//2)
        else:
            object.set_position_x(new_x=pygame.mouse.get_pos()[0])
        if pygame.mouse.get_pos()[1] < object.get_rect().height//2:
            object.set_position_y(new_y=object.get_rect().height//2)
        elif pygame.mouse.get_pos()[1] > self.local_widow_height-self.default_settings["hud"]["height"]-object.get_rect().height//2:
            object.set_position_y(new_y=self.local_widow_height-self.default_settings["hud"]["height"]-object.get_rect().height//2)
        else:
            object.set_position_y(new_y= pygame.mouse.get_pos()[1])