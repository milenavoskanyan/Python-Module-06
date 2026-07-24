from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients: list[str] = dark_spell_allowed_ingredients()
    isvalid: str = "INVALID"
    for ingr in allowed_ingredients:
        if ingr.casefold() in ingredients.casefold():
            isvalid = "VALID"
            break
    return f"{ingredients} - {isvalid}"
