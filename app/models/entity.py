from typing import Optional

from pydantic import BaseModel


class Entity(BaseModel):
    entity_uuid: str
    entity_name: str
    file_number: Optional[str] = None
    state: Optional[str] = None
    status: Optional[str] = None
    address: Optional[str] = None
    agent: Optional[str] = None
    agent_address: Optional[str] = None
    entity_type: Optional[str] = None
    entity_subtype: Optional[str] = None
    status_date: Optional[str] = None
    status_change_date: Optional[str] = None
    registered_date: Optional[str] = None
    standing: Optional[str] = None
    jurisdiction: Optional[str] = None
    url: Optional[str] = None
    source: Optional[str] = None
    source_id: Optional[str] = None
    source_url: Optional[str] = None
    source_date: Optional[str] = None
    source_data: Optional[str] = None
    source_data_hash: Optional[str] = None
    notes: Optional[str] = None
    last_updated: Optional[str] = None
    last_updated_by: Optional[str] = None
    created: Optional[str] = None
    created_by: Optional[str] = None
    deleted: Optional[bool] = False
    deleted_date: Optional[str] = None
    deleted_by: Optional[str] = None
    deleted_reason: Optional[str] = None
    deleted_notes: Optional[str] = None
    deleted_source: Optional[str] = None
    deleted_source_id: Optional[str] = None
    deleted_source_url: Optional[str] = None
    deleted_source_date: Optional[str] = None
    deleted_source_data: Optional[str] = None
    deleted_source_data_hash: Optional[str] = None
    deleted_last_updated: Optional[str] = None
    deleted_last_updated_by: Optional[str] = None
    deleted_created: Optional[str] = None
    deleted_created_by: Optional[str] = None
