from typing import List
from uuid import uuid4

from fastapi import APIRouter  # , Depends

# from ..dependencies import get_token_header
from ..models.source import Source
from ..models.state import State

router = APIRouter(
    prefix="/sources",
    tags=["sources"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

sources_db: List[Source] = [
    Source(
        source_uuid=uuid4(),
        source_state=State(
            state_uuid=uuid4(),
            state_name="Arizona",
            state_code="az"
        ),
        start_url="https://ecorp.azcc.gov/EntitySearch/Index",
        query_url="https://ecorp.azcc.gov/EntitySearch/Search",
        detail_url="https://ecorp.azcc.gov/BusinessSearch/BusinessInfo?entityNumber=",
    ),
    Source(
        source_uuid=uuid4(),
        source_state=State(
            state_uuid=uuid4(),
            state_name="Colorado",
            state_code="co"
        ),
    ),
    Source(
        source_uuid=uuid4(),
        source_state=State(
            state_uuid=uuid4(),
            state_name="California",
            state_code="ca"
        ),
    ),
]


@router.get("/", tags=["sources"])
async def read_sources() -> List[Source]:
    return sources_db
