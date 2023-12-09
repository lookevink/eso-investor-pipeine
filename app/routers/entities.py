from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/entities",
    tags=["entities"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_entities_db = {"123456789": {"name": "Entity 1"}, "987654321": {"name": "Entity 2"}}


@router.get("/", tags=["entities"])
async def read_entities() -> dict[str, dict[str, str]]:
    return fake_entities_db


@router.get("/{entity_uuid}", tags=["entities"])
async def read_entity(entity_uuid: str) -> dict[str, str]:
    if entity_uuid not in fake_entities_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"name": fake_entities_db[entity_uuid]["name"], "entity_uuid": entity_uuid}


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