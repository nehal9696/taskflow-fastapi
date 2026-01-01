from pydantic import BaseModel, Field
from typing import Optional 
from datetime import datetime

class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    
class TaskResponse(BaseModel):
    id: int 
    title: str
    desciption: Optional[str]
    is_completed: bool
    created_at: datetime
    
    class Config:
        from_attributes = True