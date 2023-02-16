class Mode:
    def __init__(self, is_second_house_added=False) -> None:
        self.modes = ("Single Blue", "Single Yellow", "On Rep Blue", "On Rep Yellow", "Simult")
        if False == is_second_house_added:
            self.modes = ("Single Blue",)
        self.index = 0
        self.space_press_counter = 1
        self.space_states = {"first_ready": 1, "second_ready": 2, "finished": 3}
        self.current_space_press_state = self.space_states["first_ready"]
        self.run_first, self.run_second = False, False
        self.is_locked = False

    def change_mode(self):
        if self.index < len(self.modes)-1:
            self.index += 1
        else:
            self.index = 0

    def get_mode(self):
        return self.modes[self.index]
    
    def run(self):
        if False == self.is_locked:
            if self.index == 0:
                self.start_first()
                self.stop_second()
            elif self.index == 1:
                self.stop_first()
                self.start_second()
            elif self.index == 2:
                if self.space_states["first_ready"] == self.current_space_press_state:
                    self.start_first()
                    self.current_space_press_state = self.space_states["second_ready"]
                elif self.space_states["second_ready"] == self.current_space_press_state:
                    self.start_second()
                    self.current_space_press_state = self.space_states["finished"]
            elif self.index == 3:
                if self.space_states["first_ready"] == self.current_space_press_state:
                    self.start_second()
                    self.current_space_press_state = self.space_states["second_ready"]
                elif self.space_states["second_ready"] == self.current_space_press_state:
                    self.start_first()
                    self.current_space_press_state = self.space_states["finished"]
            elif self.index == 4:
                self.lock()
                self.start_first()
                self.start_second()

    def start_first(self):
        self.run_first = True

    def stop_first(self):
        self.run_first = False

    def start_second(self):
        self.run_second = True

    def stop_second(self):
        self.run_second = False

    def is_first_running(self):
        return self.run_first

    def is_second_running(self):
        return self.run_second

    def lock(self):
        self.is_locked = True

    def unlock(self):
        if self.space_states["finished"] == self.current_space_press_state:
            self.current_space_press_state = self.space_states["first_ready"]
        self.is_locked = False