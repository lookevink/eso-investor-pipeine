from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException  # Depends,

from app.schemas.entity import Entity

# from ..dependencies import get_token_header

router = APIRouter(
    prefix="/entities",
    tags=["entities"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


def uuid():
    pass


fake_entities_db: List[Entity] = [
    Entity(
        entity_uuid=uuid4(),
        entity_name="Test Entity",
    ),
    Entity(
        entity_uuid=uuid4(),
        entity_name="Test Entity 2",
    ),
    Entity(
        entity_uuid=uuid4(),
        entity_name="Test Entity 3",
    ),
    Entity(
        entity_uuid=uuid4(),
        entity_name="Test Entity 4",
    ),
]


@router.get("/", tags=["entities"])
async def read_entities() -> list[Entity]:
    return fake_entities_db


@router.get("/{entity_uuid}", tags=["entities"])
async def read_entity(entity_uuid: str) -> Entity:
    if entity_uuid not in fake_entities_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return next((x for x in fake_entities_db if x.entity_uuid == entity_uuid), None)


@router.put(
    "/{entity_uuid}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_entity(entity_uuid: str):
    if entity_uuid != "123456789":
        raise HTTPException(
            status_code=403, detail="You can only update the item: 123456789"
        )
    return {"entity_uuid": entity_uuid, "name": "Updated Entity Name"}
