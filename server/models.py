
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

# Define models here
class Exercise:(db.Model)
__tablename__ = "exercises"


id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String)
category = db.Column(db.String)
equipment_needed = db.Column(db.Boolean)

#workoutEX to Exercise
workout_exercises = db.relationship(
    "WorkoutExercises",
    back_populates="exercise"
    )


#workouts to Ex M -U
workouts = db.relationship(
    "Workout",
    secondary="workout_exercise",
    viewonly=True
)


class Workout:(db.Model)
__tablename__ = "workouts"

id = db.Column(db.Integer, primary_key=True)
date = db.Column(db.Date)
duration_minutes = db.Column(db.Integer)
notes = db.Column(db.Text)

#workoutEX to Workout U
workout_exercises = db.relationship(
    "WorkoutExercises",
    back_populates="workout"
    )


#workout to WorkoutEx M -U
exercises = db.relationship(
    "Exercise",
    secondary="workout_exercise",
    viewonly=True
)



class WorkoutExercise:(db.Model)
__tablename__ = "workout_exercise"

id = db.Column(db.Integer, primary_key=True)
workout_id = db.Column(db.Integer, db.ForeignKey("workouts.id"))
exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))
reps = db.Column(db.Integer)
sets = db.Column(db.Integer)
duration_seconds = db.Column(db.Integer)

#workout to workoutEX U
workout = db.relationship(
    "Workout",
    back_populates="workout_exercise"
)

#exercises to workoutEX U
exercise = db.relationship(
    "Exercise",
    back_populates="workout_exercise"
    )
