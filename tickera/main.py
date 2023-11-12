from models.westick import WesTick
from models.player import Player
from models.event import PlayerEvent
from pathlib import Path

tick = WesTick(difficulty = 5, db = Path("test/"))


DEFAULT_STATUS = 50
DEFAULT_MAX_STATUS = 100
DEFAULT_BONUS = 0
DEFAULT_MAX_BONUS=50

stats = {
    stat_name: {
        "base": DEFAULT_STATUS,
        "bonus": DEFAULT_BONUS,
        "max_base": DEFAULT_MAX_STATUS,
        "max_bonus": DEFAULT_MAX_BONUS
    } for stat_name in ("intelligence", "strength", "dexterity", "agility", "luck", "vitality")
}

player = Player(name = "minoru", stats = stats, lore = "a", inventory = [])
print(player)
finds_something = f"finds {tick.locations[0].objects[0]} and puts it in his pocket"
print(finds_something)
finds_something_effect = PlayerEvent(effect = {"type_": "inventory_change", "description": finds_something})
print(finds_something_effect)

dies = PlayerEvent(effect = {"type_": "attribute_change", "description": "takes a shot, receives lethal damage"})
player = dies(finds_something_effect(player))
print(player)
#tick.add_player(player)

#print(tick.players)


