from typing import List
from uuid import uuid4

from fastapi import APIRouter  # , Depends


# from ..dependencies import get_token_header
from ..models.agent import Agent
from ..models.entity import Entity
from ..models.source import Source
from ..models.state import State

router = APIRouter(
    prefix="/agents",
    tags=["agents"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

agents_db: List[Agent] = [
    Agent(
        agent_uuid=uuid4(),
        agent_state=State(
            state_uuid=uuid4(),
            state_name="Arizona",
            state_code="az"
        ),
        agent_source=Source(
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
        agent_name="Test Agent",
    ),
    Agent(
        agent_uuid=uuid4(),
        agent_state=State(
            state_uuid=uuid4(),
            state_name="Arizona",
            state_code="az"
        ),
        agent_source=Source(
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
        agent_name="Test Agent 2",
    ),
    Agent(
        agent_uuid=uuid4(),
        agent_state=State(
            state_uuid=uuid4(),
            state_name="Arizona",
            state_code="az"
        ),
        agent_source=Source(
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
        agent_name="Test Agent",
    ),
]


@router.get("/", tags=["agents"])
async def read_agents() -> List[Agent]:
    return agents_db
