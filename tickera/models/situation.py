from pydantic import BaseModel
from .location import Location
from .player import Player
from .event import PlayerEvent

class Situation(BaseModel):
    location: Location
    description: str
    players: list[Player]

