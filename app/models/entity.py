from typing import List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel

from app.models.agent import Agent
from app.models.source import Source
from app.models.state import State


class Entity(BaseModel):
    entity_uuid: Optional[UUID] = uuid4()
    entity_state: Optional[State] = None
    entity_source: Optional[Source] = None
    entity_external_id: Optional[str] = None
    entity_name:  Optional[str] = None
    entity_type: Optional[str] = None
    entity_county: Optional[str] = None
    entity_agent_name: Optional[str] = None
    entity_agent_type: Optional[str] = None
    eneity_status: Optional[str] = None
    entity_formation_date: Optional[str] = None
    entity_reason_for_status: Optional[str] = None
    entity_approval_date: Optional[str] = None
    entity_status_date: Optional[str] = None
    entity_original_incorporation_date: Optional[str] = None
    entity_life_period: Optional[str] = None
    entity_business_type: Optional[str] = None
    entity_last_annual_report_filed: Optional[str] = None
    entity_domicile_state: Optional[str] = None
    entity_annual_report_due_date: Optional[str] = None
    entity_years_due: Optional[str] = None
    entity_original_publish_date: Optional[str] = None
    entity_statutory_agent: Optional[Agent] = None
    entity_principal_information: Optional[List[dict]] = None
    entity_address: Optional[str] = None
    entity_address_last_updated: Optional[str] = None
    entity_principal_office_address: Optional[dict] = None
    entity_principal_office_address_last_updated: Optional[str] = None
