from dataclasses import dataclass, field
from pathlib import Path
from typing import List



@dataclass(frozen=True)
class Credentials:
    email: str
    password: str


# Ингредиенты и рецепт
@dataclass
class Ingredient:
    name: str
    weight_g: int

    def as_display(self) -> str:
        return f"{self.name} - {self.weight_g} г"


@dataclass
class Recipe:
    title: str
    cooking_time_min: int
    description: str
    ingredients: List[Ingredient] = field(default_factory=list)

    @property
    def ingredient_names(self) -> List[str]:
        return [i.name for i in self.ingredients]

    @property
    def ingredient_displays(self) -> List[str]:
        return [i.as_display() for i in self.ingredients]


# Пути к ассетам
class Assets:

    DIR = Path.cwd() / "assets"

    @staticmethod
    def file(name: str) -> Path:
        return (Assets.DIR / name).resolve()


# Тестовая сборка
class TestData:
    CREDENTIALS = Credentials(
        email="weiwei@blizzard.lich",
        password="14881488q",
    )

    RECIPE = Recipe(
        title="Блинчики",
        cooking_time_min=5,
        description="смешать",
        ingredients=[
            Ingredient("молоко", 100),
            Ingredient("мука", 300),
        ],
    )

    ASSETS = Assets
