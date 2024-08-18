from datetime import datetime

class Lift:
  def __init__(self, exercise, weight, sets, reps, rpe, date=None, notes="", roasted=False, roastedcomments = ""):
    self.exercse = exercise
    self.weight = weight
    self.sets = sets
    self.reps = reps
    self.rpe = rpe
    self.date = date or datetime.now().strftime('%Y-%m-%d')
    self.notes = notes
    self.roasted = roasted
    self.roastedcomments = roastedcomments

    def __str__(self):
      roast_status = "Yes" if self.roasted else "No"
      roast_comment_display = f" | Roast Comment: {self.roast_comment}" if self.roast_comment else ""
      return f"{self.date}: {self.exercise} - {self.weight} lbs for {self.sets} sets of {self.reps} reps | Roasted: {roast_status}{roast_comment_display} | Notes: {self.notes}"