from pydantic import BaseModel, validator
from typing import Literal
from .player import Player
from magentic import prompt
from .location import Object

class AttributeDeltaUpdate(BaseModel):
    attribute: str
    value: float

    def __call__(self, target: Player):
        target = target.as_dict()
        target[self.attribute] = target[self.attribute] + self.value
        return Player(**target)
    
class InventoryUpdate(BaseModel):
    mode: Literal["add", "delete"]
    item: Object

    def __call__(self, target: Player):
        if self.mode == "add":
            target.inventory.append(self.item)
            return target
        target.inventory.remove(self.item)
        return target


@prompt("Create a AttributeDeltaUpdate based on this action: {description} on a {player_class}.")
def create_attribute_update(description: str, player_class = Player) -> AttributeDeltaUpdate:
    ...

@prompt("Create a InventoryUpdate based on this action: {description} from a Player.")
def create_inventory_update(description: str) -> InventoryUpdate:
    ...
 

class Effect(BaseModel):
    type_: Literal["attribute_change", "inventory_change"]
    description: str
    effect_class: InventoryUpdate | AttributeDeltaUpdate = None

    def set_call(self):
        if self.type_ == "attribute_change":
            self.effect_class = create_attribute_update(self.description)
            return
        self.effect_class = create_inventory_update(self.description)

    def __call__(self, target: Player):
        return self.effect_class(target)



class PlayerEvent(BaseModel):
    effect: dict[str, str]

    @validator("effect")
    @classmethod
    def set_effect(cls, value):
        value = Effect(**value)
        value.set_call()
        return value
    
    def __call__(self, target: list[Player] | Player):
        if isinstance(target, list):
            out = []
            for t in target:
                out.append(self.effect(t))
            return out
        return self.effect(target)

    

