def suggest_action(pattern):
    if pattern == "health_risk":
        return "Start mosquito fogging and issue public health advisory."

    elif pattern == "water_risk":
        return "Inspect water pipelines and alert residents to avoid usage."

    else:
        return "No immediate action required."