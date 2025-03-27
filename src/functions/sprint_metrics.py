import random

def get_sprint_progress():
    """Simulates sprint progress in %."""
    return random.randint(40, 100)  # Fake progress between 40% and 100%

def get_velocity():
    """Simulates velocity in story points."""
    return random.randint(20, 50)  # Fake velocity between 20 and 50 story points

def get_burndown_chart():
    """Simulates burndown chart data."""
    days = list(range(1, 11))  # Sprint days
    remaining_work = [random.randint(10, 50) for _ in days]  # Fake work remaining
    return {"days": days, "remaining_work": remaining_work}

def get_open_impediments():
    """Simulates a list of current impediments."""
    impediments = [
        "Blocked by API issue",
        "Waiting for UI design",
        "Database migration delay",
        "Dependency on external team"
    ]
    return random.sample(impediments, k=random.randint(0, 2))  # Return 0-2 impediments

def get_bug_status():
    """Simulates bug count in the sprint."""
    open_bugs = random.randint(0, 10)
    resolved_bugs = random.randint(5, 20)
    return {"open": open_bugs, "resolved": resolved_bugs}

if __name__ == "__main__":
    # Quick test to see the simulated data
    print("Sprint Progress:", get_sprint_progress(), "%")
    print("Velocity:", get_velocity(), "story points")
    print("Burndown Chart:", get_burndown_chart())
    print("Open Impediments:", get_open_impediments())
    print("Bug Status:", get_bug_status())
