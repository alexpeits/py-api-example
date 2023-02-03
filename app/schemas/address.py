from uuid import UUID

from pydantic import BaseModel, constr


class CreateUserAddressRequest(BaseModel):
    address: constr(max_length=100)

    class Config:
        extra = "forbid"


class GetAddressResponse(BaseModel):
    id: UUID
    address: str

    class Config:
        orm_mode = True
