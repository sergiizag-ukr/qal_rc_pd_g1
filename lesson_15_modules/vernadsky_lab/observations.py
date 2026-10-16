from . import minerals
import datetime

_journal = []


def record(researcher, mineral_name, note):
    if minerals.get_mineral(mineral_name) is None:
        return f"Мінерал '{mineral_name}' не зареєстровано. Спочатку додайте його до каталогу"
    else:
        _journal.append({"researcher": researcher,
                         "mineral": mineral_name,
                         "note": note,
                         "date": datetime.date.today()
                         })
        return f"Спостереження записано: {researcher} → {mineral_name}"

def get_observations(mineral_name=None):

    observations =[]

    if len(_journal) == 0:
        return observations

    if mineral_name is None:
            return _journal

    for i in _journal:
            if i["mineral"] == mineral_name:
                observations.append(i)
    return observations

    
    
    
    
        

    
