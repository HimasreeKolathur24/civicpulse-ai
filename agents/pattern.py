def detect_pattern(data):
    count = {"health": 0, "water": 0}

    for d in data:
        if d["type"] in count:
            count[d["type"]] += 1

    if count["health"] >= 3:
        return "health_risk"
    elif count["water"] >= 2:
        return "water_risk"
    else:
        return "normal"