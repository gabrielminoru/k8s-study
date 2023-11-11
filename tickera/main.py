from models.westick import WesTick
from models.player import Player
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

player = Player(name = "minoru", stats = stats, lore = "a")



tick.add_player(player)

print(tick)


