# GymTracker Bot — Project State & AI Context

**Note to AI Assistant:** The user is providing this file to give you the complete context of their project. Read this carefully before providing guidance. Pick up exactly at the "Immediate Next Steps" section.

## 🎯 Project Goal
Transform a legacy project into a modern **Telegram Gym Tracker Bot**. 
The user wants to log exercises, track progress over time, and deploy the bot to a free cloud service (like Railway or Render). This is a learning project aimed at practicing cloud/backend skills.

## 🛠 Tech Stack
*   **Language:** Python 3.10+
*   **Web Framework:** FastAPI
*   **Database:** PostgreSQL (currently running locally via Docker Compose)
*   **ORM:** SQLAlchemy 2.0 (using `asyncio` and `asyncpg`)
*   **Migrations:** Alembic
*   **Validation/Config:** Pydantic V2 & `pydantic-settings`
*   **Bot Framework (Future):** `python-telegram-bot` (Webhook architecture)

## ✅ Completed Work (Phase 1 Progress)
1. **Fresh Start:** Completely wiped the old SQLite codebase and initialized a fresh Git repository.
2. **Infrastructure:**
   * Created `docker-compose.yml` to run `postgres:16` and `adminer`.
   * Created `pyproject.toml` for dependencies and editable install (`pip install -e .`).
3. **Core App Structure:**
   * `app/config.py`: Centralized Pydantic settings loading `DATABASE_URL` from `.env`.
   * `app/database.py`: Configured `create_async_engine` and `async_sessionmaker`.
4. **Database Models (`app/models/workout.py`):**
   * `Exercise`: id, name, muscle_group, equipment, rep_ideal_range, tips.
   * `WorkoutSession`: id, date.
   * `WorkoutSet`: id, session_id (FK), exercise_id (FK), weight_kg, set_number, actual_reps, notes.
5. **API Schemas (`app/schemas/workout.py`):**
   * Created Pydantic models for Create and Response operations for all three models.
   * Configured `model_config = {"from_attributes": True}` on Response schemas to support SQLAlchemy objects.

## 🚀 Immediate Next Steps
The database is running, and the Python models are written. The very next thing the user needs to do is generate the tables using Alembic.

1.  **Initialize Alembic:** Guide the user to run `alembic init alembic`.
2.  **Configure Alembic for Async:** Help the user edit `alembic.ini` and `alembic/env.py` to support `asyncpg` and point to `app.database.Base.metadata`.
3.  **Generate Migration:** Guide the user to run `alembic revision --autogenerate -m "Initial tables"`.
4.  **Apply Migration:** Run `alembic upgrade head`.

## 🔮 Future Phases
Once the database tables exist:
*   **Phase 1 (Cont'd):** Build FastAPI CRUD endpoints in `app/routers/` to test data insertion/retrieval via Swagger UI.
*   **Phase 2:** Build the Telegram Bot (`app/bot/handlers.py`) and connect it to the FastAPI endpoints.
*   **Phase 3:** Dockerize the FastAPI app itself and deploy to Railway/Render.
