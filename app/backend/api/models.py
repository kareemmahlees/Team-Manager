from pydantic import BaseModel, UUID4


class ReturnLogin(BaseModel):
    id: UUID4
    username: str
    phone: str
    gender: str
    role: str
