from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from app.schemas.state import State


class Source(BaseModel):
    source_uuid: Optional[UUID] = uuid4()
    source_state: Optional[State] = None
    start_url: Optional[str] = None
    query_url: Optional[str] = None
    detail_url: Optional[str] = None
    cookies: Optional[bool] = False
    headless: Optional[bool] = False
    captcha: Optional[bool] = False
