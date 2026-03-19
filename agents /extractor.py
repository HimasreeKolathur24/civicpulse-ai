def extract_data(texts):
    results = []

    for t in texts:
        t_lower = t.lower()

        if "fever" in t_lower or "cough" in t_lower:
            category = "health"
            location = "ward 1" if "ward 1" in t_lower else "unknown"

        elif "water" in t_lower or "smell" in t_lower:
            category = "water"
            location = "ward 2" if "ward 2" in t_lower else "unknown"

        else:
            category = "other"
            location = "unknown"

        results.append({
            "text": t,
            "type": category,
            "location": location
        })

    return results
