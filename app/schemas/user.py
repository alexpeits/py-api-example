from uuid import UUID

from pydantic import BaseModel, constr


class CreateUserRequest(BaseModel):
    name: constr(max_length=20)

    class Config:
        extra = 'forbid'


class GetUserResponse(BaseModel):
    id: UUID
    name: str

    class Config:
        orm_mode = True
