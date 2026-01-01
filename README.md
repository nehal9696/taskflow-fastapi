# TaskFlow – FastAPI Backend Service

TaskFlow is a production-oriented backend API built using FastAPI, designed to demonstrate clean architecture, secure authentication, and scalable backend patterns.

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite (local) / PostgreSQL (production-ready)
- Pydantic
- JWT Authentication (upcoming)
- Alembic (upcoming)
- Pytest (upcoming)

## Features Implemented
- Modular FastAPI project structure
- Contract-first API design using Pydantic
- Database integration with SQLAlchemy
- Dependency-injected DB session management
- Auto-generated OpenAPI documentation

## Project Structure

app/
├── api/
├── core/
├── db/
├── models/
├── schemas/

## How to Run
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```