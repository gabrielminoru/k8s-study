from pydantic import BaseModel, root_validator

class Stat(BaseModel):
    base: float
    bonus: float

    max_base: float
    max_bonus: float

    @root_validator(pre = True)
    @classmethod
    def validate(cls, values):
        assert values['max_base'] >= values['base'], "Base value is larger than allowed."
        assert values['max_bonus'] >= values['bonus'], "Bonus is larger than allowed."
        return values

class Stats(BaseModel):
    strength: Stat
    agility: Stat
    dexterity: Stat
    vitality: Stat
    luck: Stat
    intelligence: Stat

    def __str__(self):
        repr = ""
        stats = self.model_dump()
        for stat in stats:
            repr += f"{stat.capitalize()}: {int(stats[stat]['base'])} + {int(stats[stat]['bonus'])}\n"
        return repr
