from typing import Optional

from pydantic import BaseModel


class Source(BaseModel):
    source_uuid: str
    source_url: str
    source_name: str
    source_state: str
    source_type: str
    source_subtype: str
    source_category: str
    source_description: Optional[str] = None
    source_notes: Optional[str] = None
    source_last_updated: Optional[str] = None
    source_last_updated_by: Optional[str] = None
    source_created: Optional[str] = None
    source_created_by: Optional[str] = None
    source_deleted: Optional[bool] = False
    source_deleted_date: Optional[str] = None
    source_deleted_by: Optional[str] = None
    source_deleted_reason: Optional[str] = None
    source_deleted_notes: Optional[str] = None
    source_deleted_last_updated: Optional[str] = None
    source_deleted_last_updated_by: Optional[str] = None
    source_deleted_created: Optional[str] = None
    source_deleted_created_by: Optional[str] = None
