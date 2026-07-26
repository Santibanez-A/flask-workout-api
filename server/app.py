from flask import Flask, make_response
from flask_migrate import Migrate

from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# ALL workouts
@app.get('/workouts')
def get_workouts():
    return make_response(
        {"message": "List all workouts",}, 200
    )

#Get ID Workouts
@app.get('/workouts/<int:id>')
def get_workout_by_id(id):
    return make_response(
        {"message":f"Show workout {id}"},200
    )


#CREATE Workouts
@app.post('/workouts')
def create_workout():
    return make_response(
        {"message": "Create a workout"},201
    )

#DELETE Workouts by ID
@app.delete('/workouts/<int:id>')
def delete_workout(id):
    return make_response(
        {"message":f"Delete workout {id}"}, 200
    )

#GET ALL EXercises
@app.get('/exercises')
def get_exercises():
    return make_response(
        {"message":"List all exercises"}, 200
    )

#GET ID EXercises
@app.get('/exercises/<int:id>')
def get_exercise_by_id(id):
    return make_response(
        {"message":f"Show exercise {id}"}, 200
    )

#CREATE EXercises
@app.post('/exercises')
def post_exercises():
    return make_response(
        {"message": "Create an exercise"}, 201
    )

#DELETE EX by ID
@app.delete('/exercises/<int:id>')
def del_exercise_by_id(id):
    return make_response(
        {"message":f"Delete exercise {id}"}, 200
    )

#CREATE Workout- id - EX- ID - workEX
@app.post('/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises')
def add_exercise_to_workout(exercise_id, workout_id):
    return make_response(
        {"message":(f"Add exercise {exercise_id}"
                    f"Add workout {workout_id}")}, 201
    )

if __name__ == "__main__":
    app.run(port=5555, debug=True)