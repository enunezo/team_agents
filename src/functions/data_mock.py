import random
def manage_backlog():
    return {
        "high_priority": ["Fix checkout bug", "Improve login security"],
        "medium_priority": ["Dark mode feature", "Refactor dashboard UI"],
        "low_priority": ["Add Easter egg"]
    }

def get_sprint_metrics():
    return {
        "sprint_status": random.choice(["Active", "Completed", "Upcoming"]),
        "velocity": f"{random.randint(20, 40)} story points",
        "burn_down_chart": "https://example.com/burn_down_chart.png"
    }

def get_sprint_impediments():
    return [
        {"issue": "Database performance issues", "assigned_to": "Alice (Dev)"},
        {"issue": "API rate limit exceeded", "assigned_to": "Bob (QA)"}
    ]

def get_test_status():
    return {
        "total_tests": 120,
        "passed": 100,
        "failed": 15,
        "blocked": 5
    }

def get_bug_report():
    return [
        {"bug": "Login failure on mobile", "status": "Open", "assigned_to": "Charlie (Dev)"},
        {"bug": "Payment gateway timeout", "status": "In Progress", "assigned_to": "Alice (Dev)"}
    ]

def get_dev_task_info():
    return {
        "ticket": "DEV-123",
        "status": "In Progress",
        "impediments": ["Waiting for API update"],
        "release_history": ["Release 1.0.0 - Deployed", "Release 1.1.0 - Scheduled"]
    }

def get_technical_requirements():
    return {
        "🛠️ Technical requirements: ",
        "1. API v2.0 integration",
        "2. performance optimizations, ",
        "3. database schema updates."
    }