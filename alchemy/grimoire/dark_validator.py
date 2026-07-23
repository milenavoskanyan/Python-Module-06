from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    for ingr in allowed_ingredients:
        if ingr.casefold() in ingredients.casefold():
            isvalid: str = "VALID"
            break
    else:
        isvalid: str = "INVALID"
    return f"{ingredients} - {isvalid}"