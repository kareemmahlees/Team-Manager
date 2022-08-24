from pydantic import BaseModel, UUID4
from datetime import date


class ReturnLogin(BaseModel):
    id: UUID4
    username: str
    phone: str
    gender: str
    role: str


class TaskReturn(BaseModel):
    title: str
    description: str
    created_at: date
    deadline: date
    created_by: str
    member_id: UUID4
    id: int
    member_name: str
