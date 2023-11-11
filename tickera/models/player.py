from pydantic import BaseModel, validator
from .stats import Stats, Stat
from .location import Location
from typing import Literal

class Player(BaseModel):
    name: str
    stats: dict[str, dict[str, float]]
    lore: str
    location: dict[str, str] | None = None
    health: float = 100

    @validator("stats")
    @classmethod
    def validate_stats(cls, value):
        return Stats(**{stat: Stat(**value[stat]) for stat in value})
    
    def __str__(self):
        name = f"---\nName: {self.name} | Health: {self.health}\n"

        stats = f"---\nStats\n{str(self.stats)}---\n"
        location = f"Location: {self.location}\n---"

        return name + stats + location
    
    def set_location(self, location: Location) -> None:
        self.location = location.model_dump()

    def update(self, attribute: Literal["health", "location"], value: float | Location):
        if attribute == "health":
            self.health = self.health + value
        elif attribute == "location":
            self.location = value.model_dump()
        