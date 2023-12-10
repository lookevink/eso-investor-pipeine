from pydantic import BaseModel, Field


class EntityNames(BaseModel):
    """
    Represents a list of entity names.

    Attributes:
        names (list[str]): The list of entity names.

    """
    names: list[str] = Field(..., example=["Venture REI", "Another Co"])
