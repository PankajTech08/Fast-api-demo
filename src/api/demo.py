from typing import Literal

from fastapi import APIRouter

from src.models.fruit import Fruit

router = APIRouter()


@router.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": (
            "Hello FastAPI Project!: run the http://127.0.0.1:8000/docs "
            "to see endpoints"
        )
    }


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"item_id": item_id, "query": q}


@router.post("/items/")
def create_item(name: str, price: float) -> dict[str, str | float]:
    return {"name": name, "price": price}


@router.get("/fruit")
def display_fruit() -> Fruit:
    return Fruit(
        name="Apple",
        color="red",
        weight=4.2,
        bazam={"foobar": [(1, True, 0.1)]},
    )
