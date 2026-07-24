def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed_ingredients: list[str] = light_spell_allowed_ingredients()
    isvalid: str = "INVALID"
    for ingr in allowed_ingredients:
        if ingr.casefold() in ingredients.casefold():
            isvalid = "VALID"
            break
    return f"{ingredients} - {isvalid}"
