from typing import Annotated

from pydantic import BaseModel, StringConstraints, Field


class People(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, max_length=50)]
    birth_year: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    eye_color: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    gender: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    hair_color: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    height: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    mass: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    skin_color: Annotated[str, StringConstraints(min_length=1, max_length=20)]
    homeworld: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    films: list[Annotated[str, Field(strict=True)]]
    species: list[Annotated[str, Field(strict=True)]]
    starships: list[Annotated[str, Field(strict=True)]]
    vehicles: list[Annotated[str, Field(strict=True)]]
    url: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    created: Annotated[str, StringConstraints(min_length=1, max_length=40)]
    edited: Annotated[str, StringConstraints(min_length=1, max_length=40)]


class ListPeople(BaseModel):
    count: Annotated[int, Field(strict=True, gt=0)]
    next: Annotated[str, StringConstraints(min_length=1, max_length=100)]
    previous: None
    results: list[People]

