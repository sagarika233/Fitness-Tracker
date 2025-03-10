import json
import os

class Database:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump([], f)

    def load_data(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_data(self, data):
        existing_data = self.load_data()
        existing_data.append(data)
        with open(self.filename, "w") as f:
            json.dump(existing_data, f, indent=4)
