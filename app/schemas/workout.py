from datetime import date
from typing import Optional

from pydantic import BaseModel

class ExerciseCreate(BaseModel):
    name: str
    muscle_group: str
    equipment: str
    rep_ideal_range: int
    tips: Optional[str] = None

class ExerciseResponse(BaseModel):
    id: int
    name: str
    muscle_group: str
    equipment: str
    rep_ideal_range: int
    tips: Optional[str] = None

class WorkoutSessionCreate(BaseModel):
    date: date

class WorkoutSessionResponse(BaseModel):
    id: int
    date: date

class WorkoutSetCreate(BaseModel):
    session_id: int
    exercise_id: int
    weight_kg: float
    set_number: int
    actual_reps: int
    notes: str

class WorkoutSetResponse(BaseModel):
    id: int
    session_id: int
    exercise_id: int
    weight_kg: float
    set_number: int
    actual_reps: int
    notes: str