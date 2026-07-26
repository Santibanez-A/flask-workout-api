from marshmallow import fields, validates, ValidationError
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import Exercise, Workout, WorkoutExercise


class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        include_fk = True

    exercise = fields.Nested(
        lambda: ExerciseSchema(
            only=("id", "name", "category", "equipment_needed")
        ),
        dump_only=True
    )


class ExerciseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True

    workouts = fields.Nested(
        lambda: WorkoutSchema(
            only=("id", "date", "duration_minutes", "notes")
        ),
        many=True,
        dump_only=True
    )
    @validates("name")
    def validate_name(self, value):
        if not value or not value.strip():
            raise ValidationError("Exercise name cannot be empty.")


class WorkoutSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True

    exercises = fields.Nested(
        ExerciseSchema,
        many=True,
        dump_only=True,
        exclude=("workouts",)
    )

    workout_exercises = fields.Nested(
        WorkoutExerciseSchema,
        many=True,
        dump_only=True,
    )

    @validates("duration_minutes")
    def validate_duration(self, value):
        if value <= 0:
            raise ValidationError(
            "Workout duration must be greater than zero."
        )



exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)