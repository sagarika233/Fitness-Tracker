from database import Database

class FitnessTracker:
    def __init__(self, user):
        self.user = user
        self.db = Database("workouts.json")

    def log_workout(self, workout_type, duration, calories):
        workout = {
            "type": workout_type,
            "duration": duration,
            "calories": calories
        }
        self.db.save_data(workout)

    def view_workouts(self):
        return self.db.load_data()
