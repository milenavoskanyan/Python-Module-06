from elements import create_fire  # absolute import
from ..elements import create_air  # relative import (package)
from alchemy.potions import strength_potion  # absolute import


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}' mixed with '{create_fire()}'"
    )
