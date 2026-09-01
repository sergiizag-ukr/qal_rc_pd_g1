MINERAL_CATALOG = {"Алмаз":{
        "formula": "C",
        "hardness": 10,
        "origin": "Африка",
        "discovered": 1867
    },
    "Корунд": {
        "formula": "Al₂O₃",
        "hardness": 9,
        "origin": "Індія",
        "discovered": 1800
    },
    "Топаз": {
        "formula": "Al₂SiO₄(F,OH)₂",
        "hardness": 8,
        "origin": "Бразилія",
        "discovered": 1737
    },
    "Кварц": {
        "formula": "SiO₂",
        "hardness": 7,
        "origin": "Урал",
        "discovered": 1845
    },
    "Малахіт": {
        "formula": "Cu₂CO₃(OH)₂",
        "hardness": 4,
        "origin": "Урал",
        "discovered": 1747
    }
}


def get_mineral(mineral):
    for i in MINERAL_CATALOG:
        if i == mineral:
            return MINERAL_CATALOG[i]
    return None

def register_mineral(name, formula, hardness, origin, discovered):

    for i in MINERAL_CATALOG:
        if i == name:
            return f"Мінерал '{name}' вже зареєстровано в каталозі"

    if hardness < 1 or hardness > 10:
        return "Некоректна твердість: має бути від 1 до 10"
        
    MINERAL_CATALOG[name] = {
        "formula": formula,
        "hardness": hardness,
        "origin": origin,
        "discovered": discovered
        }
    return f"Мінерал '{name}' додано до каталогу"