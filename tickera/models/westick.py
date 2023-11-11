from pydantic import BaseModel, validator
from .player import Player
from .location import Location 
from uuid import uuid4
from pathlib import Path
from magentic import prompt
import random

@prompt("Create a random RPG story with a {theme} theme place with a name, short description and list of visible objects.")
def create_location(theme: str ) -> Location:
    ...

class WesTick(BaseModel):
    difficulty: float
    db: Path
    __session_id: str = uuid4()
    players: list[Player] = []
    npcs: list = []
    locations: list[Location] = [create_location(theme = "random")]

    def add_player(self, player: Player):
        if not player.location:
            self.players.append(player)
            return
        random_location = random.choice(self.locations)
        player.set_location(random_location)
        self.players.append(player)

    def create_npc(self, npc):
        pass

    @classmethod
    def create_location(cls, theme: str = "random") -> Location:
        return create_location(theme)

    def add_location(self, location: Location) -> None:
        self.locations.append(location)

    def at_least_one_alive(self):
        return sum([p.health > 0 for p in self.players]) > 0
    
    def get_player(self, name):
        for p in self.players:
            if p.name == name:
                return p 
    
    
    def run(self) -> None:
        
        while self.at_least_one_alive():
            self.get_player("minoru").update("health", "-5")
            print(self.get_player("minoru"))



    def __str__(self):
        id_info = f"id: {self.__session_id}\n"
        db_info = f"db: {str(self.db)}\n"
        players = f"players: {', '.join([p.name for p in self.players])}\n"
        npcs = f"npcs: {', '.join([p.name for p in self.npcs])}"
        return id_info + db_info + players + npcs
