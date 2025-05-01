from pydantic import BaseModel
from uuid import UUID

class TaskCreate(BaseModel):
    task_text: str


class TaskResponse(BaseModel):
    id: UUID
    task_text: str
    is_active: bool

    class Config:
        from_attributes = True