class Mode:
    def __init__(self, is_second_house_added=False) -> None:
        self.modes = ("Single Blue", "Single Yellow", "On Rep Blue", "On Rep Yellow", "Simult")
        if False == is_second_house_added:
            self.modes = ("Single Blue",)
        self.index = 0
        self.space_press_counter = 1
        self.run_first, self.run_second = False, False

    def change_mode(self):
        if self.index < len(self.modes)-1:
            self.index += 1
        else:
            self.index = 0

    def get_mode(self):
        return self.modes[self.index]
    
    def run(self):
        if self.index == 0:
            self.start_first()
            self.stop_second()
        elif self.index == 1:
            self.stop_first()
            self.start_second()
        elif self.index == 2:
            if 1 == self.space_press_counter:
                self.start_first()
                self.space_press_counter = 2
            else:
                self.start_second()
                self.space_press_counter = 1
        elif self.index == 3:
            if 1 == self.space_press_counter:
                self.start_second()
                self.space_press_counter = 2
            else:
                self.start_first()
                self.space_press_counter = 1
        elif self.index == 4:
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