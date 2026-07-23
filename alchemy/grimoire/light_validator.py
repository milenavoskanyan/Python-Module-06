def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    for ingr in allowed_ingredients:
        if ingr.casefold() in ingredients.casefold():
            isvalid: str = "VALID"
            break
    else:
        isvalid: str = "INVALID"
    return f"{ingredients} - {isvalid}"