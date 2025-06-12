def get_disruption_level(delay_minutes: int) -> int:
    if delay_minutes < 30:
        return 1
    elif delay_minutes < 90:
        return 2
    else:
        return 3

def suggest_action(level: int) -> str:
    mapping = {
        1: "You're good! No immediate action needed.",
        2: "Check with your airline or app for rerouting options.",
        3: "Talk to gate staff immediately and look into alternate routes.",
    }
    return mapping.get(level, "No suggestion.")
