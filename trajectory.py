import pygame
import json
import numpy

import color

class Trajectory:
    def __init__(self, window) -> None:
        self.window = window
        self.color_manager = color.Color()
        self.data = []

        self.initial_velocity = 40
        self.angle = 45
        self.offset = pygame.math.Vector2(0, 0)
        self.delta_time = 1e-3
        self.gravity = 9.807

        with open('default_settings.json') as default_settings_file:
            self.default_settings = json.load(default_settings_file)
        with open('trajectory_settings.json') as trajectory_settings_file:
            self.trajectory_settings = json.load(trajectory_settings_file)

    def set_offset(self, new_offset):
        self.offset.update(new_offset)
    
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

    def check_if_point_is_out_of_screen(self, point):
        cartesian_point = pygame.math.Vector2(point[0], point[1]) + self.offset
        return  cartesian_point.x > pygame.display.get_surface().get_size()[0] or \
                cartesian_point.x < 0 or \
                cartesian_point.y < 0 or \
                cartesian_point.y > pygame.display.get_surface().get_size()[1]-self.default_settings["hud"]["height"]

    def check_if_point_is_out_of_window(self, point):
        cartesian_point = pygame.math.Vector2(point[0], -point[1]) + self.offset
        return  cartesian_point.x > pygame.display.get_surface().get_size()[0] or \
                cartesian_point.x < 0 or \
                cartesian_point.y < 0 or \
                cartesian_point.y > 2*pygame.display.get_surface().get_size()[1]

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
        for idx in range(0, len(self.data), 400):
            if not self.check_if_point_is_out_of_screen(self.data[idx]):
            # if self.data[idx][1]+self.offset.y < pygame.display.get_surface().get_size()[1]-self.default_settings["hud"]["height"]:
                pygame.draw.circle(surface=self.window, color=self.color_manager.white, center=self.data[idx]+self.offset, radius=1)
            else:
                break
