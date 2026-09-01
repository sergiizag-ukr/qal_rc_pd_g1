import minerals

def hardest_minerals(n=3):
    
    sorted_minerals = sorted(minerals.MINERAL_CATALOG, key = lambda name: minerals.MINERAL_CATALOG[name]["hardness"], reverse=True)

    result = []
    for i in range(n):
        result.append(sorted_minerals[i])

    return result

def search_by_origin(origin_keyword):

    result = []

    for name in minerals.MINERAL_CATALOG:
        if origin_keyword.lower() in minerals.MINERAL_CATALOG[name]["origin"].lower():
            result.append(name)

    return result

