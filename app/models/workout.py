from datetime import date

from app.database import Base
from sqlalchemy import Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Exercise(Base):
    __tablename__ = "exercises"    # actual table name in Postgres

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    muscle_group: Mapped[str] = mapped_column(String(100))
    equipment: Mapped[str] = mapped_column(String(100))
    rep_ideal_range: Mapped[int] = mapped_column(Integer)
    tips: Mapped[str] = mapped_column(String(500))

class WorkoutSession(Base):
    __tablename__ = "workout_sessions"    # actual table name in Postgres

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    date: Mapped[date] = mapped_column(Date)

class WorkoutSet(Base):
    __tablename__ = "workout_sets"    # actual table name in Postgres

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    session_id: Mapped[int] = mapped_column(Integer, ForeignKey("workout_sessions.id"))
    exercise_id: Mapped[int] = mapped_column(Integer, ForeignKey("exercises.id"))
    weight_kg: Mapped[float] = mapped_column(Float)
    set_number: Mapped[int] = mapped_column(Integer)
    actual_reps: Mapped[int] = mapped_column(Integer)
    notes: Mapped[str] = mapped_column(String(500))
