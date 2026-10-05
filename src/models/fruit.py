from typing import Literal

from pydantic import BaseModel, Field


class Fruit(BaseModel):
    name: str
    color: Literal["red", "green"]
    weight: float = Field(..., gt=0)
    bazam: dict[str, list[tuple[int, bool, float]]]
