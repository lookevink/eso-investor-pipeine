from fastapi import APIRouter, Depends
from typing import List
from uuid import UUID, uuid4

# from ..dependencies import get_token_header
from ..models.user import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

users_db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
    ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
    ),
    User(
        id=uuid4(),
        first_name="James",
        last_name="Gabriel",
    ),
    User(
        id=uuid4(),
        first_name="Eunit",
        last_name="Eunit",
    ),
]


@router.get("/", tags=["users"])
async def read_users() -> List[User]:
    return users_db
