#!/usr/bin/env python3
from datetime import date
from app import app
from models import db, Exercise, Workout, WorkoutExercise


with app.app_context():

    print("Clearing database...")

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Creating exercises...")

    bench_press = Exercise(
        name="Bench Press",
        category="Strength",
        equipment_needed=True
    )

    squat = Exercise(
        name="Back Squat",
        category="Strength",
        equipment_needed=True
    )

    plank = Exercise(
        name="Plank",
        category="Core",
        equipment_needed=False
    )

    db.session.add_all([
        bench_press,
        squat,
        plank
    ])
    db.session.commit()

    print("Creating workouts...")

    workout1 = Workout(
        date=date(2026, 7, 26),
        duration_minutes=60,
        notes="Push day"
    )

    workout2 = Workout(
        date=date(2026, 7, 27),
        duration_minutes=75,
        notes="Leg day"
    )

    db.session.add_all([
        workout1,
        workout2
    ])
    db.session.commit()

    print("Connecting workouts and exercises...")

    db.session.add_all([
        WorkoutExercise(
            workout=workout1,
            exercise=bench_press,
            sets=4,
            reps=8
        ),
        WorkoutExercise(
            workout=workout2,
            exercise=squat,
            sets=4,
            reps=6
        ),
        WorkoutExercise(
            workout=workout1,
            exercise=plank,
            sets=3,
            duration_seconds=60
        )
    ])

    db.session.commit()

    print("Seed complete!")