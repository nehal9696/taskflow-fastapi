from fastapi import FastAPI

from app.api.v1.routes import users
from app.db.session import engine
from app.db.base import Base
from app.models import user, task
from app.api.v1.routes import auth
from app.api.v1.routes import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskFlow API",
    description="Backend services for task management.",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}