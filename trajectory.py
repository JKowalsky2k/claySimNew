import pygame
import json
import numpy
import copy

import color

class Trajectory:
    def __init__(self, window) -> None:
        with open('settings/default_settings.json') as default_settings_file:
            self.default_settings = json.load(default_settings_file)
        with open('settings/trajectory_settings.json') as trajectory_settings_file:
            self.trajectory_settings = json.load(trajectory_settings_file)

        self.window = window
        self.color_manager = color.Color()
        self.data = []

        self.initial_velocity = 40
        self.angle = 45
        self.offset = pygame.math.Vector2(0, 0)
        self.delta_time = 1e-3
        self.gravity = 9.807
        self.visibility = True

    def set_offset(self, new_offset):
        self.offset.update(new_offset)
    
    def visible(self):
        self.visibility = True

    def invisible(self):
        self.visibility = False

    def is_visible(self):
        return self.visibility

    def increase_initial_velocity(self):
        if self.initial_velocity < self.trajectory_settings["velocity"]["max"]:
            self.initial_velocity += self.trajectory_settings["velocity"]["step"]

    def decrease_initial_velocity(self):
        if self.initial_velocity > self.trajectory_settings["velocity"]["min"]:
            self.initial_velocity -= self.trajectory_settings["velocity"]["step"]

    def get_initial_velocity(self):
        return self.initial_velocity

    def increase_angle(self):
        if self.angle < self.trajectory_settings["angle"]["max"]:
            self.angle += self.trajectory_settings["angle"]["step"]

    def decrease_angle(self):
        if self.angle > self.trajectory_settings["angle"]["min"]:
            self.angle -= self.trajectory_settings["angle"]["step"]

    def get_angle(self):
        return self.angle

    def get_nearest_point_to_mouse_cursor(self):
        new_position = min(list(filter(lambda point: not self.check_if_point_is_out_of_screen(point), copy.copy(self.data))), key=lambda point: numpy.sqrt((point[0]-pygame.mouse.get_pos()[0]+self.offset.x)**2+(point[1]-pygame.mouse.get_pos()[1]+self.offset.y)**2))
        return pygame.math.Vector2(new_position[0], new_position[1])
    
    def get_last_index(self):
        return len(self.data)-1
    
    def get_point(self, index):
        return self.data[index]

    def check_if_point_is_out_of_screen(self, point):
        cartesian_point = pygame.math.Vector2(point[0], point[1]) + self.offset
        return  cartesian_point.x > pygame.display.get_surface().get_size()[0] or \
                cartesian_point.x < 0 or \
                cartesian_point.y > pygame.display.get_surface().get_size()[1]-self.default_settings["hud_config"]["height"]

    def check_if_point_is_out_of_window(self, point):
        cartesian_point = pygame.math.Vector2(point[0], -point[1]) + self.offset
        return  cartesian_point.x > pygame.display.get_surface().get_size()[0] or \
                cartesian_point.x < 0 or \
                cartesian_point.y > 2*pygame.display.get_surface().get_size()[1]

    def adjust(self, end_point_position):
        end_point_index = [pygame.math.Vector2(point[0], point[1]) for point in self.data].index(end_point_position)
        self.data = self.data[:end_point_index+1]

    def calculate(self):
        velocity = self.initial_velocity
        velocity_x = numpy.cos(numpy.deg2rad(self.angle))*velocity
        velocity_y = numpy.sin(numpy.deg2rad(self.angle))*velocity

        idx = 0
        pos = numpy.zeros(shape=(100_000, 2))

        while True:
            ay = -self.gravity
            velocity_y += ay * self.delta_time
            velocity = numpy.sqrt(velocity_x**2 + velocity_y**2)
            pos[idx+1, 0] = pos[idx, 0] + velocity_x*self.delta_time
            pos[idx+1, 1] = pos[idx, 1] + velocity_y*self.delta_time + 0.5*ay*self.delta_time**2
            pos[idx][1] *= -1
            if self.check_if_point_is_out_of_window(pos[idx+1]):
                break
            idx += 1
        self.data = pos[:idx]

    def draw(self):
        if True == self.is_visible():
            for idx in range(0, len(self.data), 400):
                if not self.check_if_point_is_out_of_screen(self.data[idx]):
                    pygame.draw.circle(surface=self.window, color=self.color_manager.white, center=self.data[idx]+self.offset, radius=1)
                else:
                    break
