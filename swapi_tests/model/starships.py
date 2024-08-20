from typing import Annotated

from pydantic import BaseModel, StringConstraints, Field


class StarShip(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    model: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    starship_class: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    manufacturer: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    cost_in_credits: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    length: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    crew: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    passengers: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    max_atmosphering_speed: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    hyperdrive_rating: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    MGLT: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    cargo_capacity: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    consumables: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    films: list[Annotated[str, StringConstraints(min_length=1, max_length=100)]]
    pilots: list[Annotated[str, StringConstraints(min_length=1, max_length=100)]]
    url: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    created: Annotated[str, StringConstraints(min_length=1, max_length=40)]
    edited: Annotated[str, StringConstraints(min_length=1, max_length=40)]


class ListStarShips(BaseModel):
    count: Annotated[int, Field(strict=True, gt=0)]
    next: Annotated[str | None, StringConstraints(min_length=1, max_length=100)]
    previous: None
    results: list[StarShip]


