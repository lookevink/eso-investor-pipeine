from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

# from app.models.source import Source  # circular import


class State(BaseModel):
    state_uuid: Optional[UUID] = uuid4()
    state_name: str
    state_code: str
    # state_source: Optional[Source] = None  # circular import


