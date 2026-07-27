from flask import Flask, request, make_response
from flask_migrate import Migrate
from marshmallow import ValidationError

from models import db, Exercise, Workout, WorkoutExercise
from schemas import (
    exercise_schema,
    exercises_schema,
    workout_schema,
    workouts_schema,
    workout_exercise_schema
)
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# ALL workouts
@app.get("/workouts")
def get_workouts():
    workouts = Workout.query.all()

    return make_response(
        workouts_schema.dump(workouts),
        200
    )

#Get ID Workouts
@app.get('/workouts/<int:id>')
def get_workout_by_id(id):
    workout = Workout.query.get(id)

    if not workout:
        return make_response(
            {"error": "Workout not found"},
            404
        )

    return make_response(
        workout_schema.dump(workout),
        200
    )
    

#CREATE Workouts
@app.post('/workouts')
def create_workout():
    data = request.get_json()
    try:
        new_workout = workout_schema.load(
            data,
            session=db.session
        )

        db.session.add(new_workout)
        db.session.commit()

        return make_response(
            workout_schema.dump(new_workout), 201
        )
    except ValidationError as error:
        return make_response(
            {"message": error.messages}, 400
        )


#DELETE Workouts by ID
@app.delete('/workouts/<int:id>')
def delete_workout(id):
    workout = Workout.query.get(id)

    if not workout:
        return make_response(
            {"error": "Workout not found"},404
        )

    db.session.delete(workout)
    db.session.commit()

    return make_response(
        {},204
        )


#GET ALL EXercises
@app.get('/exercises')
def get_exercises():
    exercises = Exercise.query.all()

    return make_response(
        exercises_schema.dump(exercises), 200
    )


#GET ID EXercises
@app.get('/exercises/<int:id>')
def get_exercise_by_id(id):
    exercise = Exercise.query.get(id)

    if not id:
        return make_response(
            {"message":"Error exercise not found"}, 404
        )


    return make_response(
        exercise_schema.dump(exercise), 200
    )


#CREATE EXercises
@app.post('/exercises')
def post_exercises():
    data = request.json()

    try:
        new_exercise = exercise_schema.load(
            data, session=db.session
        )

        db.session.add(new_exercise)
        db.session.commit()

        return make_response(
            exercise_schema.dump(new_exercise),201
        )

    except ValidationError as error:
        return make_response(
            {"error": error.messages},400
        )


#DELETE EX by ID
@app.delete('/exercises/<int:id>')
def delete_exercise(id):

    exercise = Exercise.query.get(id)

    if not exercise:
        return make_response(
            {"error":"Exercise not found"}, 404
        )

    db.session.delete(exercise)
    db.session.commit()

    return make_response(
        {}, 204
    )

#CREATE Workout- id - EX- ID - workEX
@app.post('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises')
def add_exercise_to_workout(exercise_id, workout_id):
    workout = Workout.query.get(workout_id)
    exercise = Exercise.query.get(exercise_id)

    if not workout:
        return make_response(
            {"error": "Workout not found"}, 404
        )

    if not exercise:
        return make_response(
            {"error": "Exercise not found"}, 404
        )


    data = request.json() or {}

    new_workout_exercise = WorkoutExercise(
        workout_id=workout_id,
        exercise_id=exercise_id,
        reps=data.get("reps"),
        sets=data.get("sets"),
        duration_seconds=data.get("duration_seconds")
    )

    db.session.add(new_workout_exercise)
    db.session.commit()

    return make_response(
        workout_exercise_schema.dump(new_workout_exercise), 201
    )




if __name__ == "__main__":
    app.run(port=5555, debug=True)