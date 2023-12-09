from fastapi import APIRouter  # , Depends
from typing import List
from uuid import uuid4  # , UUID

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
        user_uuid=uuid4(),
        first_name="John",
        last_name="Doe",
    ),
    User(
        user_uuid=uuid4(),
        first_name="Jane",
        last_name="Doe",
    ),
    User(
        user_uuid=uuid4(),
        first_name="James",
        last_name="Gabriel",
    ),
    User(
        user_uuid=uuid4(),
        first_name="Eunit",
        last_name="Eunit",
    ),
]


@router.get("/", tags=["users"])
async def read_users() -> List[User]:
    return users_db
