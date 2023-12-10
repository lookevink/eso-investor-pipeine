from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

# from app.models.entity import Entity  # circular import
from app.schemas.source import Source
from app.schemas.state import State


class Agent(BaseModel):
    agent_uuid: Optional[UUID] = uuid4()
    agent_state: Optional[State] = None
    agent_source: Optional[Source] = None
    agent_name: Optional[str] = None
    agent_appointed_status:  Optional[str] = None
    agent_attention: Optional[str] = None
    agent_address: Optional[str] = None
    agent_last_updated: Optional[str] = None
    agent_email: Optional[str] = None
    agent_mailing_address: Optional[str] = None
    agent_county: Optional[str] = None
    # agent_entities: Optional[List[Entity]] = None  # circular import
