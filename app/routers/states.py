from fastapi import APIRouter, Depends

from ..dependencies import get_token_header
from ..models.state import State

router = APIRouter(
    prefix="/states",
    tags=["states"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

states_db = {
    "0": State(
        state_uuid="0",
        state_name="Arizona",
        state_code="az"
    ),
    "1": State(
        state_uuid="1",
        state_name="Colorado",
        state_code="co"
    ),
    "2": State(
        state_uuid="2",
        state_name="California",
        state_code="ca"
    ),
}


@router.get("/", tags=["states"])
async def read_states() -> dict[str, State]:
    return states_db
