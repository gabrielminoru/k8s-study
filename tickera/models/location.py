from pydantic import BaseModel

class Object(BaseModel):
    name: str
    description: str
    weigth: float

    def __str__(self):
        name_info = f"---\nObject: {self.name}"
        description_info = f"Description: {self.description}\n---"
        weigth_info = f"Weigth: {self.weigth}\n"
        return name_info + weigth_info + description_info

class Location(BaseModel):
    name: str
    description: str
    objects: list[Object]

    def __str__(self):
        name_info = f"---\nLocation: {self.name}\n"
        description_info = f"Description: {self.description}\n---"
        objects = f"Objects: {', '.join([o.name for o in self.objects])}\n"
        return name_info + objects + description_info