from . import minerals
from . import observations


def summary():

    num_minerals = len(minerals.MINERAL_CATALOG)
    num_obser = len(observations.get_observations())

    researchers = []
    quantity = 0
    best_researcher = ""

    for i in observations._journal:
        researchers.append(i["researcher"])

    if len(observations._journal) > 0:
        for name in researchers:
            if researchers.count(name) > quantity:
                best_researcher = name
                quantity = researchers.count(name)
        result = best_researcher
    else:
        result = "Спостережень ще немає"

    return (f"Мінералів у каталозі: {num_minerals},\n"
            f"Спостережень у журналі: {num_obser},\n"
            f"Найактивніший дослідник: {result} ")
        
def mineral_report(name):

    if minerals.get_mineral(name) is None:
        return f"Мінерал '{name}' відсутній у каталозі"

    mineral = minerals.get_mineral(name)
    observation = observations.get_observations(name)

    return (f" Mineral: {mineral} ,\n"
            f"Observation: {observation}")



    


