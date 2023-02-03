from app.lib.db.session import create_session
from app.models import Address, User
from app.schemas.address import CreateUserAddressRequest, GetAddressResponse
from app.schemas.user import CreateUserRequest, GetUserResponse
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/{user_id}")
async def get_user_by_uuid(user_id):
    with create_session() as session:
        user = session.get(User, user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return GetUserResponse.from_orm(user)


@router.post("/", status_code=201)
async def create_user(user_data: CreateUserRequest):
    with create_session() as session:
        user = User(name=user_data.name)
        session.add(user)
        session.commit()
        response = GetUserResponse.from_orm(user)

    return response


@router.get("/{user_id}/addresses")
async def get_users_addresses(user_id):
    with create_session() as session:
        user = session.get(User, user_id)
        addresses = user.addresses

    return [GetAddressResponse.from_orm(address) for address in addresses]


@router.post("/{user_id}/addresses")
async def create_user_address(user_id, address_data: CreateUserAddressRequest):
    with create_session() as session:
        user = session.get(User, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        address = Address(address=address_data.address, user_id=user.id)
        session.add(address)
        session.commit()

        response = GetAddressResponse.from_orm(address)

    return response
