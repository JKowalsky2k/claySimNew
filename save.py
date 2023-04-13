import json

class Save:
    def __init__(self) -> None:
        self.index = 0
        self.data = dict()
        self.load()

    def save(self,  start_point1, start_point2, trajectory1, 
                    end_point1, end_point2, trajectory2):
        pass

    def load(self):
        pass

    def save_file_to_disc(self):
        with open("saved_trajectories.json", "w") as file:
            json.dump(self.data, file)

    def load_file_from_disc(self):
        with open("saved_trajectories.json", "r") as file:
            self.data = json.load(file)

    def get_save(self):
        return self.data[self.index]

    def change_save(self):
        self.index = (self.index + 1) % len(self.data)

