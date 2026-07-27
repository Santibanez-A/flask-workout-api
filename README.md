# Flask Workout API

## Project Description

Flask Workout API is a RESTful backend application for managing workouts, exercises, and the exercises performed during each workout.

The application uses Flask, SQLAlchemy, Flask-Migrate, Marshmallow, and SQLite. It supports creating, retrieving, and deleting workouts and exercises. It also supports connecting an existing exercise to an existing workout while recording sets, repetitions, or duration.

The database includes three main models:

* `Workout` stores the workout date, duration, and notes.
* `Exercise` stores the exercise name, category, and equipment requirement.
* `WorkoutExercise` connects workouts and exercises while storing sets, repetitions, and duration.

## Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd flask-workout-api
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Enter the virtual environment

```bash
pipenv shell
```

### 4. Move into the server directory

```bash
cd server
```

### 5. Apply the database migrations

```bash
flask db upgrade
```

### 6. Seed the database

```bash
python seed.py
```

The seed file creates sample workouts, exercises, and workout-exercise relationships.

## Running the Application

From the `server` directory, start the Flask development server:

```bash
flask run
```

The API will run at:

```text
http://127.0.0.1:5000
```

## API Endpoints

### Workouts

#### `GET /workouts`

Returns a list of all workouts. Each workout includes its related exercises and workout-exercise details.

#### `GET /workouts/<id>`

Returns one workout matching the provided ID.

Returns a `404` response if the workout does not exist.

#### `POST /workouts`

Creates a new workout.

Example request body:

```json
{
  "date": "2026-07-26",
  "duration_minutes": 60,
  "notes": "Upper-body workout"
}
```

The workout duration must be greater than zero.

#### `DELETE /workouts/<id>`

Deletes the workout matching the provided ID.

Returns a `404` response if the workout does not exist.

### Exercises

#### `GET /exercises`

Returns a list of all exercises. Each exercise includes its related workouts.

#### `GET /exercises/<id>`

Returns one exercise matching the provided ID.

Returns a `404` response if the exercise does not exist.

#### `POST /exercises`

Creates a new exercise.

Example request body:

```json
{
  "name": "Deadlift",
  "category": "Strength",
  "equipment_needed": true
}
```

The exercise name cannot be empty.

#### `DELETE /exercises/<id>`

Deletes the exercise matching the provided ID.

Returns a `404` response if the exercise does not exist.

### Workout Exercises

#### `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises`

Connects an existing exercise to an existing workout.

Example request body using sets and repetitions:

```json
{
  "sets": 4,
  "reps": 8
}
```

Example request body using duration:

```json
{
  "sets": 3,
  "duration_seconds": 60
}
```

Returns a `404` response if either the workout or exercise does not exist.

## Testing the API

After starting the Flask server, endpoints can be tested with a browser, Postman, or `curl`.

Example:

```bash
curl http://127.0.0.1:5000/workouts
```

```bash
curl http://127.0.0.1:5000/exercises
```

## Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* Marshmallow
* Marshmallow-SQLAlchemy
* SQLite
